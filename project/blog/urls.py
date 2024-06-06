
from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<slug:slug>/', views.post, name="post"),
    path('page/<slug:slug>/', views.page, name="page"),
    path('event/<slug:slug>/', views.event, name="event"),
    path('new/<slug:slug>/', views.new, name="new"),
    path('category/<slug:slug>/', views.category, name="category"),
    path('tag/<slug:slug>/', views.tag, name="tag"),
    path('shops/', views.shops, name='shops'),
    path('search/', views.search, name='search'),
]

