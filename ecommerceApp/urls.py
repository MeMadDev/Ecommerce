from django.urls import path
from ecommerceApp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('order',views.order,name="order"),
    path('my_profile',views.my_profile,name="my_profile"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('cart',views.cart,name="cart"),
]
