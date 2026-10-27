from django.contrib import admin
from fitness.models import Client, Trainer, TrainingSession

# Register your models here.

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email')
    list_filter = ('specialization',)
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'joined_date')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('client', 'trainer', 'session_date')
    list_filter = ('trainer', 'session_date')
    search_fields = ('client__first_name', 'client__last_name', 'trainer__first_name', 'trainer__last_name')