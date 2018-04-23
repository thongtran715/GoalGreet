from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login , logout as auth_logout , authenticate
from . models import Paws, Follow_Up, Comments
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from paws.forms import SignUpForm

# Create your views here.
def index(request):
    if request.user.is_authenticated: 
        username = request.user.username
        user = User.objects.get(username=username)
        all_paws = Paws.objects.filter(~Q(fromUserId = user))
        all_comments = Comments.objects.all()
       
    else:
        all_paws = Paws.objects.all()
        all_comments = Comments.objects.all()
    context = {
        'all_paws': all_paws,
        'all_comments': all_comments,
    }
    return render(request,'paws/index.html', context)

def comment(request, paws_id):
    if request.user.is_authenticated:
        paws = Paws.objects.get(id=paws_id)
        if request.POST.get("comment_btn"):
            username = request.user.username
            user = User.objects.get(username=username)
            comment = Comments(fromUserId=user, toPawsId = paws, comment_content=request.POST["comment"])
            if comment.comment_content != '':
                comment.save()
            return redirect('/')
        elif request.POST.get("like_btn"):
            paws.number_of_likes += 1
            paws.save()
            return redirect('/')
        else:
            # This is a follow happens
            username = request.user.username
            user = User.objects.get(username=username)
            follow = Follow_Up(fromUserId= user , toPawsId= paws)
            follow.save()
            return redirect('/')
    else:
        return redirect('/', "")
            
def logout_view (request):
     auth_logout(request) 
     return redirect("/")
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password = password)
        if user is not None:
            auth_login(request,user)
            return redirect("/")
    else:
        return render(request,'paws/login.html')
def writePaws (request):
    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.user.username
            user = User.objects.get(username=username)
            title = request.POST["paws_title"]
            content = request.POST.get("paws_content", "")
            a_paw = Paws(fromUserId = user, title=title, content=content) 
            if title != "" and content != "":
                a_paw.save()
            return redirect('/')
        else:
            return render(request,'paws/writePaws.html')
    else:
        return render(request,'paws/login.html')
def yourPaws(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username) 
        paws = Paws.objects.filter(fromUserId = user)
        comments = Comments.objects.all()
        context = {
            "paws":paws,
            "comments":comments
        }
        return render(request, "paws/yourPaws.html",context)
    else:
        return HttpResponse("GO LOG IN ")

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request,user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request,'paws/register.html', {'form': form}) 

def follow_Up_View (request):
    return HttpResponse("Follow")