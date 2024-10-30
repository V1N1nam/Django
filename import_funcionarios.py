import os
import sys
import django
import json

# Adicione o caminho do diretório do projeto ao sys.path para garantir o acesso ao manage.py
sys.path.append("C:/Users/arauj/Desktop/VS_code/DjangoStuff/Django")  # Verifique se o caminho está correto

# Configuração para acessar o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()  # Inicializa o Django

def importar_funcionarios():
    # Importa o modelo após a configuração do Django
    from app.models import Funcionario
    
    try:
        with open('funcionarios.json', encoding='utf-8') as f:
            data = json.load(f)
            for entry in data:
                fields = entry['fields']
                Funcionario.objects.create(
                    nome=fields['nome'],
                    cargo=fields['cargo'],
                    data_nascimento=fields['data_nascimento']
                )
        print('Funcionários importados com sucesso!')
    
    except Exception as e:
        print('\nErro ao importar funcionários:', e)

if __name__ == '__main__':
    importar_funcionarios()
