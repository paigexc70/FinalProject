from django.urls import path
from .views import index, fpost, fdetail

urlpatterns = [
    path('', index, name="home"),
    path('fpost/', fpost, name="fpost"),
    path('fdetail/', fdetail, name="fdetail"),
 
  
]