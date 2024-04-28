from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=600,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='post_images',null=True,blank=True)
    
    def __str__(self):
        return self.title
    

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    password = models.CharField(max_length=100, null=True, blank=True)
    frame = models.IntegerField(null=True)

    def __str__(self):
        return self.title
   