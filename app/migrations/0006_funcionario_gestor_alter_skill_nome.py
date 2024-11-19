# Generated by Django 5.1 on 2024-11-19 19:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_funcionario_skills_skill_nivel_cargo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='gestor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='funcionarios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skill',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
