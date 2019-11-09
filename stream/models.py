from django.db import models
from users.models import Profile


class Stream(models.Model):
  creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
  playback_id = models.CharField("Stream Playback id", max_length=100, blank=False, null=False)
  views = models.PositiveIntegerField("Stream Views", default=0)

  def __str__(self):
    return f'{self.creator} : {self.playback_id}'