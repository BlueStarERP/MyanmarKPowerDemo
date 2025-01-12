from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
    # path('login/', UserLoginView.as_view(), name = 'UserLoginView'),
    # path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    path('login/',views.loginpage, name='login'),
    # path('logout/', views.logoutuser, name='logoutuser'),
    # path('register/', views.registerpage, name='registerpage'),
    path('', views.home, name='home'),
    path('create_item/', views.create_item, name='create_item'),

]