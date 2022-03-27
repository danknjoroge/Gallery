from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTest(TestCase):
    '''method to create instance before each test is run '''

    def setUp(self):
        self.nairobi = Location(location='Nairobi')
    '''Testing  instance'''
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_location(self):
        self.nairobi.save_location()
        location= Location.objects.all()
        self.assertTrue(len(location)>0)

class CategoryTestCase(TestCase):
    '''method to create instance before each test is run '''
    def setUp(self):
        self.sports= Category(category = "Sports")
        
    '''Testing  instance'''
    def test_instance(self):
        self.assertTrue(isinstance(self.sports,Category))
    
    def test_save_location(self):
        self.sports.save_category()
        category= Category.objects.all()
        self.assertTrue(len(category)>0)


class TestImage(TestCase):


    def setUp(self):
        '''create location and save '''
        self.nairobi= Location(name="Nairobi")
        self.nairobi.save_location()

        '''create category and save'''
        self.sports= Category(name="Sports")
        self.sports.save_category()

        self.new_image= Image(name="Curly", description="An amazing picture", image="Add image", location=self.nairobi, category= self.sports )
        self.new_image.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_delete_image(self):
        self.new_image= Image(name="Curly", description="An amazing picture", image="Add image", location=self.nairobi, category= self.sports )
        self.new_image.save_image()
        self.new_image.delete_image()
        





