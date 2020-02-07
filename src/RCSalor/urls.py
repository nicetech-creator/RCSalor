from django.contrib import admin
from django.urls import path
from . import views

app_name = 'RCSalor'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('business', views.business_detail, name = 'business_detail'),
]
