#from django.contrib import admin
from django.urls import path
from . import views

#import restaurant
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path("index/", views.index),
     #path('menu-items/', views.menu_items),
    # add following lines to urlpatterns list
     path('menu-items/', views.MenuItemsView.as_view()),
     path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
     path('secret/', views.secret),
     #path('menu/<int:id>', views.single_item),
     
     path('api-token-auth/', obtain_auth_token),
]
