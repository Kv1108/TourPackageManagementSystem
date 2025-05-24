from django.db import models
from django.utils.text import slugify

class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    location = models.CharField(max_length=100)
    featured_image = models.ImageField(upload_to='tour_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Itinerary(models.Model):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='itineraries')
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    transportation = models.CharField(max_length=200, blank=True, null=True)
    attractions = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Itineraries"
        ordering = ['day_number']

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"