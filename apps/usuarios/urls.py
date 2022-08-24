from django.urls import path

from .views import RegistrarUsuario

app_name = 'usuarios'

urlpatterns = [
    path('registarse/', RegistrarUsuario.as_view(), name = 'registro')
]