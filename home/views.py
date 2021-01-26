from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
#htmlpages
def home(request):
    allposts=Post.objects.all()
    context={'allposts':allposts}
    
    
    
    return render(request,'home/home.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please fill the form properly!")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your message has been sent successfully!!")

        
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none()
    else:
        allpoststitle = Post.objects.filter(title__icontains=query)
        allpostscontent = Post.objects.filter(content__icontains=query)
        allpostsauthor = Post.objects.filter(author__icontains=query)
        allposts =  allpoststitle .union(allpostscontent,allpostsauthor)
    if allposts.count() == 0:
         messages.warning(request,"No search results found,please refine your query!")
    params = {'allposts':allposts,'query':query}
    return render(request,'home/search.html',params)
#authentication Apis
def handlesignup(request):
    if request.method =='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errors in input
        if len(username)> 10:
            messages.error(request,"username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"username should contain only letters and numbers!")
            return redirect('home')
        if pass1 != pass2 :
            messages.error(request,"password does not match")
            return redirect('home')


        myuser = User.objects.create_user(username, email ,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been created successfuly!")
        return redirect('home')
        


    else:
        return HttpResponse('404 - not found')


def handlelogin(request):
    if request.method =='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"logged in successfuly")
            return redirect('home')
        else:
            messages.error(request,"invalid credentials,please try again")
            return redirect('home')
    return HttpResponse('404-notfound')

    
def handlelogout(request):
    logout(request)
    messages.success(request,"logged out successfuly")
    return redirect('home')
    