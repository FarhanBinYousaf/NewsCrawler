from django.db import models
from django.utils import timezone
# Create your models here.

class News(models.Model):
    heading = models.CharField(max_length=200)
    link  = models.CharField(max_length=300, null=True, blank=True)
    date = models.CharField(max_length=100)

    # def __str__(self):
    #     return str(self.heading)