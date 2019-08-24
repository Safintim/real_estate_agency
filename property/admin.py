from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year', ]
    search_fields = ['town', 'town_district', 'address', 'owner', ]
    readonly_fields = ['created_at', ]
    list_editable = ['new_building', ]
