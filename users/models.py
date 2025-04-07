from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="user-profile/%Y-%m-%d")
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "user_profiles"
