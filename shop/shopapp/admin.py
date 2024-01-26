from django.contrib import admin
from shopapp.models import Client, Product, Order

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'quantity', 'image']
    ordering=['name', 'quantity']
    list_filter=['date_time_additions_product']
    search_fields =['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'date_time_placing_order']
    list_filter=['client', 'date_time_placing_order']
    search_fields =['client']

admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


