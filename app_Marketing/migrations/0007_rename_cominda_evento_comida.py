# Generated by Django 5.0.6 on 2024-06-03 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Marketing', '0006_alter_campania_fechafinal_alter_campania_fechainicio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='cominda',
            new_name='comida',
        ),
    ]
