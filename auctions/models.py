from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    current_bid = models.IntegerField()
    image = models.CharField(max_length=64)

class bid():
    pass