from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm


class MainView(ListView):
    model = Post
    template_name = 'index.html'
    
    
class DetailView(DetailView):
    model = Post
    template_name = 'fpost.html'

class AddPostView(CreateView):
   model = Post
   form_class = PostForm
   template_name = 'addpost.html'
   #fields = '__all__'

class UpdateView(UpdateView):
   model = Post
   form_class = EditForm
   template_name = 'updatepost.html'
   #fields = ['title', 'body']

class DeleteView(DeleteView):
   model = Post
   form_class = EditForm
   template_name = 'deletepost.html'
   


