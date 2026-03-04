from django_filters.rest_framework import FilterSet
from .models import Hotels, Room


class HotelFilter(FilterSet):
    class Meta:
        model = Hotels
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'services': ['exact']
        }

class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'room_status': ['exact'],
            'price': ['gt', 'lt']
        }