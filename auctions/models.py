from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=1000)
    current_bid = models.PositiveIntegerField()
    image_url = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_user")
    isactive = models.BooleanField(default=True)

    def __repr__(self) -> str:
        return self.title

class Bid(models.Model):
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")

class Comment(models.Model):
    # should this also be cascade?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=512)

class Category(models.Model):
    pass