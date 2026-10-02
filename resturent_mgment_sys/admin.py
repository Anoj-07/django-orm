from django.contrib import admin
from unfold.admin import ModelAdmin

from resturent_mgment_sys.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)