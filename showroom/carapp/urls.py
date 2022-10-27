# from django.contrib import admin
from django.urls import path, include
from carapp import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index.html'),
    path('register/',views.register,name='register.html'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('home/',views.home,name='home.html'), 
    # path('logout/',views.logout,name='logout'),





    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change_password/', views.change_password, name='change_password'),
]