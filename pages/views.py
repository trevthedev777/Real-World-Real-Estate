from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, county_choices


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'county_choices': county_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get Realtor of the month
    rotm_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'rotm_realtors': rotm_realtors
    }
    return render(request, 'pages/about.html', context)


# def about(request):
#     return render(request, 'pages/listings.html')
