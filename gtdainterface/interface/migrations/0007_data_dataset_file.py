# Generated by Django 3.1.5 on 2021-01-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0006_auto_20210121_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='dataset_file',
            field=models.FileField(default=None, upload_to='media'),
        ),
    ]
