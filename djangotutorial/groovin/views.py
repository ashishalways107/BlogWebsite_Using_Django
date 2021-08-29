from django.shortcuts import redirect, render
from .models import posts
from django.contrib.auth.models import User
from datetime import date
from addComments.models import addingComments
# Create your views here.

def index(request):
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
    if request.method=="POST":
        message=request.POST['message']
        newComment=addingComments(comment=message,time=date.today())
        newComment.postId=post_obj
        newComment.userId=User.objects.get(id=request.user.id)
        newComment.save()
    
    all_comments=addingComments.objects.filter(postId_id=id)
    res=[]
    for comments in all_comments:
        user_pk=comments.userId_id
        user=User.objects.get(id=user_pk)
        dict={'first_name':user.first_name,'last_name':user.last_name,'comm':comments}
        res.append(dict)
            
    cnt=addingComments.objects.filter(postId_id=id).count()

    return render(request,'post-details.html',{'post_obj':post_obj,'comment_obj':res,'comments':cnt})            

def delete(request,id):
    posts.objects.filter(id=id).delete()
    return redirect('/')    