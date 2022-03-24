from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTest(TestCase):

    def setUp(self):
        self.nairobi = Location(location='Nairobi')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_location(self):
        self.nairobi.save_location()
        location= Location.objects.all()
        self.assertTrue(len(location)>0)

class CategoryTestCase(TestCase):
    
    def setUp(self):
        self.sports= Category(category = "Sports")
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sports,Category))
    
    def test_save_location(self):
        self.sports.save_category()
        category= Category.objects.all()
        self.assertTrue(len(category)>0)






