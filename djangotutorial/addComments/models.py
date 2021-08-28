from django.db.models.deletion import CASCADE
from groovin.models import posts
from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.

class addingComments(models.Model):
    comment=models.TextField()
    time=models.DateField()
    postId=models.ForeignKey(posts,on_delete=CASCADE)
    userId=models.ForeignKey(User,on_delete=CASCADE)
