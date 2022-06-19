from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    Text = models.TextField(max_length=500)

class Author(models.Model):
    author =models.ForeignKey(Post, on_delete=models.CASCADE)
    Created_date =models.DateTimeField()
    Publised_date =models.DateTimeField()