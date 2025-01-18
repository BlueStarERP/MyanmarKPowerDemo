from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
#Shop View
    path('shopview1/', views.shopview1, name='shopview1'),
    path('shopview2/', views.shopview2, name='shopview2'),
    path('login/',views.loginpage, name='login'),
    # path('logout/', views.logoutuser, name='logoutuser'),

    path('', views.home, name='home'),
    path('create_item/', views.create_item, name='create_item'),
    path('category_list/', views.category_list, name='category_list'),
    path('item_details/1/', views.item_details, name='item_details'),


]