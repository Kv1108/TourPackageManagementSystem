from django.contrib import admin
from .models import TourPackage, Itinerary

class ItineraryInline(admin.TabularInline):
    model = Itinerary
    extra = 1

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration', 'location')
    search_fields = ('title', 'location')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ItineraryInline]

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('tour_package', 'day_number', 'title')
    list_filter = ('tour_package',)