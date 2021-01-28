from django.contrib import admin
from django.urls import path
from ebook import views


urlpatterns = [
    path("", views.index, name='ebook'),
    path("about", views.about, name= 'about'),
    path("services", views.services, name= 'services'),
    path("contact", views.contact, name= 'contact'),
]