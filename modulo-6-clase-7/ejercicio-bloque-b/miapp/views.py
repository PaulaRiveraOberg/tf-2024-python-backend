from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, UpdateView

from .forms import CommentForm, PostForm
from .models import Comment, Post


def home(request):
    """Vista para la página principal."""
    recent_posts = Post.objects.filter(is_published=True).order_by("-created_at")[:5]

    context = {
        "recent_posts": recent_posts,
    }

    if request.user.is_authenticated:
        user_posts = Post.objects.filter(author=request.user).order_by("-created_at")[
            :5
        ]
        context["user_posts"] = user_posts

    return render(request, "miapp/home.html", context)


@login_required
def profile_view(request):
    """Vista para el perfil del usuario."""
    # Obtener todas las publicaciones del usuario
    posts = Post.objects.filter(author=request.user).order_by("-created_at")

    # Obtener todos los comentarios del usuario
    comments = Comment.objects.filter(author=request.user).order_by("-created_at")[:5]

    # Contadores para estadísticas
    user_posts_count = posts.count()
    user_comments_count = Comment.objects.filter(author=request.user).count()

    context = {
        "posts": posts,
        "comments": comments,
        "user_posts_count": user_posts_count,
        "user_comments_count": user_comments_count,
    }

    return render(request, "miapp/profile.html", context)


@login_required
@permission_required("miapp.add_post", raise_exception=True)
def create_post(request):
    """Vista para crear una nueva publicación."""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # El usuario actual es el autor
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, "¡La publicación ha sido creada con éxito!")
            return redirect("miapp:profile")
    else:
        form = PostForm()

    return render(request, "miapp/create_post.html", {"form": form})


@login_required
@permission_required("miapp.change_own_post", raise_exception=True)
def edit_post(request, pk):
    """Vista para editar una publicación existente."""
    post = get_object_or_404(Post, pk=pk)

    # Verificar que el usuario es el autor
    if request.user != post.author:
        messages.error(request, "No tienes permiso para editar esta publicación.")
        return redirect("miapp:profile")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "¡La publicación ha sido actualizada con éxito!")
            return redirect("miapp:profile")
    else:
        form = PostForm(instance=post)

    return render(request, "miapp/edit_post.html", {"form": form})


class EditCommentView(PermissionRequiredMixin, UpdateView):
    model = Comment
    fields = ["body"]
    template_name = "miapp/edit_comment.html"
    permission_required = "miapp.change_comment"

    def get_success_url(self):
        messages.success(self.request, "¡El comentario ha sido actualizado con éxito!")
        return reverse("miapp:profile")

    def form_valid(self, form):
        # Asegurarse de que solo el autor pueda editar el comentario
        if self.request.user != self.get_object().author:
            messages.error(
                self.request, "No tienes permiso para editar este comentario."
            )
            return redirect("miapp:profile")
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = "miapp/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        """Solo mostrar publicaciones publicadas, ordenadas por fecha de creación descendente."""
        return Post.objects.filter(is_published=True).order_by("-created_at")


@login_required
def add_comment(request, post_id):
    """Vista para agregar un comentario a una publicación."""
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        body = request.POST.get("body")
        if body:
            comment = Comment(
                post=post,
                author=request.user,
                body=body,
                is_published=True,  # Por defecto, los comentarios son publicados
            )
            comment.save()
            messages.success(request, "¡Comentario agregado con éxito!")
        else:
            messages.error(request, "El comentario no puede estar vacío.")

    # Redirigir a la vista de lista de publicaciones
    return redirect("miapp:post_list")
