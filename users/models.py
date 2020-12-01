from django.db import models

# Create your models here.

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    class Meta:
        ordering = ['created']
