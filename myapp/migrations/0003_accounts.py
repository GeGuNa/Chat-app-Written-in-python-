# Generated by Django 4.2.11 on 2024-04-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_boobqk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('surn', models.CharField(max_length=300)),
                ('day', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
    ]
