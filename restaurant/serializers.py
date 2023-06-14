from rest_framework import serializers
from .models import MenuItem
#from restaurant import MenuItem, Category





class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        
    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length=255)
    


#class CategorySerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Category
        #fields = ['id', 'title']

#class MenuItemSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = MenuItem
        #fields = ['id','title','price','inventory']
        
