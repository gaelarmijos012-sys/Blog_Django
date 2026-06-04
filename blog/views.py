from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import postForm

def editar_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = postForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = postForm(instance=post)
    return render(request, 'crear_nuevo.html', {'form': form, 'editando': True})

def borrar_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('home')

def detalle_post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'detalle_post.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def contacto(request):
    return render(request, 'contacto.html')

def crear_post(request):
    if request.method == "POST":
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = postForm()
    return render(request, 'crear_nuevo.html', {'form': form, 'editando': False})

def home(request):
    post = Post.objects.all().order_by('fecha_publicacion')
    return render(request, 'home.html', {'post': post})

def post1(request):
    return render(request, 'post1.html')

def post2(request):
    return render(request, 'post2.html')

def post3(request):
    return render(request, 'post3.html')
