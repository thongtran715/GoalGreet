from django.shortcuts import render ,redirect
from django.template import loader
from . models import Paws, Follow_Up, Comments
from django.http import HttpResponse
# Create your views here.
def index(request):
    all_paws = Paws.objects.all()[:10]
    all_comments = Comments.objects.all()
    context = {
        'all_paws' : all_paws,
        'all_comments' : all_comments,
    } 
    return render(request,'paws/index.html',context)