# Generated by Django 4.0.5 on 2022-07-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_topten'),
    ]

    operations = [
        migrations.AddField(
            model_name='topten',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
    ]
