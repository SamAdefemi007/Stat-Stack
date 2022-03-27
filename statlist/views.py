from django.shortcuts import render
from .models import Player, Country
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


def country(request):
    countryObj = Country.objects.all().values_list(
        "countryName", flat=True).distinct()
    playerobj = {}
    if request.method == "POST":
        countryname = request.POST["countrySet"]
        playerobj = Player.objects.all().filter(
            playerCountry__countryName=countryname).order_by("-skills__rating")
    return render(request, 'statlist/country.html', {'countries': countryObj, 'players': playerobj})
