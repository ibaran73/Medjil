# Generated by Django 3.1 on 2020-11-13 05:50

from django.db import migrations
import os
import pandas as pd
import numpy as np
from math import sqrt
import csv
from datetime import datetime
from django.db import IntegrityError, transaction
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
###############################################################################
########################## FILE HANDLING ######################################
###############################################################################
def IsNumber(value):
    "Checks if string is a number"
    try:
        float(value)
        check = True
    except:
        check = False
    return(check)

# Check file type and read the measurements
def check_filetype(input_file):
    readings = open(input_file, 'r', encoding='utf-8').read().split("\n")
    fileType = None
    # readings = dataset.read().decode("utf-8").split("\n")
    fileType = None
    for line in readings:
        # print(line)
        if "BFOD" in line:
            fileType = "BFOD"
        elif "Level Type" in line:
            fileType = "DNA03"
            break

    # return fileType
    if fileType == "BFOD":
        return ImportBFOD_v18(readings)
    elif fileType == "DNA03":
        return ImportDNA(readings)

# File Format produced by LS15
def ImportBFOD_v18(raw_data):
    # Initialise array
    Blocks = []; block = []
    # Read data
    for line in raw_data:# f:
        line = line.strip()
        col = line.split('|')[1:]
        
        # Start level run 
        if line.startswith('|---------|---------|---------|---------|------------'):
            if block:
                Blocks.append(block)
                block = []
        elif len(col) == 11:
            block.append(col)
    if block:
        Blocks.append(block)  
    #----------------------------------------------------------------------
    # Finally store the staff readings into a table/list format and store    
    readings = {}
    j = 0
    for i in range(len(Blocks)):
        block = Blocks[i]
        if len(block)>7:
            j += 1
            tmp = []
            for r in block:
                r = [x.strip() for x in r]
                if (IsNumber(r[0]) or IsNumber(r[1]) or IsNumber(r[2])):
                    if IsNumber(r[0]):
                        pillar = r[8]; reading = r[0]; nreadings = r[6]; stdev = r[7]; 
                    elif IsNumber(r[1]):
                        pillar = r[8]; reading = r[1]; nreadings = r[6]; stdev = r[7]; 
                    elif IsNumber(r[2]):
                        pillar = r[8]; reading = r[2]; nreadings = r[6]; stdev = r[7]; 
                    tmp.append([pillar, float(reading), nreadings, float(stdev)])
            tmp  = pd.DataFrame(tmp, columns=['PILLAR','READING','COUNT','STD_DEVIATION'])
            # Update dictionary
            readings.update({'Set'+str(j):tmp})
    return readings

# File Format produced by DNA03
def ImportDNA(raw_data):
    # Initialise array
    Blocks = []; block = []
    # Read data
    for line in raw_data:
        line = line.strip()
        # print(line)
        col = line.split('|')[1:]
        # Start level run 
        if line.endswith('| MS |___DEV__|___________|'):
            if block:
                Blocks.append(block)
                block = []
        elif len(col) == 10:
            block.append(col)
    if block:
        Blocks.append(block)      
    #----------------------------------------------------------------------
    # Finally store the staff readings into a table/list format and store
    readings = {}
    j = 0
    for i in range(len(Blocks)):
        block = Blocks[i]
        if len(block)>7:
            j += 1
            # Append items
            pillar = []; reading = []; stdev = []; nreadings = None
            tmp = []
            for r in block:
                r = [x.strip() for x in r]
                
                if (IsNumber(r[0]) or IsNumber(r[1]) or IsNumber(r[2])):
                    if IsNumber(r[0]):
                        pillar = r[8]; reading = r[0]; stdev = r[7]; nreadings = r[6]
                    elif IsNumber(r[1]):
                        pillar = r[8]; reading = r[1]; stdev = r[7];
                    elif IsNumber(r[2]):
                        pillar = r[8]; reading = r[2]; stdev = r[7];
                    
                    tmp.append([pillar, float(reading), nreadings, float(stdev)])
            tmp  = pd.DataFrame(tmp, columns=['PILLAR','READING','COUNT','STD_DEVIATION'])
            readings.update({'Set'+str(j):tmp})
    return readings

