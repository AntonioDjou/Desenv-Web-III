"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for django_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  
from rest_framework import routers

from hello import views  

# Configuração do Roteador da API 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'jogadores', views.JogadorViewSet)

urlpatterns = [
    # --- Rotas Principais e da API ---
    path('admin/', admin.site.urls),  # Apenas uma vez
    path('', views.home, name='home'),
    path('ola/<str:name>/', views.hello2, name='hello2'),
    path('api/post_hello/', views.post_hello, name='post_hello'),
    path('inicial/', views.inicial, name='inicial'),
    path('problema/', views.problema, name='problema'),
    path('solucao/', views.solucao, name='solucao'),
    path('autor/', views.autor, name='autor'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('api/', include(router.urls)),  # Inclui as rotas da API

    # 1. Rota para login: /usuarios/login/
    path('usuarios/login/',
         auth_views.LoginView.as_view(template_name='usuarios/login.html'),
         name='login'),

    # 2. Rota para dashboard: /usuarios/dashboard/
    path('usuarios/dashboard/', views.dashboard, name='dashboard'),

    # 3. Rota para logout: /usuarios/logout/
    path('usuarios/logout/', auth_views.LogoutView.as_view(), name='logout'),
]