from django.shortcuts import render
from django.views.generic import ListView, DetailView
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