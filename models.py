from django.db import models
from django.urls import reverse


class Testimonials(models.Model):
    name = models.CharField(max_length=25, blank=False)
    photo = models.ImageField(blank=False, null=False)
    job = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.name
