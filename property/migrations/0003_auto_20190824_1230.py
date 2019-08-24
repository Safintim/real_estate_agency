# Generated by Django 2.2.4 on 2019-08-24 09:30

from django.db import migrations


def install_value_for_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(install_value_for_new_building)
    ]
