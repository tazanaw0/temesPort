from django.urls import path
from . import views #from this folder (base) import all the views

urlpatterns =[
    path('', views.home, name='home')
    #path('socials/', views.socials, name='socials'),
]
 