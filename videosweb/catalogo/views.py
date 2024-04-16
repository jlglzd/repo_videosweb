from django.shortcuts import render

# Create your views here.

from .models import Video, Autor, VideoInstancia, Genre

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books=Video.objects.all().count()
    num_instances=VideoInstancia.objects.all().count()
    # Videos disponibles (status = 'a')
    num_instances_available=VideoInstancia.objects.filter(status__exact='a').count()
    num_authors=Autor.objects.count()  # El 'all()' esta implícito por defecto.

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

from django.views import generic

class BookListView(generic.ListView):
    model = Video

class BookDetailView(generic.DetailView):
    model = Video