# Apply Corrections to staff Readings
def calculate_length(dato, sf, coe, t_0, t_ave, oset):
    from math import sqrt

    data_table = []
    pillarlist = []
    for i in range(len(dato)-1):
        pillari, obsi, nmeasi, stdi= dato[i] 
        pillarj, obsj, nmeasj, stdj = dato[i+1]
        if stdi == 0:
            stdi = 10**-5
        if stdj == 0:
            stdj = 10**-5
        dMeasuredLength = obsj- obsi
        dCorrection = (sf)*(1+coe*(float(t_ave)-t_0))
        cMeasuredLength = dMeasuredLength*dCorrection
        dStdDeviation = sqrt(float(stdi)**2 + float(stdj)**2)
        data_table.append([str(oset), pillari+'-'+pillarj, '{:.1f}'.format(float(t_ave)),
                                    '{:.5f}'.format(obsi), '{:.5f}'.format(obsj), '{:.6f}'.format(dStdDeviation),
                                    '{:.5f}'.format(dMeasuredLength), '{:.5f}'.format(cMeasuredLength)])
        if not pillari in pillarlist:
            pillarlist.append(pillari)
        if not pillarj in pillarlist:
            pillarlist.append(pillarj)
    return pillarlist, data_table

# Dictionary to table format - staff readings
def rawdata_to_table(dataset, t_avg1, t_avg2, staff_atrs):
    dCorrectionFactor = staff_atrs['dCorrectionFactor']
    dThermalCoefficient = staff_atrs['dThermalCoefficient']
    dStdTemperature = staff_atrs['dStdTemperature']
    rawReportTable = []
    uniquePillarList = []
    for key, value in dataset.items():
        if key.startswith("Set1"):
            obs_set = 1
            pillar_list1, dataset1 = calculate_length(value.values, dCorrectionFactor, dThermalCoefficient, dStdTemperature, t_avg1, obs_set)
        elif key.startswith("Set2"):
            obs_set = 2
            pillar_list2, dataset2 = calculate_length(value.values, dCorrectionFactor, dThermalCoefficient, dStdTemperature, t_avg2, obs_set)

    rawReportTable = {'headers': ['SET','PILLAR','TEMPERATURE','FROM','TO', 'STD_DEVIATION', 'MEASURED', 'CORRECTED'], 'data': dataset1+dataset2}
    
    # Get the list of pins/pillars
    pillar_list2 = pillar_list1 + pillar_list2
    for pillars in pillar_list2:
        if not pillars in uniquePillarList:
            uniquePillarList.append(pillars)

    return uniquePillarList, rawReportTable
