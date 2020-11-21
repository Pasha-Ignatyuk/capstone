from django.contrib import admin
from orders.models import Status, Order, ProductsInOrder, ProductInBasket

# Register your models here.

class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder
    extra = 0

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status,StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines =[ProductsInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order,OrderAdmin)

class ProductsInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductsInOrder._meta.fields]

    class Meta:
        model = ProductsInOrder

admin.site.register(ProductsInOrder,ProductsInOrderAdmin)

class ProductInBasketAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)
