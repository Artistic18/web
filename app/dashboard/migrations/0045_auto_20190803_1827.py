# Generated by Django 2.2.3 on 2019-08-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0044_auto_20190729_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]