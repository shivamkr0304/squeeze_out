# Generated by Django 4.1.4 on 2023-03-24 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homeApp', '0006_remove_student_sub_fac_feedback_feedback_fac1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_sub_fac_feedback',
            name='roll_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]