from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Último login')),
                ('dni', models.CharField(max_length=20, unique=True, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=150, blank=True, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=150, blank=True, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='Email')),
                ('telefono', models.CharField(max_length=20, blank=True, verbose_name='Teléfono')),
                ('cargo', models.CharField(max_length=100, blank=True, verbose_name='Cargo')),
                ('fecha_contratacion', models.DateField(blank=True, null=True, verbose_name='Fecha de contratación')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de alta')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]
