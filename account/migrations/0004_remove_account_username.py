# Generated by Django 3.2.2 on 2021-09-23 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_name_account_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
    ]