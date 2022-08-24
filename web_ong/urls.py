"""web_ong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name = 'inicio'),
    path('Acercade/contacto', views.Contacto, name='contacto'),
    path('Acercade/nosotros', views.Nosotros, name= 'nosotros'),
    path('login/', auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('usuario/', include('apps.usuarios.urls')),
    path('Noticias/', include('apps.noticias.urls')),
    #path('regitrarse/', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]