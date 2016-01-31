from django.contrib.auth.models import AbstractUser, User
from django.db import models


class UserProfile(AbstractUser):
	pass
    #someAdditionalVar = models.BooleanField(default=False)
