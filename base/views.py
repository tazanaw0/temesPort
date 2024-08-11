from django.shortcuts import render
from .models import Photo
# Create your views here. 
# created a function name home that will render my home.html file when app is requested.
def home (request):
    context = { #context variables created for use in our html template files
        'tumblr_url': 'https://madvillainn.tumblr.com',
        'github_url': 'https://github.com/tazanaw0',
        'insta_url': 'https://instagram.com/madvillaiinn',
    }
    return render(request, 'home.html', context)
#Album of candid photos 
def portraits(request):
    photos = Photo.objects.filter(category='portrait') #variable defined to fetch and filter (object.filter() method) photos based on their category 
    return render(request, 'portraitPhotography.html', {'photos': photos})

#Album of landscape photos
def landscape(request):
    photos = Photo.objects.filter(category='landscape')
    return render(request, 'landscapePhotography.html', {'photos': photos})

#Album of street photos
def street (request):
    photos = Photo.objects.filter(category='street')
    return render(request, 'streetPhotography.html', {'photos':photos})

#def socials (request):
    #context = {
    #    'tumblr_url': 'https://madvillainn.tumblr.com',
     #   'github_url' : 'https://github.com/tazanaw0'
   # }
   # return render(request, 'home.html', context)