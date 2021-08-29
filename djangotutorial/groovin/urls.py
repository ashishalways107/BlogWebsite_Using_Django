from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('post-details/<int:id>',views.postdetails,name="postdetails")
    ]
