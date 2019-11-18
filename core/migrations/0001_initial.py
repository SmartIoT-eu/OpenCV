# Generated by Django 2.0 on 2019-11-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('info', models.TextField(verbose_name='Información')),
                ('image', models.ImageField(upload_to='base', verbose_name='Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace externo')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'perfiles',
                'ordering': ['-created'],
            },
        ),
    ]
