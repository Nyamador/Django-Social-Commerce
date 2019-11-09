from django.db import models
from users.models import VelocityUser, Profile , Relationship
# from feed.models import Activity


class ActivityManager(models.Manager):
  # 1. Get's all the id's of the profiles a user is following
  # 2. 
  def get_user_timeline(self, user):
    """
    Returns a list of all posts from profiles followed by a user
    """
    user = VelocityUser.objects.get(id=user)
    profiles_user_follows = user.relationship_set.all().values()
    profile_ids = [ profile['target_id'] for profile in profiles_user_follows ]
    posts_list = []
    all_activities = self.all().values()
    timeline_data = [ posts_list.append(post) for post in all_activities if post['actor_id'] in profile_ids]
    return posts_list