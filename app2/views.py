from django.shortcuts import render

# Create your views here.

def Contact(request):
    return render(request, 'contact.html',)

def Shop(request):
    return render(request, 'shop.html',)