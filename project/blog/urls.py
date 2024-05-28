
from django.contrib import admin
from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('page/', views.page, name="page"),
]

