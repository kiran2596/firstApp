
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
          path('', views.index ,name="ShopHome"),
          path('about/', views.about ,name="AboutUS"),
          path('contact/', views.contact ,name="ContactUS"),
          path('tracker/', views.tracker ,name="Tracker"),
          path('productview/', views.proView ,name="ProductViewc"),
          path('checkout/', views.checkout ,name="Checkout"),
]
