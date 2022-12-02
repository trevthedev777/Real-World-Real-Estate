from django.urls import path

from . import views
# 1. /listings, calls from the listings view file
# 2. Search is linked to the main urls.py file, anything with
#  listings/ will route from here
urlpatterns = [
    path('', views.index, name='listings'),  # Listings page
    path('<int:listing_id>', views.listing,
         name='listing.html'),  # listing page
    path('search.html', views.search, name='search.html'),
]
