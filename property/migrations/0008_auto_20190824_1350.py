# Generated by Django 2.2.4 on 2019-08-24 10:50

from django.db import migrations
import phonenumbers


def normalize_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        phonenumber = phonenumbers.parse(flat.owners_phonenumber, region='RU')
        if phonenumbers.is_valid_number(phonenumber):
            flat.owners_phone_pure = phonenumbers.format_number(phonenumber, phonenumbers.PhoneNumberFormat.E164)
        else:
            flat.owners_phone_pure = '+79999999999'
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20190824_1349'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers)
    ]
