from django.contrib import admin
from account.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
