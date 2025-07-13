from django.contrib import admin
from django.urls import path, include
from portfolio import views
urlpatterns = [

    path('about', views.AboutPageView, name='about'),
    path('', views.HomePageView, name='home'),
    path('projects/', include('projects.urls')),

]
