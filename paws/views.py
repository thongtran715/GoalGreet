from django.shortcuts import render ,redirect
from django.template import loader
from django.contrib.auth.models import User
from . models import Paws, Follow_Up, Comments
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index(request):
    all_paws = Paws.objects.all()[:10]
    all_comments = Comments.objects.all()
    context = {
        'all_paws' : all_paws,
        'all_comments' : all_comments,
    } 
    return render(request,'paws/index.html',context)

def comment(request, paws_id):
    user = User.objects.get(username="thongtran")
    paws = Paws.objects.get(id=paws_id)
    comment = Comments(fromUserId=user, toPawsId = paws, comment_content=request.POST["comment"])
    comment.save()
    return HttpResponse('Saved it')
