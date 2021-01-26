from django.urls import path
from . import views

urlpatterns = [
   #API to post a comment 
   path('postComment', views.postComment, name="postComment"),
   path('', views.bloghome, name='bloghome'),
   path('<str:slug>', views.blogpost, name='blogpost'),
   
   
  
   

]