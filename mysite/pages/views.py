from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create  your views here.


def index(request):
	#return HttpResponse('Hello From Post')
	posts=Posts.objects.all()[:10]
	contexts = {
	       'title':'latest Posts',
	       'posts':posts

	}
	return render(request,'pages/index.html',contexts)

def details(request,id):
	post=Posts.objects.get(id=id)
	context = {
	        'post' : post

	}
	return render(request,'pages/details.html',context)
