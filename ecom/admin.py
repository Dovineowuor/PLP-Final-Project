# admin.py
from django.contrib import admin
from .models import Customer, Product, Orders, Feedback, Category

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at', 'updated_at')
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ('name', 'description', 'quantity', 'price', 'created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feedback, FeedbackAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)
