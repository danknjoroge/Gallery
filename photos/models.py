from pickle import FALSE
from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=71)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=71)


class Image(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to = 'photos/', null=FALSE, blank=FALSE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)






