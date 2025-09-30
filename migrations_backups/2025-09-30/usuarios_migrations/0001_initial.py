from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=15, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=100)),
                ('numero_calle', models.IntegerField()),
                ('casa', models.BooleanField(default=False)),
                ('edificio', models.BooleanField(default=False)),
                ('piso', models.CharField(max_length=10, null=True, blank=True)),
                ('departamento_numero_casa', models.CharField(max_length=10, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
