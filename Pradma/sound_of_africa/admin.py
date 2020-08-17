from django.contrib import admin
from .models import Sound_Audio, Sound_Video

# Register your models here.
class PradmaVideoAdmin(admin.ModelAdmin):
    list_display = ['video_upload_by', 'video_title','video_upload', 'video_timestamp',]

class PradmaAudioAdmin(admin.ModelAdmin):
    list_display = ['audio_upload_by', 'audio_title','audio_upload', 'audio_timestamp',]

admin.site.register(Sound_Video, PradmaVideoAdmin)
admin.site.register(Sound_Audio, PradmaAudioAdmin)