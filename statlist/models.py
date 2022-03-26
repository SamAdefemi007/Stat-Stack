from operator import truediv
from django.db import models

# Create your models here.


class Country(models.Model):
    countryID = models.AutoField(primary_key=True)
    countryName = models.CharField(max_length=200)
    countryFlag = models.URLField(max_length=1000)

    def __str__(self):
        return self.countryName


class Club(models.Model):
    clubID = models.AutoField(primary_key=True)
    clubName = models.CharField(max_length=200)
    clubLogo = models.URLField(max_length=1000)

    def __str__(self):
        return self.clubName


class Skills(models.Model):
    skillsID = models.AutoField(primary_key=True)
    prefferedFoot = models.CharField(max_length=10)
    pace = models.IntegerField(default=0)
    shooting = models.IntegerField(default=0)
    passing = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    dribbling = models.IntegerField(default=0)
    defending = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.rating}, {self.prefferedFoot}"


class TransferMarket(models.Model):
    transferID = models.AutoField(primary_key=True)
    value = models.IntegerField(default=0, null=True)
    contractExpiry = models.DateField()
    wages = models.CharField(max_length=10)
    releaseClause = models.CharField(max_length=10)

    def __str__(self):
        return self.value, self.wages, self.releaseClause, self.contractExpiry


class Player(models.Model):
    playerID = models.AutoField(primary_key=True)
    playerName = models.CharField(max_length=200)
    playerAge = models.IntegerField(default=0)
    playerPhoto = models.URLField(max_length=1000)
    playerPosition = models.CharField(max_length=3)
    playerCountry = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True)
    playerClub = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    skills = models.OneToOneField(
        Skills, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.playerName, self.playerAge, self.playerPosition
