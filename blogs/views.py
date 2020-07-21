from django.shortcuts import render
from .models import post
#from django.http import HttpResponse
posts = [
	{
		'author' : 'NileshN',
		'content' : 'How tech works',
		'title' : 'tech',
		'date_published' : '10 july'
	},
	{
		'author' : 'NileshNN',
		'content' : 'How tech goes wrong',
		'title' : 'tech_2',
		'date_published' : '9 july'
	}
]
# Create your views here.
def home(request):
	context = {
	'posts' : post.objects.all()
	}
	return render(request, 'blogs/home.html',context)
	
    

def about(request):
	return render(request,'blogs/about.html',{'title' : 'About'})