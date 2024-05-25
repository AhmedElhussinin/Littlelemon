from .models import MenuItems, Booking
from rest_framework import serializers


class MenuItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'