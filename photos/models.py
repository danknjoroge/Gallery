from pickle import FALSE
from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to = 'gallery/', null=FALSE, blank=FALSE)

