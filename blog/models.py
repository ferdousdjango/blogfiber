from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=155)
    views= models.IntegerField(default=0)
    content = models.TextField()
    image=models.ImageField(upload_to='media',max_length=100,blank=True)
    author = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    timestamp=models.DateTimeField(blank=True)
    hometitle=models.CharField(max_length=155,blank=True)
    homeimage =models.ImageField(upload_to='media',max_length=100,blank=True)
    homecontent = models.TextField(blank=True)
    

    
    
    
    

    def __str__(self):
        return  self.title + ' by ' + ' '+ self.author

#this post will remain at the right side of the screen

    
class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)   
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username 

    

    
    
    


