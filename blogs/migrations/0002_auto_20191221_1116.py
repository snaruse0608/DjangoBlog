# Generated by Django 3.0.1 on 2019-12-21 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='update_dateeime',
            new_name='update_datetime',
        ),
    ]