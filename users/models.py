import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

class UserQuerySet(models.query.QuerySet):

    def get_count(self):
        return self.count()

    def get_today_user_count(self):
        return self.exclude(date_joined__lt=datetime.date.today()).count()


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
    nickname = models.CharField(blank=True, null=True, max_length=20)
    avatar = models.FileField(upload_to='avatar/')
    mobile = models.CharField(blank=True, null=True, max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True, null=True)
    subscribe = models.BooleanField(default=False)
    objects = UserQuerySet.as_manager()

    class Meta:
        db_table = "v_user"


class Feedback(models.Model):
    contact = models.CharField(blank=True, null=True, max_length=20)
    content = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        db_table = "v_feedback"