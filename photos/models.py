from pickle import FALSE, TRUE
from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=71, blank=TRUE, default=None)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=71, null=TRUE, default=None)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.category

class Image(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    image_pic = models.ImageField(upload_to = 'pics/', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=TRUE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=TRUE)
    

    # @classmethod
    # def search_by_name(cls, name):
    #     image= cls.objects.filter(name__icontains=name)
    #     return image

    @classmethod
    def search_by_category(cls, category):
        image= cls.objects.filter(category__category__icontains=category)
        return image

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)








