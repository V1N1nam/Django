from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm as CustomAuthenticationForm
from .forms import UserRegistrationForm
from .models import Funcionario, Skill, CalendarioItem, Funcionario
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import CalendarioItemForm
from django.contrib.auth.decorators import login_required
from .forms import FuncionarioForm
import io
from django.http import FileResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Funcionario, Skill
from django.http import FileResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect

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

@login_required(login_url='login')
def principal_view(request):
    return render(request, 'main.html')

@login_required(login_url='login')
def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    print(funcionarios)
    return render(request, 'main.html', {'funcionarios': funcionarios})

@login_required(login_url='login')
def funcionario_detalhes(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)
    return render(request, 'skills.html', {'funcionario': funcionario})

@login_required(login_url='login')
def adicionar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        
    else:
        form = FuncionarioForm()

    return render(request, 'adicionar_funcionario.html', {'form': form})

@login_required(login_url='login')
def remove_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, id=funcionario_id)

    if request.method == 'POST':
        funcionario.delete()
        return redirect('main')

    return redirect('main')

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def calendario_eventos(request):
    eventos = CalendarioItem.objects.all()
    eventos_lista = []

    for evento in eventos:
        eventos_lista.append({
            'id': evento.id,  # Adicionado para garantir que o ID esteja disponível
            'title': evento.titulo,
            'start': evento.data_inicio.isoformat(),
            'end': evento.data_fim.isoformat() if evento.data_fim else evento.data_inicio.isoformat(),
            'description': evento.descricao,
        })

    return JsonResponse(eventos_lista, safe=False)

@login_required(login_url='login')
def calendarioView(request):
    items = CalendarioItem.objects.all().order_by('data_inicio')
    return render(request, 'calendario.html', {'items': items})

@login_required(login_url='login')
def adicionar_item_view(request):
    if request.method == 'POST':
        form = CalendarioItemForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo item no banco de dados
            return redirect('calendario')  # Redireciona para a página do calendário após salvar
    else:
        form = CalendarioItemForm()
    
    return render(request, 'adicionar_item.html', {'form': form})

@login_required(login_url='login')
def deletar_evento(request, evento_id):
    if request.method == 'POST':
        evento = get_object_or_404(CalendarioItem, id=evento_id)
        evento.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required(login_url='login')
def gerar_relatorio_pdf(request):
    try:
        # Obtenha os dados do relatório
        funcionarios = Funcionario.objects.all()  # Ou aplique os filtros desejados

        # Renderize o novo template somente com a tabela
        template = get_template('relatorio_pdf.html')  # Nome do novo template
        html = template.render({'funcionarios': funcionarios})

        # Converta o HTML para PDF
        result = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

        if pdf.err:
            return HttpResponse("Erro ao gerar o PDF", status=500)

        result.seek(0)
        return FileResponse(result, content_type='application/pdf')
    
    except Exception as e:
        return HttpResponse(f"Erro na geração do PDF: {str(e)}", status=500)