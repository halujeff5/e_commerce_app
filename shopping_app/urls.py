"""shopping_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from .views import blazers, sweaters, t_shirts, shirts 
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    # path("hello/", views.hello_geek)
    path("blazers", views.blazer, name='blazers'),
    path("shirts", views.shirt, name='shirts'),
    path("t_shirts", views.t_shirt, name='t_shirts'),
    path("sweaters", views.sweater, name='sweaters'),
    path("checkout", views.checkout, name='checkout'),
    path("upload", views.upload, name='upload'),


]
