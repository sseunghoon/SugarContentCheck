# Generated by Django 3.2.2 on 2021-05-10 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_intentsity_choice_intensity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='unit',
            new_name='belong',
        ),
    ]
