from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Sound_Video(models.Model):
    video_upload_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=200)
    video_timestamp = models.DateTimeField(auto_now=True)
    video_upload = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.video_title + ": " + str(self.video_upload)

class Sound_Audio(models.Model):
    audio_upload_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    audio_title = models.CharField(max_length=200)
    audio_timestamp = models.DateTimeField(auto_now=True)
    audio_upload = models.FileField(upload_to='audio/', null=True, verbose_name="")

    def __str__(self):
        return self.audio_title + ": " + str(self.audio_upload)