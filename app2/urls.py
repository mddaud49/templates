from django.urls import path,include
from . import views

urlpatterns = [
    path('contact/',views.Contact,name='contact'),
    path('shop/',views.Shop,name='shop'),

]