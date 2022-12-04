from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.models import Listing


# Adding context allows us to access the data on the templates
def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)  # sort by most recent
    paginator = Paginator(listings, 3)  # sort listings, 3 per page
    page = request.GET.get('page')  # calls the page from the back end
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
