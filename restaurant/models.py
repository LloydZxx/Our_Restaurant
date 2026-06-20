from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.
#hero section
class HeroSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = RichTextField()
    btn = models.CharField(max_length=50,default="Explore Our Menu")
    btnlink = models.UUIDField(null=True, blank=True)
    image = models.ImageField(upload_to='hero/')

    def str(self):
        return self.title

#today special
class SpecialHeader(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

    def str(self):
        return self.title

class SpecialItem(models.Model):
    tag = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu/')
    btn = models.CharField(max_length=50)
    btnlink = models.UUIDField(null=True, blank=True)

    def str(self):
        return self.title

#service section
class ServiceSection(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

    def str(self):
        return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

    def str(self):
        return self.title
    
#Customers favorites
class FavoriteHeader(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

    def str(self):
        return self.title

class FavItem(models.Model):
    tag = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu/')
    btn = models.CharField(max_length=50)
    btnlink = models.UUIDField(null=True, blank=True)
    def str(self):
        return self.title

#Menu
class Menu(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class LatestMenu(models.Model):
    tag = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu/')
    btn = models.CharField(max_length=50)
    btnlink = models.UUIDField(null=True, blank=True)
    def str(self):
        return self.title

#Feedback
class CustomerFeedback(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu/',blank=True,null=True)
    description = RichTextField()
    def __str__(self):
        return self.name

#Contact Us
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    subject = RichTextField()
    description = RichTextField()

    def __str__(self):
        return self.name
    
class Branches(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='contact/')

    def __str__(self):
        return self.title