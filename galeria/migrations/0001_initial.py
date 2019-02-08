# Generated by Django 2.1.5 on 2019-02-03 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('segundo_inicio', models.IntegerField(blank=True, null=True)),
                ('segundo_fin', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(verbose_name='fecha creacion')),
                ('ciudad', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galeria.Categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=20)),
                ('ciudad', models.CharField(max_length=20)),
                ('foto', models.ImageField(upload_to='archivos/fotos_usuarios/')),
                ('categorias_favoritas', models.ManyToManyField(to='galeria.Categoria')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reproducible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(verbose_name='fecha creacion')),
                ('ciudad', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('reproducible_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='galeria.Reproducible')),
                ('contenido', models.FileField(upload_to='archivos/audios/')),
            ],
            options={
                'abstract': False,
            },
            bases=('galeria.reproducible',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('reproducible_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='galeria.Reproducible')),
                ('contenido', models.FileField(upload_to='archivos/videos/')),
            ],
            options={
                'abstract': False,
            },
            bases=('galeria.reproducible',),
        ),
        migrations.AddField(
            model_name='reproducible',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galeria.Categoria'),
        ),
        migrations.AddField(
            model_name='reproducible',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galeria.Perfil'),
        ),
        migrations.AddField(
            model_name='imagen',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galeria.Perfil'),
        ),
        migrations.AddField(
            model_name='clip',
            name='referencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.Reproducible'),
        ),
    ]
