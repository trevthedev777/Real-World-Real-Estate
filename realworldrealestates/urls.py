from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Brings all apps for routing here
urlpatterns = [
    path('', include('pages.urls')),  # Home page
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
