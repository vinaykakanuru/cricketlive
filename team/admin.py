from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayerHistory)
admin.site.register(Matches)
admin.site.register(PointsTable)