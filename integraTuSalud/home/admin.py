from django.contrib import admin
from .models import Articulo
from tinymce.widgets import TinyMCE


#formfield_overrides = {
#    models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
#}
#admin.site.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'etiqueta', 'imagen', 'fecha')
    #fields = ['titulo', 'autor', 'etiqueta']

admin.site.register(Articulo, ArticuloAdmin)
# Register your models here.
