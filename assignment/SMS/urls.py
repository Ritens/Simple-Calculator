from django.urls import path,include
from .views import *


urlpatterns = [
    
   path('home/',Home),
   path('home/page2.html',page2),
   path('home/delete/<int:id>',delete),
   path('home/edit/<int:id>',edit),
   path('home/home.html',Home),
   
]
