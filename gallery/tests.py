from django.test import TestCase
from .models import Category,location,Image
import datetime as dt

# Create your tests here.


#location class method tests
class locationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kenya= location(name = 'Kenya')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,location))

    # Testing Save Method
    def test_save_method(self):
        self.kenya.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations) > 0)  

#Category class method tests
class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.nature= Category(name = 'Nature')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nature,Category))

    # Testing Save Method
    def test_save_category(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)  

#Image class method tests     
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):

        # Creating a new location and saving it
        self.kenya= location(name="Kenya")
        self.kenya.save_location()

        # Creating a new category and saving it
        self.nature= Category(name="Nature")
        self.nature.save_category()


        self.img1= Image(   image="testImage",
                            name="img1",
                            url="Testurl",
                            description="This is a test",
                            location=self.kenya
                        )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.img1,Image))

    # Testing Save Method
    def test_save_method(self):
        self.img1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)  

    # Testing delete Method
    def test_delete_method(self):
        self.img1.save_image()
        self.img1.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)      
        
         