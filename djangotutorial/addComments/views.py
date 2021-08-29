from groovin.models import posts
from addComments.models import addingComments
from django.shortcuts import redirect, render
from datetime import date
from django.contrib.auth.models import User
# Create your views here.
def comment(request,id):
    message=request.POST['message']
    print(message)
    newComment=addingComments(comment=message,time=date.today())
    post_obj=posts.objects.get(id=id)
    post_obj.save()
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
    # return render(request,'/',{'comment_obj':res})
    return redirect('/about')
    