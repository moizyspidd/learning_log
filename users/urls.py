from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Страница входа
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #страница выхода
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #страница регистрации
    path('register/', views.register, name='register'),


]
