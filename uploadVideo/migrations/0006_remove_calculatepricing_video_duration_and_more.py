# Generated by Django 4.0.6 on 2022-07-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadVideo', '0005_calculatepricing_receivevideo_uploaded_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculatepricing',
            name='video_duration',
        ),
        migrations.RemoveField(
            model_name='calculatepricing',
            name='video_size',
        ),
        migrations.RemoveField(
            model_name='calculatepricing',
            name='video_type',
        ),
        migrations.AddField(
            model_name='calculatepricing',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='calculatepricing',
            name='size',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='calculatepricing',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
