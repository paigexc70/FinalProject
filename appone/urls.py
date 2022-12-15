from django.urls import path
#from . import views
from .views import MainView, DetailView


urlpatterns = [
    #path('', views.index, name="home"),
    #path('fpost/', views.fpost, name="fpost"),
    path('', MainView.as_view(), name="main"),
    path('article/<int:pk>', DetailView.as_view(), name='fpost'),
 
  
]