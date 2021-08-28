from django.db import models

# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.CharField(max_length=50)
    date = models.DateField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title

