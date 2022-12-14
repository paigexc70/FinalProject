from django.urls import path
from .views import index, fpost

urlpatterns = [
    path('', index, name="home"),
    path('fpost/', fpost, name="fpost"),
 
 
  
]