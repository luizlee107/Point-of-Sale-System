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
    

  
    path('pos/card',views.card,name='card'),
    path('pos/cash',views.cash,name='cash'),
    path('cart/<str:pk>/delete',views.delete_cart,name='delete_cart'),
    path('cart/<str:pk>/edit', views.edit_cart, name='edit_cart'),
    path('cart/delete_all',views.delete_cart_all,name='delete_cart_all'),
    path('cart/receipt',views.receipt,name='receipt'),


    path('calculator/',views.calc,name='calc'),

    path('export-pdf-receipt/', views.export_pdf_receipt, name='export-pdf-receipt'),  
    path('export-pdf/', views.export_pdf2, name='export-pdf'),  
]