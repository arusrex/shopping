
from django.contrib import admin
from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('page/', views.page, name="page"),
    path('event/<slug:slug>/', views.event, name="event"),
    path('new/<slug:slug>/', views.new, name="new"),
]

