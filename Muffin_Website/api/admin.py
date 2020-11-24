from django.contrib import admin
from .models import Order, IndividualOrder

"""class IndividualOrderInLine(admin.TabularInline):
    model = IndividualOrder
    extra = 7

#Dictate order of fields
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['customer']}),
        ('Date info', {'fields': ['delivery_date'], 'classes': ['collapse']}),
    ]
    inlines = [IndividualOrderInLine]
    list_display = ('customer', 'delivery_date')
    list_filter = ['delivery_date']
    search_fields = ['customer']


admin.site.register(Order, OrderAdmin)"""