from django.urls import path
from . import views #from this folder (base) import all the views

urlpatterns =[
    path('', views.home, name='home'),
    path('iPhone/', views.iPhone, name='iPhone'),
    path('Portraits/', views.portraits, name='portraits'),
    path('landscapePhotography/', views.landscape, name='landscape'),
    path('streetPhotography/', views.street, name='street'),
    #path('socials/', views.socials, name='socials'),
] 
