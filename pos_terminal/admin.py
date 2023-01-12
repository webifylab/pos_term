from django.contrib import admin
from .models import Orders

# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'foods')
  list_display_links = ('id', 'title')
  search_fields = ('id', 'title', 'foods')

admin.site.register(Orders, OrdersAdmin)