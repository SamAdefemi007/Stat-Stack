from django.contrib import admin
from .models import Player, Club, Country, TransferMarket, Skills
# Register your models here.
admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Country)
admin.site.register(TransferMarket)
admin.site.register(Skills)
