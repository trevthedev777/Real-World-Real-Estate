from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    # The main field
    def __str__(self):
        return self.name
