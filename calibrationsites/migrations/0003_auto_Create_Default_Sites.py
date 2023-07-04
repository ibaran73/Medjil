# Generated by Django 3.1 on 2020-11-10 00:11

from __future__ import unicode_literals

from django.db import migrations, models
import os
from shutil import copyfile
from datetime import datetime, date
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings
import os
#########################################################################
################################ STAFF ##################################
boya = {
    'site_type' : 'staff_range',
    'site_name' : 'Boya',
    'site_address' : 'Victor Road, Darlington',
    'country' : 'Australia',
    'state' : 'WA',
    'locality': 'Boya',
    'no_of_pillars': '21',
    'operator' : 'Landgate',
    'site_access' : os.path.join(settings.MEDIA_ROOT, 'InitialData/Staff Range/Australia/WA/Boya/Access/Boya Access Sketch.pdf'),
    'site_config' : os.path.join(settings.MEDIA_ROOT, 'InitialData/Staff Range/Australia/WA/Boya/Access/Boya Pin Configuration.pdf'),
}    

muncheng = {
    'site_type' : 'staff_lab',
    'site_name' : 'Geodetic Laboratory at Munich',
    'site_address' : 'Technical University of Munich',
    'country' : 'Germany',
    'state' : 'BY',
    'locality': 'Munchen',
    'no_of_pillars': '',
    'operator' : 'Landgate',
    'site_access' : '',
    'site_config' : '',
}    
#########################################################################
################################ EDM ####################################
edm_sites = [{
    'site_type' : 'baseline',
    'site_name' : 'Curtin',
    'site_address' : 'Kent Street',
    'country' : 'Australia',
    'state' : 'WA',
    'locality': 'Bentley',
    'no_of_pillars': 11,
    'operator' : 'Landgate',
    'site_access' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Curtin/Curtin EDM Baseline Access Sketch.pdf'),
    'site_config' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Curtin/Curtin EDM Baseline Pillar Configuration.pdf')
},{
    'site_type' : 'baseline',
    'site_name' : 'Curtin 12 Pillar',
    'site_address' : 'Kent Street',
    'country' : 'Australia',
    'state' : 'WA',
    'locality': 'Bentley',
    'no_of_pillars': 12,
    'operator' : 'Landgate',
    'site_access' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Curtin/Curtin EDM Baseline Access Sketch.pdf'),
    'site_config' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Curtin/Curtin EDM Baseline Pillar Configuration.pdf')
},{
    'site_type' : 'baseline',
    'site_name' : 'Busselton',
    'site_address' : 'Busselton Bypass Road',
    'country' : 'Australia',
    'state' : 'WA',
    'locality': 'Busselton-Vasse',
    'no_of_pillars': 6,
    'operator' : 'Landgate',
    'site_access' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Busselton/Busselton EDM Baseline Access Sketch.pdf'),
    'site_config' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Busselton/Busselton EDM Baseline Pillar Configuration.pdf'),
},{
   'site_type' : 'baseline',
    'site_name' : 'Kalgoorlie',
    'site_address' : 'Piccadilly Street',
    'country' : 'Australia',
    'state' : 'WA',
    'locality': 'Kalgoorlie-Boulder',
    'no_of_pillars': 8,
    'operator' : 'Landgate',
    'site_access' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Kalgoorlie/Kalgoorlie EDM Baseline Access Sketch.pdf'),
    'site_config' : os.path.join(settings.MEDIA_ROOT, 'InitialData/EDM Baseline/Australia/WA/Kalgoorlie/Kalgoorlie EDM Baseline Pillar Configuration.pdf')
}]

site_types = (
        (None, '--- Select Type ---'),
        # ('edm_lab', 'EDM Calibration Laboratory'),
        ('baseline','EDM Calibration Baseline'),
        ('staff_lab', 'Staff Calibration Laboratory'),
        ('staff_range','Staff Calibration Range'),               
        )
        
#########################################################################
def get_upload_to_location(instance, filename):
    creation_date = date.today().strftime('%Y-%m-%d')
    return '%s/%s/%s/%s/%s' % ('CalibrationSite', instance.site_type.capitalize(), instance.state.statecode, instance.site_name, creation_date+'-'+ filename)

file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media')) #

def load_initial_data(apps, schema_editor):
    
    Company = apps.get_model("accounts", "Company")
    Country = apps.get_model("calibrationsites", "Country")
    State = apps.get_model("calibrationsites", "State")
    Locality = apps.get_model("calibrationsites", "Locality")
    CalibrationSite = apps.get_model('calibrationsites', 'CalibrationSite')
    
    
    boya_site, created = CalibrationSite.objects.get_or_create(
        site_type = boya['site_type'],
        site_name = boya['site_name'],
        site_address = boya['site_address'],
        country = Country.objects.get(name = boya['country']),
        state = State.objects.get(statecode = boya['state']),
        locality = Locality.objects.get(name = boya['locality']),
        no_of_pillars = boya['no_of_pillars'],
        operator = Company.objects.get(company_name = boya['operator']),
        site_access = File(open(boya['site_access'], 'rb'), name = boya['site_access'].split('/')[-1]),
        site_config = File(open(boya['site_config'], 'rb'), name = boya['site_config'].split('/')[-1]),
    )
    
    munchen_site, created = CalibrationSite.objects.get_or_create(
        site_type = muncheng['site_type'],
        site_name = muncheng['site_name'],
        site_address = muncheng['site_address'],
        country = Country.objects.get(name = muncheng['country']),
        state = State.objects.get(statecode = muncheng['state']),
        locality = Locality.objects.get(name = muncheng['locality']),
        # no_of_pillars = muncheng['no_of_pillars'],
        operator = Company.objects.get(company_name = muncheng['operator']),
        # site_access = File(open(boya['site_access'], 'rb'), name = boya['site_access'].split('/')[-1]),
        # site_config = File(open(boya['site_config'], 'rb'), name = boya['site_config'].split('/')[-1]),
    )
    
    for edm_site in edm_sites:
        site, created = CalibrationSite.objects.get_or_create(
            site_type = edm_site['site_type'],
            site_name = edm_site['site_name'],
            site_address = edm_site['site_address'],
            country = Country.objects.get(name = edm_site['country']),
            state = State.objects.get(statecode = edm_site['state']),
            locality = Locality.objects.get(name = edm_site['locality']),
            no_of_pillars = edm_site['no_of_pillars'],
            operator = Company.objects.get(company_name = edm_site['operator']),
            site_access = File(open(edm_site['site_access'], 'rb'), name = edm_site['site_access'].split('/')[-1]),
            site_config = File(open(edm_site['site_config'], 'rb'), name = edm_site['site_config'].split('/')[-1]),
        )

def reverse_func(apps, schema_editor):
    CalibrationSite = apps.get_model('calibrationsites', 'CalibrationSite')
    Calibration.objects.filter(site_name = boya['site_name']).delete()
    

class Migration(migrations.Migration):

    dependencies = [
        ('calibrationsites', '0002_auto_Create_Default_Locations'),
    ]

    operations = [
        migrations.RunPython(load_initial_data, reverse_func),
    ]
