# Generated by Django 5.0.4 on 2024-04-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('idade', models.DateField()),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
    ]