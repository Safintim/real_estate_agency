from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year', ]
    search_fields = ['town', 'town_district', 'address', 'owner', ]
    readonly_fields = ['created_at', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', 'rooms_number', 'has_balcony', ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text', ]
    search_fields = ['user__username', 'flat__town', 'flat__address', ]
    list_filter = ['flat__town', ]
    raw_id_fields = ['flat']
