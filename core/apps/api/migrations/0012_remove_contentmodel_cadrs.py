# Generated by Django 5.1.3 on 2024-12-06 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_cadrmodel_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentmodel',
            name='cadrs',
        ),
    ]