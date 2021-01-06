from django.db import models

 # Create your models here.

class Category(models.Model):
   name = models.CharField(max_length=500)
   link = models.CharField(max_length=100)
   def __str__(self):
     return self.name

class News(models.Model):
   title = models.CharField(max_length=500)
   description = models.CharField(max_length=500)
   content = models.TextField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   picture = models.CharField(max_length=255)
   date = models.DateTimeField(auto_now_add=True)
   def __str__(self):
     return self.title