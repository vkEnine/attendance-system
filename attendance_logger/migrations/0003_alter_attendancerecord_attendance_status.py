# Generated by Django 4.2.6 on 2024-05-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_logger', '0002_attendancerecord_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='attendance_status',
            field=models.CharField(choices=[('P', 'Present'), ('L', 'Late'), ('S', 'Sick'), ('A', 'Absent')], max_length=1),
        ),
    ]