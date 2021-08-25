from django.db import models

# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.CharField(max_length=50)
    date = models.DateField()
    comments = models.IntegerField()
    img = models.ImageField(upload_to='pics')

