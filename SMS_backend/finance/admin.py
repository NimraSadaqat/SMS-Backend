from django.contrib import admin
from finance.models import Expenses, MonthlyIncome, Default
# Register your models here.

@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Expenses._meta.local_fields]
    search_fields = ('description','amount', 'created_at')

    def has_delete_permission(self, request, obj=None):
        # Only allow superuser to delete instances
        if request.user.is_superuser:
            return True
        return False

@admin.register(MonthlyIncome)
class MonthlyIncomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MonthlyIncome._meta.local_fields]

    def has_change_permission(self, request, obj=None):
        # Only allow superuser to update information
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        # Only allow superuser to delete instances
        if request.user.is_superuser:
            return True
        return False

@admin.register(Default)
class DefaultAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Default._meta.local_fields]

    def has_change_permission(self, request, obj=None):
        # Only allow superuser to update information
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        # Only allow superuser to delete instances
        if request.user.is_superuser:
            return True
        return False

