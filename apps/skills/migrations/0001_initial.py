# Generated by Django 5.1.3 on 2024-11-15 02:37

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MajorSkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descricao', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='descricao')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descricao', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='descricao')),
                ('ativo', models.BooleanField(default=True)),
                ('major_skill_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skills.majorskillcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('level', models.IntegerField(blank=True)),
                ('logo', models.ImageField(blank=True, upload_to='skills/logos')),
                ('resumo', models.TextField()),
                ('imagem_central', models.ImageField(blank=True, upload_to='skills/imagem_central')),
                ('descricao', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='descricao')),
                ('ativo', models.BooleanField(default=True)),
                ('skill_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='skills.skillcategory')),
            ],
        ),
    ]