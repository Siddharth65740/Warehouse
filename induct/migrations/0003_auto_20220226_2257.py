# Generated by Django 3.2.12 on 2022-02-26 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('induct', '0002_induct_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='induct_2',
            old_name='destination',
            new_name='destination1',
        ),
        migrations.RenameField(
            model_name='induct_2',
            old_name='shipment',
            new_name='shipment1',
        ),
    ]
