# Generated by Django 3.1 on 2020-11-12 02:23
import csv
from django.db import migrations, models
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings
import os
# Start migration
lg_prism_specs = [
    {'manu_unc_const':0.3,
    'manu_unc_k':2,
    'prism_model':'GPH1P',
    'prism_owner':'Landgate'}
    ]
lg_prisms = [
    {'prism_number':100,
    'photo':'',
    'comment':'EDM Baseline Calibration Prism',
    'prism_custodian_id':'',
    'prism_model':'GPH1P'}
    ]
lg_edms_specs = [
    {'edm_type':'ph',
    'manu_unc_const':1,
    'manu_unc_ppm':1.5,
    'manu_unc_k':2,
    'unit_length':1.5,
    'frequency':100,
    'carrier_wavelength':658,
    'manu_ref_refrac_index':1.000286338,
    'measurement_increments':0.0001,
    'edm_model':'TS 16',
    'edm_owner':'Landgate'},
    {'edm_type':'ph',
    'manu_unc_const':0.6,
    'manu_unc_ppm':1,
    'manu_unc_k':2,
    'unit_length':1.5,
    'frequency':100,
    'carrier_wavelength':658,
    'manu_ref_refrac_index':1.000286338,
    'measurement_increments':0.0001,
    'edm_model':'TS 30',
    'edm_owner':'Landgate'}]
lg_edms = [
    {'edm_number':364182,
    'photo':'',
    'comment':'EDM Baseline Calibration REG13 Instrument',
    'edm_custodian':'Landgate',
    'edm_model':'TS 30'},
    {'edm_number':3012827,
    'photo':'',
    'comment':'Intercomparison Instrument',
    'edm_custodian':'Landgate',
    'edm_model':'TS 16'}
    ]
lg_edmi_certs = [
    {'calibration_date':'2013-08-15',
    'scale_correction_factor':0.99999974,
    'scf_uncertainty':0.00000014,
    'scf_coverage_factor':2.1,
    'scf_std_dev':6.66666666666667E-08,
    'zero_point_correction':0.00048,
    'zpc_uncertainty':0.00017,
    'zpc_coverage_factor':2.1,
    'zpc_std_dev':0.000080952380952381,
    'standard_deviation':0.15,
    'degrees_of_freedom':14,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData/Landgate Instruments/EDMIs/364182/2013_TS30_Calibration_Report.pdf'),
    'edm_number':364182,
    'prism_number':100},
    {'calibration_date':'2015-06-17',
    'scale_correction_factor':0.999999991,
    'scf_uncertainty':0.000000033,
    'scf_coverage_factor':2,
    'scf_std_dev':0.0000000165,
    'zero_point_correction':0.00065,
    'zpc_uncertainty':0.00024,
    'zpc_coverage_factor':2,
    'zpc_std_dev':0.00012,
    'standard_deviation':0.00022,
    'degrees_of_freedom':14,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData/Landgate Instruments/EDMIs/364182/2015_TS30_Calibration_Report.pdf'),
    'edm_number':364182,
    'prism_number':100},
    {'calibration_date':'2017-06-14',
    'scale_correction_factor':0.99999986,
    'scf_uncertainty':0.00000017,
    'scf_coverage_factor':2.1,
    'scf_std_dev':8.0952380952381E-08,
    'zero_point_correction':0.00045,
    'zpc_uncertainty':0.00021,
    'zpc_coverage_factor':2.1,
    'zpc_std_dev':0.0001,
    'standard_deviation':0.0001,
    'degrees_of_freedom':14,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData/Landgate Instruments/EDMIs/364182/2017_TS30_Calibration_Report.pdf'),
    'edm_number':364182,
    'prism_number':100},
    {'calibration_date':'2019-05-16',
    'scale_correction_factor':1.00000008,
    'scf_uncertainty':0.00000006,
    'scf_coverage_factor':2.1,
    'scf_std_dev':2.85714285714286E-08,
    'zero_point_correction':0.00032,
    'zpc_uncertainty':0.00034,
    'zpc_coverage_factor':2,
    'zpc_std_dev':0.00017,
    'standard_deviation':0.00032,
    'degrees_of_freedom':14,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData/Landgate Instruments/EDMIs/364182/2019_TS30_Calibration_Report.pdf'),
    'edm_number':364182,
    'prism_number':100},
    {'calibration_date':'2021-04-29',
    'scale_correction_factor':1.00000013,
    'scf_uncertainty':0.00000006,
    'scf_coverage_factor':2,
    'scf_std_dev':0.00000003,
    'zero_point_correction':-0.00003,
    'zpc_uncertainty':0.00016,
    'zpc_coverage_factor':2.1,
    'zpc_std_dev':7.61904761904762E-05,
    'standard_deviation':0.0003,
    'degrees_of_freedom':27,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData/Landgate Instruments/EDMIs/364182/2021_TS30_Calibration_Report.pdf'),
    'edm_number':364182,
    'prism_number':100}
    ]
