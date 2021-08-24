from django.shortcuts import render
from .models import posts
# Create your views here.

def index(request):

    # post1=posts()
    # post1.title="Fashion"
    # post1.desc="This is the First Post"
    # post1.user="Admin"
    # post1.date="May 12, 2020"
    # post1.comments=12
    # post1.img="banner-item-01.jpg"

    # post2=posts()
    # post2.title="Nature"
    # post2.desc="This is the Second Post"
    # post2.user="Admin"
    # post2.date="May 14, 2020"
    # post2.comments=24
    # post2.img="banner-item-02.jpg"

    # post3=posts()
    # post3.title="Lifestyle"
    # post3.desc="This is the Third Post"
    # post3.user="Admin"
    # post3.date="May 16, 2020"
    # post3.comments=36
    # post3.img="banner-item-03.jpg"

    # post4=posts()
    # post4.title="Sports"
    # post4.desc="This is the fourth Post"
    # post4.user="Admin"
    # post4.date="May 18, 2020"
    # post4.comments=48
    # post4.img="banner-item-04.jpg"

    # all_posts=[post1,post2,post3,post4]

    all_posts=posts.objects.all()
    return render(request,'index.html',{'posts': all_posts})

def about(request):
    return render(request,'about.html')    