
from django.contrib import admin
from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<int:id>/', views.post_view, name="post_view")
]

