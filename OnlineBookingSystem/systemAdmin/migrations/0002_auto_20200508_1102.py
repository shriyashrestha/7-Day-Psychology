# Generated by Django 3.0.6 on 2020-05-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]
