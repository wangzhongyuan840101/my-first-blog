# Generated by Django 2.0.13 on 2020-09-18 03:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 3, 28, 55, 124488, tzinfo=utc)),
        ),
    ]
