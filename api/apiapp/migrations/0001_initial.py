# Generated by Django 5.0.6 on 2024-06-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=20)),
                ('emp_phone', models.CharField(max_length=20)),
                ('emp_place', models.CharField(max_length=25)),
                ('emp_image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
