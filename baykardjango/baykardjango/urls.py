"""
URL configuration for baykardjango project.

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
from django.urls import re_path as url
from rentiha import views

urlpatterns = [
    url(r'^ihaall$',views.ihaApi),
    url(r'^ihaall/([0-9]+)$', views.ihaApi),

    url(r'^user$',views.userlogin),
    url(r'^user/([0-9]+)$', views.userlogin),
    
    url(r'^ihainformation$',views.ihaApi2),
    url(r'^ihainformation/([0-9]+)$', views.ihaApi2),   
    
]
