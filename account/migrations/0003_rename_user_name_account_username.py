# Generated by Django 3.2.2 on 2021-09-23 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210923_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_name',
            new_name='username',
        ),
    ]