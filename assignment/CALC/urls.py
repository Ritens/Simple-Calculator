from django.urls import path
from .views import *

#base url=http://127.0.0.1:8000/calculator/

urlpatterns = [
    path('home/',view_calc),
]
