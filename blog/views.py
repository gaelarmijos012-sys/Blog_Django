from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Post, Categoria
from .forms import PostForm


# ── Páginas públicas ─────────────────────────────────────────

def home(request):
    posts = Post.objects.select_related('categoria').order_by('-fecha_publicacion')

    # Filtro por categoría
    categoria_slug = request.GET.get('categoria')
    categoria_activa = None
    if categoria_slug:
        categoria_activa = get_object_or_404(Categoria, slug=categoria_slug)
        posts = posts.filter(categoria=categoria_activa)

    # Paginación: 5 posts por página
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, 'home.html', {
        'page_obj': page_obj,
        'categorias': categorias,
        'categoria_activa': categoria_activa,
    })


def detalle_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detalle_post.html', {'post': post})


def categoria_posts(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    posts = Post.objects.filter(categoria=categoria).order_by('-fecha_publicacion')
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'home.html', {
        'page_obj': page_obj,
        'categorias': Categoria.objects.all(),
        'categoria_activa': categoria,
    })


def about(request):
    return render(request, 'about.html')


def contacto(request):
    return render(request, 'contacto.html')


# ── Vistas protegidas (requieren login) ──────────────────────

@login_required(login_url='/login/')
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect(f'/?msg=creado')
    else:
        form = PostForm()
    return render(request, 'crear_nuevo.html', {'form': form, 'editando': False})


@login_required(login_url='/login/')
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/?msg=editado')
    else:
        form = PostForm(instance=post)
    return render(request, 'crear_nuevo.html', {'form': form, 'editando': True})


@login_required(login_url='/login/')
def borrar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('/?msg=eliminado')


# ── Autenticación ─────────────────────────────────────────────

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        error = 'Usuario o contraseña incorrectos'
    else:
        form = AuthenticationForm()
        error = None
    return render(request, 'login.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('home')


# ── Páginas de error ──────────────────────────────────────────

def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)
