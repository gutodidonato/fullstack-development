# Generated by Django 5.1.3 on 2024-11-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_remove_skillcategory_major_skill_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillcategory',
            name='ativo',
        ),
        migrations.AddField(
            model_name='skill',
            name='pos_destaque',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
