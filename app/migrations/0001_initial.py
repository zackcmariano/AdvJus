# Generated by Django 3.2 on 2021-04-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('rg', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=14)),
                ('nasc', models.CharField(max_length=10)),
                ('sexo', models.CharField(max_length=10)),
                ('ddd', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]