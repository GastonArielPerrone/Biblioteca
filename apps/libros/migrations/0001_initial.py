from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autores', '0001_initial'),
        ('editoriales', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, db_column='titulo_libro')),
                ('fecha_publicacion', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autores.autor', db_column='nombre_autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editoriales.editorial', db_column='nombre_editorial')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria', db_column='nombre_categoria')),
            ],
        ),
    ]
