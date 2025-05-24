from django.shortcuts import render, get_object_or_404
from .models import TourPackage

def tour_list(request):
    tours = TourPackage.objects.all()
    return render(request, 'tours/tour_list.html', {'tours': tours})

def tour_detail(request, slug):
    tour = get_object_or_404(TourPackage, slug=slug)
    return render(request, 'tours/tour_detail.html', {'tour': tour})