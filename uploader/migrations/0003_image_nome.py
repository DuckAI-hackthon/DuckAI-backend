# Generated by Django 4.2.7 on 2023-11-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_image_turma'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='nome',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
