from django.contrib import admin
from .models import *


admin.site.register(Product,verbose_name=Product)

admin.site.register(Sale,verbose_name=Sale)
admin.site.register(Purchase,verbose_name=Purchase)

admin.site.register(Pos,verbose_name=Purchase)
