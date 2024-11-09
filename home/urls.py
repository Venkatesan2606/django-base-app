from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name ="index"),
    path('signUp',views.signUp,name="signUp"),
    path('login',views.login,name="login"),
    path('dashboard', views.dashboard, name="dashboard"), 
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]
