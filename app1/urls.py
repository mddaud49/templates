from django.urls import path
from app1 import views

urlpatterns =[
    path('about/',views.About,name='about'),
]