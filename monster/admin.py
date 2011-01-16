from django.contrib import admin
from monster.models import Monster

class MonsterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Monster, MonsterAdmin)
