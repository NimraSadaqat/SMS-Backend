from django.contrib import admin
from employees.models import EmployeeInformation, Salary

# Register your models here.
@admin.register(EmployeeInformation)
class EmployeeInformationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmployeeInformation._meta.local_fields]
    search_fields = ('name','cell_number', 'qualification')

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
    
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Salary._meta.local_fields]
    search_fields = ('employee', 'salary')

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
