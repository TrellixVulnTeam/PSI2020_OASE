# Generated by Django 3.1.3 on 2021-01-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_Shop', '0017_auto_20210131_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(blank=True, default=None, max_length=45)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
