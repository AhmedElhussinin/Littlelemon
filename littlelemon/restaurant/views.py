from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import MenuItemsSerializers, BookingSerializers
from . models import MenuItems, Booking

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
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    # permission_classes = [permissions.IsAuthenticated]    

class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers    