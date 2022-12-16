from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bid(models.Model):
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")

class Listing(models.Model):

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=500)
    current_bid = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True, related_name="lisitng_bid")
    image_url = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_user")
    isactive = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auther_comment")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comment")
    text = models.CharField(max_length=512)

    def __str__(self):
        return self.text