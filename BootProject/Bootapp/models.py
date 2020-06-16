from django.db import models


# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    address = models.CharField(max_length=30)


