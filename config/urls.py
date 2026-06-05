from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (
    home, crear_post, editar_post, borrar_post,
    detalle_post, categoria_posts,
    about, contacto,
    login_view, logout_view,
)
urlpatterns = [
    path('admin/', admin.site.urls),

    # Páginas públicas
    path('', home, name='home'),
    path('post/<slug:slug>/', detalle_post, name='detalle_post'),
    path('categoria/<slug:slug>/', categoria_posts, name='categoria_posts'),
    path('about/', about, name='about'),
    path('contacto/', contacto, name='contacto'),

    # Gestión de posts (protegidas)
    path('nuevo/', crear_post, name='nuevo'),
    path('editar/<slug:slug>/', editar_post, name='editar_post'),
    path('borrar/<slug:slug>/', borrar_post, name='borrar_post'),

    # Autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Manejadores de error personalizados
handler404 = 'blog.views.error_404'
handler500 = 'blog.views.error_500'
