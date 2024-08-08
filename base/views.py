from django.shortcuts import render
# Create your views here. 
# created a function name home that will render my home.html file when app is requested.
def home (request):
    context = { #context variables created for use in our html template files
        'tumblr_url': 'https://madvillainn.tumblr.com',
        'github_url': 'https://github.com/tazanaw0',
        'insta_url': 'https://instagram.com/madvillaiinn',
    }
    return render(request, 'home.html', context)
def candid(request):
    return render(request, 'candidPhotography.html')

def landscape(request):
    return render(request, 'landscapePhotography.html')

def street (request):
    return render(request, 'streetPhotography.html')

#def socials (request):
    #context = {
    #    'tumblr_url': 'https://madvillainn.tumblr.com',
     #   'github_url' : 'https://github.com/tazanaw0'
   # }
   # return render(request, 'home.html', context)