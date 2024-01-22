from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [

    path('pos/',views.pos,name='pos'),


    #verify 2 functions in the same page
    path('product', views.product, name='product'),
    path('product_list', views.product_list, name='product_list'),
    path('product/add', views.add_product, name='add_product'),
    path('products/<int:pk>/remove', views.remove_product, name='remove_product'),
    path('product/<int:pk>/edit', views.edit_product, name='edit_product'),


    path('products/filter',views.products_filter,name='products_filter'),

    
 
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('popup_content',views.products2,name='popup_content'),
    path('calculator/',views.calc,name='calc')
]