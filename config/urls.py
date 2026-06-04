"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from blog.views import home, post1, post2, post3, crear_post, editar_post, borrar_post, detalle_post, about, contacto


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('post1/', post1, name='post1'),

    path('post2/', post2, name='post2'), 

    path('post3/', post3, name='post3'),

    path('nuevo/', crear_post, name='nuevo'),

    path('editar/<int:id>/', editar_post, name='editar_post'),

    path('borrar/<int:id>/', borrar_post, name='borrar_post'),

    path('detalle/<int:id>/', detalle_post, name='detalle_post'),

    path('about/', about, name='about'),

    path('contacto/', contacto, name='contacto'),
]
