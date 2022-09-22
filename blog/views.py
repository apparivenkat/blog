from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from blog.forms import LoginForm, SignupForm, PostForm
from blog.models import Blog
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    post = Blog.objects.all()
    return render(request, 'home.html', {'post':post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        post = Blog.objects.all()
        user = request.user
        full_name = user.get_full_name()
        grps = user.groups.all()
        return render(request, 'dashboard.html', {'post':post, 'full_name':full_name,'group':grps})
    else:
        return redirect('login')

def logoutpage(request):
    logout(request)
    return redirect('home')

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Success!!!!!!!!!!!!!!')
                    return redirect('dashboard')
        else:
            form= LoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        return redirect('dashboard')

def signup(request):    
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            messages.success(request, 'Congratulations!!!!!!!!!! Author Account Created')
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                obj = Blog(title=title, desc=desc)
                obj.save()
                form = PostForm()
                messages.success(request, 'New Blog Posted Successfully')
        else:
            form = PostForm()
        return render(request, 'addpost.html', {'form':form})
    else:
        return redirect('login')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Blog.objects.get(id=id)
            form = PostForm(instance=obj, data= request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Updated Successfully')
                return redirect('login')
        else:
            obj = Blog.objects.get(id=id)
            form = PostForm(instance=obj)
        return render(request, 'updatepost.html', {'form':form})
    else:
        return redirect('login')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            obj = Blog.objects.get(id=id)
            obj.delete()
            messages.success(request, "Post Deleted Successfully")
            return redirect('dashboard')
    else:
        return redirect('login')