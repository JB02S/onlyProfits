from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Market(models.Model):
    ticker = models.CharField(max_length=10)
    values = models.JSONField()
    # volume = models.IntegerField()

    def __str__(self):
        return self.ticker

class OnlyProfitsUser(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_markets = models.JSONField()
