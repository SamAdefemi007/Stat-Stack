from django.shortcuts import render
from .models import Player

# Create your views here.


def home(request):
    return render(request, 'statlist/home.html')


def profile(request):
    playerobj = Player.objects.all().order_by("-skills__rating")[:10]
    return render(request, 'statlist/profile.html', {'players': playerobj})
