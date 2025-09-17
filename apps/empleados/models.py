from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EmpleadoManager(BaseUserManager):
    def create_user(self, dni, password=None, **extra_fields):
        if not dni:
            raise ValueError('El DNI es un campo obligatorio')
        
        user = self.model(dni=dni, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(dni, password, **extra_fields)

class Empleado(AbstractBaseUser, PermissionsMixin):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=100, null=False, blank=False)
    dni = models.CharField(max_length=15, unique=True, null=False, blank=False)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)
    fecha_contratacion = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = EmpleadoManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombre_empleado']

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado
