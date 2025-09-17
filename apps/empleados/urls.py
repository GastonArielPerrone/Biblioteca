from django.urls import path
from .views import EmployeeRegistrationView

urlpatterns = [
    path('empleados/registrar/', EmployeeRegistrationView.as_view(), name='empleado-register'),
]
