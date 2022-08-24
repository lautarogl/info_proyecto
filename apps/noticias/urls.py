from django.urls import path
from . import views

app_name = 'noticias'
urlpatterns = [
    path('addnoticia/', views.AddNoticia.as_view(), name = 'addnoti'),
    path('mostrar_noticias', views.NoticiasClase.as_view(), name = 'noti'),
    path('detalle/<int:pk>', views.DetalleNoticiaClase.as_view(), name = 'detallenoticia'),
    path(r'^noticia/(?P<pk>[0-9]+)/comentario/$', views.add_comment_to_post, name='add_comment_to_post'),
]