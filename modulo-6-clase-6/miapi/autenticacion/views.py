from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render


# Create your views here.
def home(request):
    return render(request, "home.html")


def profile(request):
    oauth2_data = request.user.social_auth.get(provider="github")
    return render(request, "profile.html", {"oauth2_data": oauth2_data})
