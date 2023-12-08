from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [

    path('pos/',views.pos,name='pos'),
    path('create_product/',views.create_product,name='create_product'),
    path('products/',views.products,name='products'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('popup_content',views.products2,name='popup_content'),
]