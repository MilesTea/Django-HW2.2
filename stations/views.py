from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        paginator = Paginator(list(reader), 10)
    page = paginator.get_page(request.GET.get('page', 1))
    _bus_stations = []
    for station in page.object_list:
        _bus_stations.append(station)
    context = {
         'bus_stations': _bus_stations,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
