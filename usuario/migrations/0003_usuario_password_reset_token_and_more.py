# Generated by Django 4.2.7 on 2023-11-25 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_usuario_cpf_remove_usuario_telefone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password_reset_token',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Password Reset Token'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password_reset_token_created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Password Reset Token Created'),
        ),
    ]
