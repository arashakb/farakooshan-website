from django.db import models
from django.core.validators import FileExtensionValidator 
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    
    # image
    def __str__(self):
        return self.name
    
class Course(models.Model):
    image = models.ImageField(upload_to='course/', default='course/default.jpg')
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    video = models.FileField(upload_to='course/',null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    # tag 
    category = models.ManyToManyField(Category)
    # post
    content = models.TextField()
    description = models.TextField()
    objectives = models.TextField()
    whoshouldattend = models.TextField()
    cpdunit = models.TextField()
    location = models.CharField(max_length=255)

    status = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return "{} - {}".format(self.title, self.id)