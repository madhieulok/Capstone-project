

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from .models import Menu
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class _LC:
    TMPLT_INDEX = 'restaurant/index.html'


def index(request):
    return render(
        request,
        _LC.TMPLT_INDEX,
        dict(),
    )


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]