# ###############################################################################
def upload_range_data(apps, schema_editor):  
    CalibrationSite = apps.get_model("calibrationsites", "CalibrationSite")
    Pillar = apps.get_model("calibrationsites", "Pillar")
    Staff = apps.get_model("instruments", "Staff")
    DigitalLevel = apps.get_model("instruments", "DigitalLevel")
    StaffCalibrationRecord = apps.get_model("staffcalibration", "StaffCalibrationRecord")
    RangeCalibrationRecord = apps.get_model('rangecalibration', 'RangeCalibrationRecord')

    RawDataModel = apps.get_model("rangecalibration", "RawDataModel")
    AdjustedDataModel = apps.get_model("rangecalibration", "AdjustedDataModel")
    HeightDifferenceModel = apps.get_model("rangecalibration", "HeightDifferenceModel")
    BarCodeRangeParam = apps.get_model("rangecalibration", "BarCodeRangeParam")

	# Starting to read the files
    range_dir = "data_preload/Staff Range/Australia/WA/Boya/Range Calibration"
    FileDir = os.path.join(range_dir, '20172297')
    # Reading the temperature record
    if os.path.exists(os.path.join(range_dir, 'calibration_record.csv')):
        with open(os.path.join(range_dir, 'calibration_record.csv'), 'r', newline='') as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            calibration_record = []
            for row in csv_reader:
                print (row)
                observation_date = datetime.strptime(row[0], '%d/%m/%Y').date()
                site_name = row[1].strip()
                staff_number = row[2].strip()
                level_number = row[3].strip()
                start_temperature1 = float(row[4])
                end_temperature1 = float(row[5])
                start_temperature2 = float(row[6])
                end_temperature2 = float(row[7])
                job_number = row[8].strip()
                observer = row[9].strip()
                
                calibration_record.append([
                                    observation_date.strftime('%Y%m%d')+'-'+staff_number,
                                    observation_date,
                                    site_name,
                                    staff_number,
                                    level_number,
                                    start_temperature1,
                                    end_temperature1,
                                    start_temperature2,
                                    end_temperature2,
                                    job_number,
                                    observer])
            calibration_record = np.array(calibration_record, dtype=object)

    # Read the  range data and process it   
    k = 0
    for root, dirs, files in os.walk(FileDir):
        k+=1
        unique_index = None
        if files == []:
            pass
        else:
            tmp = root.split('\\')[-1].split('-')
            unique_index = tmp[0]+'-'+tmp[1]
        
        if unique_index:
            fieldfile = os.path.normpath(os.path.join(root, [f for f in os.listdir(root) if f.endswith(('.asc', 'ASC'))][0]))
            fieldbook = [f for f in os.listdir(root) if f.endswith(('pdf', 'PDF'))]
            
            if fieldbook:
                fieldbook = os.path.normpath(os.path.join(root, fieldbook[0]))
            else:
                fieldbook = None
            [instance] = calibration_record[calibration_record[:,0]==unique_index]
            # Get the Variables
            observation_date = instance[1]
            siteid = CalibrationSite.objects.get(site_name__exact = instance[2])
            staffid = Staff.objects.get(staff_number__exact = instance[3])
            levelid = DigitalLevel.objects.get(level_number__exact = instance[4])
            Set_1_AvgT = (instance[5]+instance[6])/2
            Set_2_AvgT = (instance[7]+instance[8])/2
            job_number = instance[9]

            # Process File
            
            reading = check_filetype(fieldfile)
            thisCalibRecord = StaffCalibrationRecord.objects.filter(inst_staff=staffid).order_by('-calibration_date')[0]
            
            thisStaff_Attributes = {
                'dStaffLength': thisCalibRecord.inst_staff.staff_length,
                'dThermalCoefficient': thisCalibRecord.inst_staff.thermal_coefficient*10**-6,
                'dCorrectionFactor': thisCalibRecord.scale_factor, 
                'dStdTemperature': thisCalibRecord.standard_temperature,
            }
            
            # Get the Pin information & Tabulate the staff readings
            newPillarList, thisMeasurement = rawdata_to_table(reading, 
                                                    Set_1_AvgT, 
                                                    Set_2_AvgT, 
                                                    thisStaff_Attributes) # get all the elements together
            # Match pillars/pins
            eTotalPillars = siteid.no_of_pillars
            ePillars = Pillar.objects.filter(site_id = siteid).values_list('name')
            ePillars = [x[0] for x in ePillars]
            ePillarList = sorted(ePillars, key=int)
            
            # Check pins with database
            if (newPillarList == ePillarList):
                try:
                    calibid = RangeCalibrationRecord.objects.get( job_number = job_number,
                                    site_id = siteid,
                                    inst_staff = staffid,
                                    calibration_date = observation_date, 
                                )
                except ObjectDoesNotExist:
                    calibid = RangeCalibrationRecord.objects.create( job_number = job_number,
                                            site_id = siteid,
                                            inst_staff = staffid,
                                            inst_level = levelid,
                                            ave_temperature1 = Set_1_AvgT,
                                            ave_temperature2 = Set_2_AvgT,
                                            calibration_date = observation_date, 
                                            observer = observer,
                                            field_file = File(open(fieldfile, 'rb'), name = fieldfile.split('/')[-1]),
                                        )
                # print(calibid)
                if fieldbook and (calibid.field_book == '' or not calibid.field_book):
                    calibid.field_book = File(open(fieldbook, 'rb'), name = fieldbook.split('/')[-1])
                    calibid.save()
                # Create or Get the RawDataModel
                RawDataModel.objects.get_or_create(
                                        calibration_id = calibid,
                                        observation = thisMeasurement) 

                # Perform the adjust 
                rawDataSet = []; uniquePillarList = []
                for key, value in thisMeasurement.items():
                    if key == 'data':
                        for items in value:
                            rawDataSet.append(items)
                            if not items[1] in uniquePillarList:
                                uniquePillarList.append(items[1])
                
                # to Array
                rawDataSet = np.array(rawDataSet, dtype=object)
                # print(rawDataSet)
                output_adj = []; output_hdiff = []
                for i in range(len(uniquePillarList)):
                    x = uniquePillarList[i]

                    dato = rawDataSet[rawDataSet[:,1]== x]
                    if len(dato) == 1:
                        interval = dato[0][1]
                        obs_hdiff = '{:.5f}'.format(float(dato[0][-1]));
                        adj_hdiff = '{:.5f}'.format(float(dato[0][-1]));
                        resid = '{:.5f}'.format(0.0)
                        std_dev = '{:.2f}'.format(float(dato[0][-3])*1000)
                        stdev_resid = '{:.2f}'.format(0.0)
                        std_resid = '{:.2f}'.format(0.0)
                        unc = '{:.2f}'.format(float(dato[0][-3])*1000*1.96)
                        # Construct list
                        output_adj.append([
                            interval, adj_hdiff, obs_hdiff, resid, std_dev, std_resid, unc
                        ])
                        output_hdiff.append([
                            interval, adj_hdiff, unc, len(dato)
                        ])
                    elif len(dato) == 2:
                        interval = dato[0][1]
                        # Prepare the required arrays
                        W = dato[:,-1].astype(np.float); P = np.diag(1/(dato[:,-3].astype(np.float))**2); A = np.ones(len(W))
                        
                        # Perform Least squares - Refer to J.Klinge & B. Hugessen document on Calibration of Barcode staffs
                        adj_hdiff = (np.matmul(np.transpose(A), np.matmul(P, W)))/(np.matmul(np.transpose(A), np.matmul(P, A))) # (A_T*P*A)^(-1)*A_T*P*W
                        resid = np.array(adj_hdiff - W, dtype=float)
                        std_dev = np.sqrt(1./np.sqrt(np.diag(P).astype(float))**2)
                        stdev_resid = np.sqrt(1./np.sqrt(np.diag(P).astype(float))**2 - 1./sqrt(np.matmul(np.transpose(A), np.matmul(P, A)))**2)
                        unc = (sqrt(1/np.matmul(np.transpose(A), np.matmul(P, A)))*1000*1.96)
                        std_resid = np.round_(resid/stdev_resid,1)

                        # Prepare the outputs - 
                        for j in range(len(W)):
                            output_adj.append([interval, '{:.5f}'.format(adj_hdiff), '{:.5f}'.format(W[j]), '{:.5f}'.format(resid[j]),
                                            '{:.2f}'.format(std_dev[j]*1000), '{:.2f}'.format(stdev_resid[j]*1000), 
                                            '{:.1f}'.format(std_resid[j])])
                        output_hdiff.append([interval, '{:.5f}'.format(adj_hdiff), '{:.2f}'.format(unc), len(dato)])
                    # print(dato)
                
                # Update the database
                output_hdiff = {'headers': ['PILLAR','HEIGHT DIFF','UNCERTAINTY(mm)','OBSERVATION COUNT'], 'data': [list(x) for x in output_hdiff]}
                output_adj = {'headers': ['PILLAR','ADJ HEIGHT DIFF','OBS HEIGHT DIFF','RESIDUAL','STANDARD DEVIATION','STDEV RESIDUAL','STANDARD_RESIDUAL'], 'data':  [list(x) for x in output_adj]} 
                
                if not AdjustedDataModel.objects.filter(calibration_id=calibid): 
                    AdjustedDataModel.objects.create(
                                                calibration_id = calibid,
                                                adustment = output_adj) 
                if not HeightDifferenceModel.objects.filter(calibration_id=calibid): 
                    HeightDifferenceModel.objects.create(
                                                calibration_id = calibid,
                                                height_difference = output_hdiff) 

def reverse_func(apps, schema_editor):
    Calibration_Update = apps.get_model("range_calibration", "Calibration_Update")
    RawDataModel = apps.get_model("range_calibration", "RawDataModel")
    AdjustedDataModel = apps.get_model("range_calibration", "AdjustedDataModel")
    HeightDifferenceModel = apps.get_model("range_calibration", "HeightDifferenceModel")
    RangeParameters = apps.get_model("range_calibration", "RangeParameters")
	
    Calibration_Update.objects.all().delete()
    RawDataModel.objects.all().delete()
    AdjustedDataModel.objects.all().delete()
    HeightDifferenceModel.objects.all().delete()
    RangeParameters.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rangecalibration', '0001_initial'),
        ('instruments', '0002_auto_load_default_instruments'),
        
    ]

    operations = [
    		migrations.RunPython(upload_range_data, reverse_func),
    ]
