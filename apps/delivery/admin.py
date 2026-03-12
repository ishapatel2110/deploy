from django.contrib import admin

from .models import DeliveryAssignment, DeliveryLocationPing


@admin.register(DeliveryAssignment)
class DeliveryAssignmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_boy', 'accepted_at', 'started_at', 'delivered_at')


@admin.register(DeliveryLocationPing)
class DeliveryLocationPingAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'latitude', 'longitude', 'created_at')
