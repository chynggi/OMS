# Generated by Django 2.2.5 on 2019-10-01 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMS', '0007_auto_20190927_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='units',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
