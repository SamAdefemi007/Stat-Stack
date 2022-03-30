from django.http import HttpResponse
from django.shortcuts import render
from .models import Player, Country, Club
from django.core.paginator import Paginator
from django.core.exceptions import *

# Create your views here.


def home(request):
    return render(request, 'statlist/home.html')


def profile(request):
    try:
        playerobj = Player.objects.all().order_by("-skills__rating")
    except ObjectDoesNotExist:
        print("the player object does not exist or could not be fetched from the database")
    else:
        paginator = Paginator(playerobj, 15)
        page_num = request.GET.get("page")
        page_obj = paginator.get_page(page_num)
    return render(request, 'statlist/profile.html', {'players': page_obj})


def country(request):
    try:
        countryObj = Country.objects.all().values_list(
            "countryName", flat=True).distinct()
    except ObjectDoesNotExist:
        print("the country object does not exist or could not be fetched from the database")
    playerobj = {}
    countryname = None
    countryflag = None
    if request.method == "POST":
        countryname = request.POST["countrySet"]
        try:
            countryflag = Country.objects.all().filter(
                countryName=countryname).first().countryFlag
        except MultipleObjectsReturned:
            print(
                "The query returned more than one object, possible duplication of countryname or wrong queryset")
        else:
            playerobj = Player.objects.all().filter(
                playerCountry__countryName=countryname).order_by("-skills__rating")
    return render(request, 'statlist/country.html', {'countries': countryObj, 'players': playerobj, 'countryname': countryname, 'countryflag': countryflag})


def club(request):
    try:
        clubObj = Club.objects.all().values_list(
            "clubName", flat=True).distinct()
    except ObjectDoesNotExist:
        print("the club object does not exist or could not be fetched from the database")
    playerobj = {}
    clubname = None
    clublogo = None
    if request.method == "POST":
        clubname = request.POST.get("clubSet")
        try:
            clublogo = Club.objects.all().filter(
                clubName=clubname).first().clubLogo
        except MultipleObjectsReturned:
            print(
                "The query returned more than one object, possible duplication of countryname or wrong queryset")
        else:
            playerobj = Player.objects.all().filter(
                playerClub__clubName=clubname).order_by("-skills__rating")

    return render(request, 'statlist/club.html', {'clubs': sorted(clubObj), 'players': playerobj, 'clubname': clubname, 'clublogo': clublogo})


def details(request, id):
    try:
        playerobj = Player.objects.all().filter(
            playerID=id).order_by("-skills__rating").first()
    except ObjectDoesNotExist:
        print("the Player object does not exist or could not be fetched from the database")
    except MultipleObjectsReturned:
        print("The query returned more than one object, possible duplication of countryname or wrong queryset")
    return render(request, 'statlist/playerdetail.html', {'player': playerobj})
