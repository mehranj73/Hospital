# Generated by Django 3.1.3 on 2020-11-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20201110_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateTimeField(),
        ),
    ]
