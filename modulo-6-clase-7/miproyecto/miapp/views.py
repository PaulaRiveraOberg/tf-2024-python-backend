from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from .models import Post


def home(request):
    return render(request, "miapp/home.html")


@login_required
def profile(request):
    return render(request, "miapp/profile.html")


@login_required
@permission_required("miapp.add_post", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        Post.objects.create(title=title, body=body, author=request.user)
        return redirect("miapp:profile")
    else:
        return render(request, "miapp/create_post.html")
