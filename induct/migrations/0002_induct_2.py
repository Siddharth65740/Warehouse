# Generated by Django 3.2.12 on 2022-02-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('induct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='induct_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
            ],
        ),
    ]
