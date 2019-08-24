from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['town', 'address', 'price', 'new_building', 'construction_year', 'owners_phone_pure', ]
    search_fields = ['town', 'town_district', 'address', 'owner', 'owners_phone_pure', ]
    readonly_fields = ['created_at', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', 'rooms_number', 'has_balcony', ]
    raw_id_fields = ['liked_by', 'owners']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text', ]
    search_fields = ['user__username', 'flat__town', 'flat__address', ]
    list_filter = ['flat__town', ]
    raw_id_fields = ['flat']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'owners_phone_pure', ]
    search_fields = ['name', 'flats__town', 'flats__address', 'owners_phone_pure', ]
    raw_id_fields = ['flats']
