from rest_framework import serializers
from .models import Menu, Booking
#from restaurant import MenuItem, Category





_ALL_FIELDS = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = _ALL_FIELDS



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = _ALL_FIELDS

