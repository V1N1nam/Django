from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm as CustomAuthenticationForm
from .forms import UserRegistrationForm
from .models import Funcionario, Skill
from django.template.loader import render_to_string
from django.http import JsonResponse



def minha_view(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')  # Redirecione para uma URL válida
    else:
        form = CustomAuthenticationForm()
    return render(request, 'index.html', {'form': form})

def principal_view(request):
    return render(request, 'main.html')

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    print(funcionarios)
    return render(request, 'main.html', {'funcionarios': funcionarios})

def funcionario_detalhes(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'skills.html', {'funcionario': funcionario})

def add_skill(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    
    if request.method == 'POST':
        skill_name = request.POST.get('skill')
        
        if skill_name:
            # Obtém ou cria a skill
            skill, created = Skill.objects.get_or_create(nome=skill_name)
            
            # Adiciona a skill ao funcionário
            funcionario.skills.add(skill)
            
            # Verifica se a requisição é AJAX
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Renderiza a lista de skills para retorno via AJAX
                skills_html = render_to_string('skills_list.html', {'funcionario': funcionario})
                return JsonResponse({'skills_html': skills_html})
        
        # Redireciona para a página de detalhes do funcionário
        return redirect('funcionario_detail', funcionario_id=funcionario.id)

    # Caso a requisição não seja POST, retorna um redirecionamento padrão
    return redirect('funcionario_detail', funcionario_id=funcionario.id)

def remove_skill(request, funcionario_id, skill_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    skill = get_object_or_404(Skill, id=skill_id)
    
    if skill in funcionario.skills.all():
        funcionario.skills.remove(skill)
        funcionario.save()  # Salva as alterações no banco de dados
        
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Renderiza a lista de skills para retorno via AJAX
        skills_html = render_to_string('skills_list.html', {'funcionario': funcionario})
        return JsonResponse({'skills_html': skills_html})

    # Redireciona para a página de detalhes do funcionário
    return redirect('funcionario_detail', funcionario_id=funcionario.id)

def relatorio_dinamico(request):
    # Filtros
    cargo = request.GET.get('cargo')
    skill = request.GET.get('skill')

    funcionarios = Funcionario.objects.all()

    if cargo:
        funcionarios = funcionarios.filter(cargo=cargo)
    if skill:
        funcionarios = funcionarios.filter(skills__nome=skill)

    context = {
        'funcionarios': funcionarios,
        'cargos': Funcionario.objects.values_list('cargo', flat=True).distinct(),
        'skills': Skill.objects.all(),
    }

    return render(request, 'relatorio.html', context)
