from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
								  ListView,
								  DetailView, 
								  CreateView,
								  UpdateView,
								  DeleteView
								  )
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
	
class PostListView(ListView):
	model = post
	template_name = 'blogs/home.html'
	#<app>/<model>_<viewtype>.html needed
	context_object_name='posts'
	ordering = ['-date_published'] 	
    
class PostDetailView(DetailView):
	model = post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = post
	success_url = '/'

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request,'blogs/about.html',{'title' : 'About'})