from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Plot, User

# Register your models here.


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ['plot_number', "owners", "occupied"]

    def owners(self, obj):
        return ", ".join([user.username for user in obj.users.all()])



@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['first_name', 'last_name','username', 'email', 'plot']
    fieldsets = UserAdmin.fieldsets + (('allotment', {'fields': ('plot',)}), (None, {'fields': ('anonymous_username',)}),)
