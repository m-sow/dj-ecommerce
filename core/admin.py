from django.contrib import admin
from .models import Item,OrderItem, Order

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)