from django.db import models

# Create your models here.
class OnlineStoreUsers(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    identification_number = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)