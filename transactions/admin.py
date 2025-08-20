from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'transaction_type', 'date', 'notes']
    list_filter = ['transaction_type', 'date']
    search_fields = ['description', 'notes']
    date_hierarchy = 'date'
    ordering = ['-date']
    readonly_fields = ['date']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ['date']
        return []  # Creating a new object
