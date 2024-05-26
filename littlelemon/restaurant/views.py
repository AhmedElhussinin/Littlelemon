import datetime
import json
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import MenuItemsSerializers, BookingSerializers
from . models import MenuItems, Booking
from . import serializers

# Create your views here.

@api_view()
@permission_classes(IsAuthenticated)
def msg(request):
    return Response({"message" : "this view is protected"})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializers


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializers    


class BookingView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def bookings(request):
         date = request.GET.get('date',datetime.today().date())
         bookings = Booking.objects.all()
         booking_json = serializers.serialize('json', bookings)
         return render(request, 'bookings.html',{"bookings":booking_json})  

    def bookings(request):
      if request.method == 'POST':
          data = json.load(request)
          exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
          if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
          else:
               return HttpResponse("{'error':1}", content_type='application/json')
    
      date = request.GET.get('date',datetime.today().date())

      bookings = Booking.objects.all().filter(reservation_date=date)
      booking_json = serializers.serialize('json', bookings)

      return HttpResponse(booking_json, content_type='application/json')  

class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers    