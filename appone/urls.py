from django.urls import path
#from . import views
from .views import MainView, DetailView, AddPostView


urlpatterns = [
    #path('', views.index, name="home"),
    #path('fpost/', views.fpost, name="fpost"),
    path('', MainView.as_view(), name="main"),
    path('article/<int:pk>', DetailView.as_view(), name='fpost'),
    path('addpost/', AddPostView.as_view(), name='add_post'),
 
  
]