from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.comentarios.models import Comentario
from .forms import CommentForm 
from .models import Noticia

def Noticias(request):
    #creo dicionario para pasar datos al tempaltes
    ctx = {}
    #buscar en bd lo que quiero y traerlo al templates
    notic = Noticia.objects.all()
    ctx['notis']=notic
    return render(request, 'noticias/noticias.html',ctx)

def DetalleNoticia(request, pk):
    ctx = {}
    noticias = Noticia.objects.get(pk = pk)
    ctx['resultado'] = noticias

    return render(request, 'noticias/detallenoticia.html',ctx)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect('noticias.detallenoticia', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comentario/addcomentario.html', {'form': form})



class AddNoticia(CreateView):
    model = Noticia
    fields = ['autor','titulo', 'detalle', 'imagen', 'categoria']
    template_name = 'noticias/addNoticia.html'
    success_url = reverse_lazy('noticias:noti')

class NoticiasClase(ListView):
    model=Noticia
    template_name = 'noticias/noticias.html'

class DetalleNoticiaClase(DetailView):
    model = Noticia
    template_name = 'noticias/detallenoticia.html'
    

