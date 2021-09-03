from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    context = {
        'heading' : 'My first Blog!',
        'services' : ["Future Fridays", "Mondays with You", "Oh the wekend"],
        'posts' : ["Big Blue world", "Out of space", "A-O A-Okay"],
    }

    return render(request,"home.html", context )

def contact(request):

    context = {
        'number' : '0707320000',
        'email' : 'briangachiri@gmail.com',
        'address': 'somewhere',
        'services' : ["Future Fridays", "Mondays with You", "Oh the weekend"],

    }

    return render(request,"contact.html", context )

def blog(request):

    context = {
        'posts' : ["Big Blue world", "Out of space", "A-O A-Okay", "I am number 4", "Worcesteshire Alley", "Salt & Sugar"],

    }

    return render(request,"blog/blog.html", context )