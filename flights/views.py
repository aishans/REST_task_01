from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Flight, Booking
from .serializers import *

class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

class BookingList(ListAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
