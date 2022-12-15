from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

#def index(request):
   # return render(request, 'index.html', {})

#def fpost(request):
   # return render (request, 'fpost.html', {})


class MainView(ListView):
    model = Post
    template_name = 'index.html'
    
class DetailView(DetailView):
    model = Post
    template_name = 'fpost.html'

class AddPostView(CreateView):
   model = Post
   template_name = 'addpost.html'
   fields = '__all__'