# Generated by Django 3.1.3 on 2021-01-31 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_Shop', '0016_auto_20210129_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
