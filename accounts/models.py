from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addresss = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)