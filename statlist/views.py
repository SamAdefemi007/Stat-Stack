from django.shortcuts import render
from .models import Player, Country, Club
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
    countryname = None
    countryflag = None
    if request.method == "POST":
        countryname = request.POST["countrySet"]
        countryflag = Country.objects.all().filter(
            countryName=countryname).first().countryFlag
        playerobj = Player.objects.all().filter(
            playerCountry__countryName=countryname).order_by("-skills__rating")
    return render(request, 'statlist/country.html', {'countries': countryObj, 'players': playerobj, 'countryname': countryname, 'countryflag': countryflag})


def club(request):
    clubObj = Club.objects.all().values_list(
        "clubName", flat=True).distinct()

    playerobj = {}
    clubname = None
    clublogo = None
    if request.method == "POST":
        clubname = request.POST.get("clubSet")
        clublogo = Club.objects.all().filter(
            clubName=clubname).first().clubLogo
        playerobj = Player.objects.all().filter(
            playerClub__clubName=clubname).order_by("-skills__rating")

    return render(request, 'statlist/club.html', {'clubs': clubObj, 'players': playerobj, 'clubname': clubname, 'clublogo': clublogo})


def details(request, id):
    playerobj = Player.objects.all().filter(
        playerID=id).order_by("-skills__rating").first()
    return render(request, 'statlist/playerdetail.html', {'player': playerobj})
