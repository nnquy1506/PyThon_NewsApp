from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
 # Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=500)
   link = models.CharField(max_length=100)
   def __str__(self):
     return self.name

class News(models.Model):
   title = models.CharField(max_length=500)
   description = models.CharField(max_length=500)
   content = RichTextUploadingField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   picture = models.CharField(max_length=255)
   date = models.DateTimeField(auto_now_add=True)
   breaking = models.CharField(max_length=20)
   featured = models.CharField(max_length=20)
   def __str__(self):
     return self.title