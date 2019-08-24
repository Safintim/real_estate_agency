# Generated by Django 2.2.4 on 2019-08-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='owner_flats', to='property.Owner', verbose_name='Собственники'),
        ),
    ]
