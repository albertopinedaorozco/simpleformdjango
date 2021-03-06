# Generated by Django 2.2.2 on 2019-06-19 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
                ('observaciones', models.TextField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Mesero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=30)),
                ('ingredientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saludo.Ingrediente')),
            ],
        ),
    ]
