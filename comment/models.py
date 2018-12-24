from django.db import models
from django.conf import settings
from video.models import Video
# Create your models here.

class Comment(models.Model):
    list_display = ("content","timestamp",)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30,blank=True, null=True)
    avatar = models.CharField(max_length=100,blank=True, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "v_comment"