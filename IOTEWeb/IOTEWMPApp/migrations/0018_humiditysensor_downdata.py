# Generated by Django 2.2.7 on 2019-12-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IOTEWMPApp', '0017_auto_20191202_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='humiditysensor',
            name='downdata',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]