from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    views = models.IntegerField(default=0,blank=True)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 100)
    message = models.TextField()
    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    slug = models.SlugField(max_length=200)
    image_url = models.ImageField()
    views = models.IntegerField(default=0,blank=True)
    keywords = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    likes = models.IntegerField(default=0, blank=True)
    dislikes = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

class Feedback(models.Model):
    message = models.TextField()
    name = models.CharField(max_length = 50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Seo(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.TextField()
    occasion = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
