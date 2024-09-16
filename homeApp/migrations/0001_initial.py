# Generated by Django 4.1.4 on 2023-01-13 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_sub_fac_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=10)),
                ('regd_no', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('sem', models.CharField(max_length=5)),
                ('batch', models.CharField(max_length=10)),
                ('sub_id', models.CharField(max_length=5)),
                ('sub_name', models.CharField(max_length=50)),
                ('facID', models.CharField(max_length=10)),
                ('fac_name', models.CharField(max_length=50)),
                ('fac_dept', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=50)),
            ],
        ),
    ]
