from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Profile(models.Model):
    display_name = models.CharField(max_length=200)
    bio = models.TextField()
    previous_role = models.CharField(max_length=200)
    current_role = models.CharField(max_length=200)
    profile_image = models.URLField()
    birthdate = models.DateField()
    pronouns = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    ethnicity = models.CharField(max_length=200)
    linkedin_url = models.URLField()
    github_url = models.URLField()
    is_visible = models.BooleanField()
    is_public = models.BooleanField()
    allow_contact = models.BooleanField()
    challenge = models.TextField()
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    description = models.TextField()
    url = models.URLField()
    profile = models.ForeignKey(
        'profile',
        on_delete=models.CASCADE,
        related_name='project'
    )
    






