import os
import django
import json
from app.models import Funcionario

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

def importar_funcionarios():
    try:
        with open('funcionarios.json') as f:
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