from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    dob = models.DateTimeField()
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.first_name
