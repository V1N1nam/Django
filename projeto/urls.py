from django.contrib import admin
from django.urls import path
from app import views  # Importar as views do aplicativo
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para a administração do Django
    path('', views.minha_view, name='index'),  # Mapeia a URL raiz para a view minha_view
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # URL para login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL para logout
    path('register/', views.register, name='register'),  # URL para registro de novos usuários
    path('principal/', views.principal_view, name='principal'),
]
