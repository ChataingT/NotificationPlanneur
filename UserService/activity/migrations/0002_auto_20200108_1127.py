# Generated by Django 3.0.2 on 2020-01-08 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='userId',
            new_name='userPk',
        ),
    ]