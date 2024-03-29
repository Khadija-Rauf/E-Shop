from django.contrib import admin
from .models import *

def make_refund_accepted(modeladmin,request,queryset):
    queryset.updated(refund_requested=False, refund_granted=True)

make_refund_accepted.short_description = "Update orders to refund granted"

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered','being_delievered','recieved','refund_requested','refund_granted', 'billing_address','payment','coupon']
    list_display_links = ['user', 'billing_address','payment','coupon']
    list_filter = ['user', 'ordered','being_delievered','recieved','refund_requested','refund_granted']
    search_fields = ['user__username','ref_code']
    acttion = [make_refund_accepted]
    
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)

