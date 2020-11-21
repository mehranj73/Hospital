# Generated by Django 3.1.3 on 2020-11-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id_take_attendance', models.EmailField(max_length=250)),
                ('attendance_date', models.DateTimeField()),
                ('staff', models.ManyToManyField(to='staff.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceDoctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id_take_attendance', models.EmailField(max_length=250)),
                ('attendance_date', models.DateTimeField()),
                ('doctor', models.ManyToManyField(to='doctor.Doctor')),
            ],
        ),
    ]
