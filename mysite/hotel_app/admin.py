from django.contrib import admin
from .models import (UserProfile, Country, City, Services, Hotels, ImageHotel,
                     Room, ImageRoom, Review, Booking)
from modeltranslation.admin import TranslationAdmin

@admin.register(City, Country, Services)

class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ImageHotelInline(admin.TabularInline):
    model = ImageHotel
    extra = 1

class HotelAdmin(admin.ModelAdmin):
    inlines = [ImageHotelInline]

admin.site.register(UserProfile)
admin.site.register(Hotels, HotelAdmin)
admin.site.register(Room)
admin.site.register(ImageRoom)
admin.site.register(Review)
admin.site.register(Booking)
