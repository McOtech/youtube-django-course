# Generated by Django 5.1.6 on 2025-02-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("upload", "0002_remove_uploadedfile_file_uploadedfile_actuator_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedfile",
            name="actuator",
            field=models.FileField(default=None, null=True, upload_to="files/"),
        ),
        migrations.AlterField(
            model_name="uploadedfile",
            name="micro_controller",
            field=models.FileField(default=None, null=True, upload_to="files/"),
        ),
        migrations.AlterField(
            model_name="uploadedfile",
            name="sensor",
            field=models.FileField(default=None, null=True, upload_to="files/"),
        ),
    ]
