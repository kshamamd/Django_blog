# Generated by Django 3.1.3 on 2020-12-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201202_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.BooleanField(default='False'),
        ),
    ]