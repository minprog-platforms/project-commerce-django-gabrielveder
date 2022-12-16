from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bid(models.Model):
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Listing(models.Model):

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=500)
    current_bid = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True)
    image_url = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    isactive = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=512)

    def __str__(self):
        return self.text