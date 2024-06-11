
from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [

    path('', views.index, name="index"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('users/', views.users_views, name="users"),

    path('news/', views.news, name="news"),
    path('events/', views.events, name='events'),

    path('post/<slug:slug>/', views.post, name="post"),
    path('page/<slug:slug>/', views.page, name="page"),
    path('event/<slug:slug>/', views.event, name="event"),
    path('new/<slug:slug>/', views.new, name="new"),
    path('category/<slug:slug>/', views.category, name="category"),
    path('tag/<slug:slug>/', views.tag, name="tag"),


    path('shops/', views.shops, name='shops'),
    # path('shops/', views.ShopsViews.as_view(), name='shops'),
    path('admin_shops/', views.admin_shops, name='admin_shops'),
    path('search/', views.search, name='search'),

    path('create_user/', views.create_user, name="create_user"),
    path('edit_user/<int:user_id>/', views.edit_user, name="edit_user"),
    path('change_password/<int:user_id>/', views.change_password, name="change_password"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('new_post', views.new_post, name='new_post'),

]

