# Generated by Django 4.0.6 on 2022-07-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadVideo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videodetails',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]