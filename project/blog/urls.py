
from django.contrib import admin
from django.urls import path
from blog import views
from site_setup.views import site_config

app_name = 'blog'

urlpatterns = [

    path('', views.index, name="index"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),

    path('site_config', site_config, name="site_config"),

    path('users/', views.users_views, name="users"),
    path('create_user/', views.create_user, name="create_user"),
    path('edit_user/<int:user_id>/', views.edit_user, name="edit_user"),
    path('change_password/<int:user_id>/', views.change_password, name="change_password"),
    path('user_active/<int:user_id>/', views.user_active, name="user_active"),
    path('user_staff/<int:user_id>/', views.user_staff, name="user_staff"),
    path('delete_user/<int:user_id>/', views.delete_user, name="delete_user"),

    path('news/', views.news, name="news"),
    path('new/<slug:slug>/', views.new, name="new"),
    path('add_news/', views.add_news, name="add_news"),
    path('edit_news/<int:id>/', views.edit_news, name="edit_news"),
    path('delete_news/<int:id>/', views.delete_news, name="delete_news"), # type: ignore
    path('delete_image_news/<int:id>/', views.delete_image_news, name="delete_image_news"),
    path('news_published/<int:id>/', views.news_published, name="news_published"),

    path('events/', views.events, name='events'),
    path('event/<slug:slug>/', views.event, name="event"),
    path('add_event/', views.add_event, name="add_event"),
    path('edit_event/<int:id>/', views.edit_event, name="edit_event"),
    path('delete_event/<int:id>/', views.delete_event, name="delete_event"),
    path('delete_image_event/<int:id>/', views.delete_image_event, name="delete_image_event"),
    path('event_published/<int:id>/', views.event_published, name="event_published"),

    path('page/<slug:slug>/', views.page, name="page"),

    path('search/', views.search, name='search'),

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    
    path('post/<slug:slug>/', views.post, name="post"), 
    path('category/<slug:slug>/', views.category, name="category"),
    path('tag/<slug:slug>/', views.tag, name="tag"),
    path('shops/', views.shops, name='shops'),
    # path('shops/', views.ShopsViews.as_view(), name='shops'),
    path('admin_shops/', views.admin_shops, name='admin_shops'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:id>/', views.edit_post, name="edit_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),
    path('delete_image_post/<int:id>/', views.delete_image_post, name="delete_image_post"),
    path('shop_published/<int:id>/', views.shop_published, name="shop_published"),
    path('new_category/', views.new_category, name='new_category'),
    path('new_tag/', views.new_tag, name='new_tag'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete_tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),

]

