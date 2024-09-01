from django.db import models

class Skill(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    skills = models.ManyToManyField(Skill, blank=True)  # Relacionamento ManyToMany com Skill

    def __str__(self):
        return self.nome
