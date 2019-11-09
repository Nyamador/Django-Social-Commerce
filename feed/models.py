from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import Profile
from .managers import ActivityManager


class Activity(models.Model):
  actor = models.ForeignKey(Profile, on_delete=models.CASCADE)
  comment = models.CharField("Comment", max_length=700)
  date_posted = models.DateField(default=timezone.now, editable=False)

  def __str__(self):
    return f'{self.actor} , {self.id}'
  
  objects = ActivityManager()


class ActivityMedia(models.Model):
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  media = models.FileField(upload_to='videos/uploads/%Y/%m/%d/')

  def __str__(self):
    return self.id

class Reaction(models.Model):
  actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  kind = models.CharField(max_length=20, null=False, blank=False)
  post = models.ForeignKey(Activity, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.id


# class NotificationFeed(models.Model):
#   author = models.CharField("Created By", max_length=50, null=Flase, blank=False)
#   verb = models.CharField("Verb", max_length=10, null=False, blank=False)

#   def __str__(self):
#     return f'{self.author} added a post'