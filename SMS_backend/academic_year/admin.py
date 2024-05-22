from django.contrib import admin
from academic_year.models import Academic_Year

# Register your models here.
@admin.register(Academic_Year)
class Academic_Year_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Academic_Year._meta.local_fields]
    search_fields = ('grade', 'monthly_fees', 'start_date')

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
