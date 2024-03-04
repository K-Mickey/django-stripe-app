from django.contrib import admin

from .models import Item, Order, Discount, Tax


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'currency',
    )


class OrderItemInline(admin.TabularInline):
    model = Order.items.through
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderItemInline,
    )


admin.site.register(Discount)
admin.site.register(Tax)
