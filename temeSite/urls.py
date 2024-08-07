"""
URL configuration for temeSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#webserver decides which webpages should be delivered to the user.single quotes with blank space denote our default path (home) and since we want our app to handle our home page we call for our apps url configuration file. 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))  #when the user is at our home page, django will refer to base.urls (our app urls config) to present content
]

