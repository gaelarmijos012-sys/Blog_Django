from django.contrib import admin
from .models import Post, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'tiene_archivo')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'resumen', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    readonly_fields = ('fecha_publicacion',)

    fieldsets = (
        ('Contenido', {
            'fields': ('titulo', 'slug', 'resumen', 'contenido', 'categoria')
        }),
        ('Archivo adjunto', {
            'fields': ('archivo',),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('fecha_publicacion',),
            'classes': ('collapse',),
        }),
    )

    def tiene_archivo(self, obj):
        return bool(obj.archivo)
    tiene_archivo.boolean = True
    tiene_archivo.short_description = 'Archivo'