lg_mets_specs = [
    {'manu_unc_const':0.3,
    'manu_unc_k':2,
    'measurement_increments':0.01,
    'type':'baro',
    'mets_model':'DPI740',
    'mets_owner':'Landgate'},
    {'manu_unc_const':0.6,
    'manu_unc_k':2,
    'measurement_increments':0.1,
    'type':'thermo',
    'mets_model':'HD 2301.0R - HP472ACR',
    'mets_owner':'Landgate'},
    {'manu_unc_const':3,
    'manu_unc_k':2,
    'measurement_increments':0.1,
    'type':'hygro',
    'mets_model':'HD 2301.0R - HP472ACR',
    'mets_owner':'Landgate'}
    ]
lg_mets_insts = [
    {'mets_number':74003848,
    'comment':'EDM Baseline Calibration Baro',
    'photo':os.path.join(settings.MEDIA_ROOT, 'InitialData\Landgate Instruments\Mets Photos\DRUCK_DPI_740.pdf'),
    'mets_custodian_id':'',
    'type':'baro',
    'mets_model':'DPI740'},
    {'mets_number':20013647,
    'comment':'EDM Baseline Calibration Them',
    'photo':os.path.join(settings.MEDIA_ROOT, 'InitialData\Landgate Instruments\Mets Photos\DELTA_OHM.pdf'),
    'mets_custodian_id':'',
    'type':'thermo',
    'mets_model':'HD 2301.0R - HP472ACR'},
    {'mets_number':20013647,
    'comment':'EDM BaselineExternal Temperature/RH Probe',
    'photo':os.path.join(settings.MEDIA_ROOT, 'InitialData\Landgate Instruments\Mets Photos\DELTA_OHM.pdf'),
    'mets_custodian_id':'',
    'type':'hygro',
    'mets_model':'HD 2301.0R - HP472ACR'}
    ]
lg_mets_certs = [
    {'calibration_date':'2021-03-22',
    'zero_point_correction':0.04,
    'zpc_uncertainty':0.13,
    'zpc_coverage_factor':2,
    'zpc_std_dev':0.065,
    'degrees_of_freedom':30,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData\Landgate Instruments\Mets Certificates\2021_74003848_Barometer_Calibration.pdf'),
    'type':'baro',
    'mets_number':74003848},
    {'calibration_date':'2021-04-14',
    'zero_point_correction':0,
    'zpc_uncertainty':0.2,
    'zpc_coverage_factor':2,
    'zpc_std_dev':0.1,
    'degrees_of_freedom':30,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData\Landgate Instruments\Mets Certificates\2021_20013647_Temperature_and_Relative_Humidity_Meter.pdf'),
    'type':'thermo',
    'mets_number':20013647},
    {'calibration_date':'2021-04-14',
    'zero_point_correction':0.7,
    'zpc_uncertainty':2.3,
    'zpc_coverage_factor':2,
    'zpc_std_dev':1.15,
    'degrees_of_freedom':30,
    'certificate_upload':os.path.join(settings.MEDIA_ROOT, 'InitialData\Landgate Instruments\Mets Certificates\2021_20013647_Temperature_and_Relative_Humidity_Meter.pdf'),
    'type':'hygro',
    'mets_number':20013647},
    ]


