# Generated by Django 5.1.2 on 2024-10-19 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tarefa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]
