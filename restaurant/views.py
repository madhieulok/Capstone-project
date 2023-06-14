

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


def index(request):
    return render(request, "index.html")

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_itemn = MenuItemSerializer(items, many = True)
    return Response(serialized_itemn.data)
    #return Response(items.values())
    
@api_view()
def single_item(request, id):
    item = get_object_or_404 (MenuItem, pk=id)
    serialized_itemn = MenuItemSerializer(item)
    return Response(serialized_itemn.data)


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"some secret message"})
    
    
    
  

#from rest_framework import generics
#from .models import MenuItem
#from .serializers import MenuItemSerializer


    
#@api_view()
#@permission_classes([IsAuthenticated])

#def securedview(request):
    #return Response({"message": "needs authentication"})