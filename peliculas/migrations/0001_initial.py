# Generated by Django 5.1.2 on 2024-11-14 17:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('serie', models.CharField(choices=[('dragon ball', 'Dragon Ball'), ('dragon ball z', 'Dragon Ball Z'), ('dragon ball super', 'Dragon Ball Super')], default='dragon ball', max_length=30)),
                ('sinopsis', models.TextField()),
                ('estreno', models.DateField()),
                ('imagen', models.ImageField(upload_to='peliculas/')),
                ('fecha_subida', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
