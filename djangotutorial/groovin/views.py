from django.shortcuts import render
from .models import posts
from django.contrib.auth.models import User
from addComments.models import addingComments
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
    dict_list=[]
    for post in all_posts:
        cnt=addingComments.objects.filter(postId_id=post.id).count()
        dict_list.append({'comments':cnt,'all_post':post})
    return render(request,'index.html',{'posts_info':dict_list })

def about(request):
    userss=User.objects.get(id=1)
    print(userss.email)
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html') 

def postdetails(request,id):
    post_obj=posts.objects.get(id=id)
    all_comments=addingComments.objects.filter(postId_id=id)
    res=[]
    for comments in all_comments:
        user_pk=comments.userId_id
        user=User.objects.get(id=user_pk)
        dict={'first_name':user.first_name,'last_name':user.last_name,'comm':comments}
        res.append(dict)
    return render(request,'post-details.html',{'post_obj':post_obj,'comment_obj':res})            