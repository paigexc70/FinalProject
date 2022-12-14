from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def fpost(request):
    return render (request, 'fpost.html', {})

def fdetail(request):
    return render (request, 'fdetail.html', {})


    