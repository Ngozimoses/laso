from django.db import models

class Newblog(models.Model):
    name = models.CharField(max_length=200)
    blog = models.TextField(null=True, blank=True)
    blogTitle = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # Specify a folder for uploaded images
    blogimage = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def __str__(self):
        return self.name
