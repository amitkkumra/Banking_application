# Generated by Django 2.1.7 on 2021-04-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210405_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