def add_landgate_instruments(apps, schema_editor):
    Company = apps.get_model("accounts", "Company")    
    CalibrationSite = apps.get_model('calibrationsites', 'CalibrationSite')
    InstrumentModel = apps.get_model("instruments", "InstrumentModel")
    DigitalLevel = apps.get_model('instruments', 'DigitalLevel')
    Staff = apps.get_model('instruments', 'Staff')
    StaffCalibrationRecord = apps.get_model('staffcalibration', 'StaffCalibrationRecord')
    medjil_edm_spec = apps.get_model('instruments', 'EDM_Specification')
    medjil_edm_inst = apps.get_model('instruments', 'EDM_Inst')
    medjil_prism_spec = apps.get_model('instruments', 'Prism_Specification')
    medjil_prism_inst = apps.get_model('instruments', 'Prism_Inst')
    medjil_edmi_certs = apps.get_model('instruments', 'EDMI_certificate')
    medjil_mets_spec = apps.get_model('instruments', 'Mets_Specification')
    medjil_mets_inst = apps.get_model('instruments', 'Mets_Inst')
    medjil_mets_certs = apps.get_model('instruments', 'Mets_certificate')

    # Add digital levels
    with open(os.path.join(settings.MEDIA_ROOT, 'InitialData/Landgate Instruments/Digital Levels/digital_levels.csv'), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        k = 0
        inst_type = 'level'
        for row in reader:
                k +=1
                make = row[1].strip()
                level_model = row[2].strip().upper()
                level_number = row[0].strip()
                level_owner = 'Landgate'
                level_obj, created = DigitalLevel.objects.get_or_create(
                        level_model = InstrumentModel.objects.get(model__exact=level_model), 
                        level_owner = Company.objects.get(company_name__exact=level_owner),
                        level_number = level_number,
                        )
    # Add bar-coded staves
    with open(os.path.join(settings.MEDIA_ROOT, 'InitialData/Landgate Instruments/Staves/staves.csv'), 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        k = 0
        inst_type = 'staff'
        for row in reader:
                k +=1
                staff_number = row[0].strip()
                staff_model = row[1].strip().upper()
                staff_type = row[2].strip()
                staff_owner = 'Landgate'
                staff_length = row[3].strip()
                thermal_coefficient = row[4].strip()
                standard_temperature = row[5].strip()
                observed_temperature = row[6].strip() 
                scale_factor = row[7].strip()
                graduation_uncertainty = row[8].strip()
                calibration_date = row[9].strip()
                observer = row[10].strip()
                site_name = row[11].strip()
                field_book = row[12].strip()
                calibration_report = row[13].strip()
                job_number = row[14].strip()
                level_model = row[15].strip()

                calibration_date = datetime.strptime(calibration_date, '%d/%m/%Y').date()
                staff_obj, created = Staff.objects.get_or_create(
                        staff_model = InstrumentModel.objects.get(model__exact=staff_model), 
                        staff_type = staff_type,
                        staff_owner = Company.objects.get(company_name__exact=staff_owner),
                        staff_number = staff_number,
                        staff_length = staff_length,
                        thermal_coefficient = thermal_coefficient,
                        )
                # print(level_model)
                record_obj, created = StaffCalibrationRecord.objects.get_or_create(
                    job_number = job_number,
                    inst_staff = staff_obj,
                    # inst_level = InstrumentModel.objects.get(model__exact = level_model),
                    site_id = CalibrationSite.objects.get(site_name__exact = site_name),
                    scale_factor = scale_factor,
                    grad_uncertainty = graduation_uncertainty,
                    standard_temperature = standard_temperature,
                    # observed_temperature = observed_temperature,
                    # observer = observer,
                    calibration_date = calibration_date, 
                    # field_book = File(open(field_book, 'rb'), name = field_book.split('/')[-1]),
                    calibration_report = File(open(os.path.join(settings.MEDIA_ROOT, calibration_report), 'rb'), name = calibration_report.split('/')[-1]),
                )
                if level_model:
                        record_obj.inst_level = DigitalLevel.objects.get(level_model__model__exact = level_model)
                if observed_temperature:
                        record_obj.observed_temperature = observed_temperature
                if observer:
                        record_obj.observer = observer
                if field_book and (record_obj.field_book == '' or not record_obj.field_book):
                        record_obj.field_book = File(open(os.path.join(settings.MEDIA_ROOT, field_book), 'rb'), name = field_book.split('/')[-1])
                record_obj.save()
    
    # Add Landgate Prism
    for spec in lg_prism_specs:
        record_obj, created = medjil_prism_spec.objects.get_or_create(
            manu_unc_const = spec['manu_unc_const'],
            manu_unc_k = spec['manu_unc_k'],
            prism_model = InstrumentModel.objects.get(
                model__exact=spec['prism_model']),
            prism_owner = Company.objects.get(
                company_name__exact=spec['prism_owner'])
            )
    for prism in lg_prisms:
        record_obj, created = medjil_prism_inst.objects.get_or_create(
            prism_number = prism['prism_number'],
            photo = prism['photo'],
            comment = prism['comment'],
            # prism_custodian = '',
            prism_specs = medjil_prism_spec.objects.get(
                prism_model__model__exact = prism['prism_model'])
            )
    # Add Landgate Total station Specifications
    for spec in lg_edms_specs:
        record_obj, created = medjil_edm_spec.objects.get_or_create(
            edm_type = spec['edm_type'],
            manu_unc_const = spec['manu_unc_const'],
            manu_unc_ppm = spec['manu_unc_ppm'],
            manu_unc_k = spec['manu_unc_k'],
            unit_length = spec['unit_length'],
            frequency = spec['frequency'],
            carrier_wavelength = spec['carrier_wavelength'],
            manu_ref_refrac_index = spec['manu_ref_refrac_index'],
            measurement_increments = spec['measurement_increments'],
            edm_model = InstrumentModel.objects.get(
                model__exact=spec['edm_model']),
            edm_owner = Company.objects.get(
                company_name__exact=spec['edm_owner'])
            )
    for edm in lg_edms:
        record_obj, created = medjil_edm_inst.objects.get_or_create(
            edm_number = edm['edm_number'],
            photo = edm['photo'],
            comment = edm['comment'],
            # edm_custodian = '',
            edm_specs = medjil_edm_spec.objects.get(
                edm_model__model__exact = edm['edm_model'],
                edm_owner__exact = Company.objects.get(
                    company_name__exact=edm['edm_custodian']))
            )
    for cert in lg_edmi_certs:
        record_obj, created = medjil_edmi_certs.objects.get_or_create(
            calibration_date = cert['calibration_date'],
            scale_correction_factor = cert['scale_correction_factor'],
            scf_uncertainty = cert['scf_uncertainty'],
            scf_coverage_factor = cert['scf_coverage_factor'],
            scf_std_dev = cert['scf_std_dev'],
            zero_point_correction = cert['zero_point_correction'],
            zpc_uncertainty = cert['zpc_uncertainty'],
            zpc_coverage_factor = cert['zpc_coverage_factor'],
            zpc_std_dev = cert['zpc_std_dev'],
            standard_deviation = cert['standard_deviation'],
            degrees_of_freedom = cert['degrees_of_freedom'],
            certificate_upload = cert['certificate_upload'],
            edm = medjil_edm_inst.objects.get(
                edm_number__exact=cert['edm_number']),
            prism = medjil_prism_inst.objects.get(
                prism_number__exact=cert['prism_number'])
            )
    # Add Landgate Mets gear
    for spec in lg_mets_specs:
        record_obj, created = medjil_mets_spec.objects.get_or_create(    
            manu_unc_const = spec['manu_unc_const'],
            manu_unc_k = spec['manu_unc_k'],
            measurement_increments = spec['measurement_increments'],
            mets_model =  InstrumentModel.objects.get(
                inst_type__exact=spec['type'],
                model__exact=spec['mets_model']),
            mets_owner = Company.objects.get(
                company_name__exact=spec['mets_owner'])
            )
    for inst in lg_mets_insts:
        record_obj, created = medjil_mets_inst.objects.get_or_create(
            mets_number = inst['mets_number'],
            comment = inst['comment'],
            photo = inst['photo'],
            # mets_custodian = inst['mets_custodian'],
            mets_specs = medjil_mets_spec.objects.get(
                mets_model__inst_type__exact=inst['type'],
                mets_model__model__exact=inst['mets_model'],
                mets_owner__exact = Company.objects.get(
                    company_name__exact='Landgate'))
            )
    for cert in lg_mets_certs:
        medjil_mets_certs.objects.get_or_create(
            calibration_date = cert['calibration_date'],
            zero_point_correction = cert['zero_point_correction'],
            zpc_uncertainty = cert['zpc_uncertainty'],
            zpc_coverage_factor = cert['zpc_coverage_factor'],
            zpc_std_dev = cert['zpc_std_dev'],
            degrees_of_freedom = cert['degrees_of_freedom'],
            certificate_upload = cert['certificate_upload'],
            instrument = medjil_mets_inst.objects.get(
                mets_specs__mets_model__inst_type__exact=cert['type'],
                mets_specs__mets_owner__exact = Company.objects.get(
                    company_name__exact='Landgate'),
                mets_number__exact=cert['mets_number'])
            )


def reverse_func(apps, schema_editor):
    DigitalLevel = apps.get_model('instruments', 'DigitalLevel')
    Staff = apps.get_model('instruments', 'Staff')
    
    DigitalLevel.objects.all().delete()
    Staff.objects.all().delete()



class Migration(migrations.Migration):

    dependencies = [
        ('calibrationsites', '0001_initial'),
        ('instruments', '0002_auto_load_default_instruments'),
        ('staffcalibration', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(add_landgate_instruments, reverse_func),
    ]
