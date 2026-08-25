from django.contrib import admin
from .models import Plot, UserAllotment

# Register your models here.


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ['plot_number', "owners"]

    def owners(self, obj):
        return ", ".join([user.username for user in obj.userallotment_set.all()])

        