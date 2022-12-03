from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    # shows the fieldssto display on admin panel
    # set the clickable links with lis_display
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'county', 'postcode', 'price')
    list_per_page = 10

    # Register the model
admin.site.register(Listing, ListingAdmin)
