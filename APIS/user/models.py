from django.db import models

# Create your models here.
class ModelUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    registration_date = models.DateTimeField(auto_now_add=True)
    ID = models.PositiveIntegerField() 

    def __str__(self):
        return self.first_name, self.last_name, self.username, self.email