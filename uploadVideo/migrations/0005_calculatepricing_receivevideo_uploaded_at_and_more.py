# Generated by Django 4.0.6 on 2022-07-20 16:26

import crum
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uploadVideo.custom_validations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploadVideo', '0004_alter_receivevideo_video_alter_videodetails_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatePricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_size', models.IntegerField()),
                ('video_duration', models.IntegerField()),
                ('video_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='receivevideo',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='receivevideo',
            name='user',
            field=models.ForeignKey(default=crum.get_current_user, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receivevideo',
            name='video',
            field=models.FileField(upload_to='video/', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mkv'], "Try Uploading 'mp4' or 'mkv' files"), uploadVideo.custom_validations.file_size_validation, uploadVideo.custom_validations.file_length_validation]),
        ),
        migrations.AlterField(
            model_name='videodetails',
            name='size',
            field=models.CharField(max_length=120, null=True),
        ),
    ]