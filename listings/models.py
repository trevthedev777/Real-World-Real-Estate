from django.db import models
from datetime import datetime
from realtors.models import Realtor


# DO_NOTHING = keeps the listing even if the realtor is deleted
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    address = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=200)
    county = models.CharField(max_length=20)
    postcode = models.CharField(max_length=8)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqm = models.IntegerField()
    lot_size = models.DecimalField(max_digits=6, decimal_places=1)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    # The main field
    def __str__(self):
        return self.title
