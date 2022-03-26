import csv
from .models import Player, Country, Club, TransferMarket, Skills
from pathlib import Path


for item in [Player, Country, Club, TransferMarket, Skills]:
    item.objects.all().delete()

print("Table dropped successfully")
BASE_DIR = Path(__file__).resolve().parent.parent
data_link = str(BASE_DIR) + '/statlist/data/data.csv'

with open(data_link) as file:
    reader = csv.reader(file, delimiter=",")
    next(reader)
    name = set()
    clubSet = set()
    for row in reader:
        country_obj = Country.objects.create(
            countryName=row[4], countryFlag=row[5])
        club_obj = Club.objects.create(
            clubName=row[8],
            clubLogo=row[9]
        )

        skill_obj = Skills.objects.create(
            prefferedFoot=row[13],
            pace=row[35],
            shooting=row[39],
            passing=row[27],
            strength=row[42],
            dribbling=row[29],
            defending=row[60],
            rating=row[58]
        )

        transfer_obj = TransferMarket.objects.create(
            value=row[10],
            contractExpiry=int(row[21]),
            wages=row[11],
            releaseClause=row[59]
        )

        Player.objects.create(
            playerName=row[1],
            playerAge=row[2],
            playerPhoto=row[3],
            playerPosition=row[57],
            playerCountry=country_obj,
            playerClub=club_obj,
            skills=skill_obj,
            playerValue=transfer_obj
        )


print("data parsed")
