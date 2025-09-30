from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_libro', models.ForeignKey(on_delete=models.deletion.CASCADE, to='libros.libro', db_column='libro_id')),
                ('nombre_usuario', models.ForeignKey(on_delete=models.deletion.CASCADE, to='usuarios.usuario', db_column='usuario_id')),
                ('nombre', models.ForeignKey(on_delete=models.deletion.CASCADE, to='empleados.empleado', db_column='empleado_id')),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('hora_prestamo', models.TimeField(auto_now_add=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('hora_devolucion', models.TimeField(blank=True, null=True)),
                ('estado', models.CharField(default='pendiente', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
