
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para a administração do Django
    path('', views.minha_view, name='index'),  # Mapeia a URL raiz para a view minha_view
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),  # URL para login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL para logout
    path('register/', views.register, name='register'),  # URL para registro de novos usuários
    path('main/', views.lista_funcionarios, name='main'),  # Corrigido para lista_funcionarios
    path('adicionar_funcionario/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('remove_funcionario/<int:funcionario_id>/', views.remove_funcionario, name='remove_funcionario'),
    path('funcionario/<int:funcionario_id>/', views.funcionario_detalhes, name='funcionario_detail'),  # Corrigido para nome correto da URL)
    path('funcionario/<int:funcionario_id>/add_skill/', views.add_skill, name='add_skill'),  # Adiciona skill ao funcionário
    path('funcionario/<int:funcionario_id>/remove_skill/<int:skill_id>/', views.remove_skill, name='remove_skill'),
    path('relatorio/', views.relatorio_dinamico, name='relatorio_dinamico'),
    path('calendario/eventos/', views.calendario_eventos, name='calendario_eventos'),
    path('calendario/', views.calendarioView, name='calendario'),
    path('calendario/adicionar/', views.adicionar_item_view, name='adicionar_item'),
    path('calendario/deletar/<int:evento_id>/', views.deletar_evento, name='deletar_evento'),
]
