from django.shortcuts import render
from .models import Player
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    return render(request, 'statlist/home.html')


def profile(request):
    playerobj = Player.objects.all().order_by("-skills__rating")
    paginator = Paginator(playerobj, 15)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return render(request, 'statlist/profile.html', {'players': page_obj})
