# Generated by Django 4.2.7 on 2023-11-24 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_usuario_cpf_remove_usuario_telefone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='data_nascimento',
        ),
    ]
