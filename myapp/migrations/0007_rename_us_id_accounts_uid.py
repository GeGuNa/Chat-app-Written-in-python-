# Generated by Django 4.2.11 on 2024-04-04 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_accounts_us_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='us_id',
            new_name='uid',
        ),
    ]
