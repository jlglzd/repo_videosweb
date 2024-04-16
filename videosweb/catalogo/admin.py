from django.contrib import admin

# Register your models here.

from .models import Autor, Genre, Video, VideoInstancia

#admin.site.register(Video)
#admin.site.register(Autor)
admin.site.register(Genre)
#admin.site.register(VideoInstancia)

# Define the admin class
class AutorAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombre', 'fecha_de_nacimiento')

# Register the admin class with the associated model
admin.site.register(Autor, AutorAdmin)

# Register the Admin classes for Video using the decorator

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for VideoInstance using the decorator

@admin.register(VideoInstancia)
class VideoInstanciaAdmin(admin.ModelAdmin):
    pass

