from django.contrib import admin
from students.models import Student, FamilyInformation
# Register your models here.

@admin.register(FamilyInformation)
class FamilyInformationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FamilyInformation._meta.local_fields]
    search_fields = ('father_nic_number', 'father_name', 'father_cell_number')

    def has_delete_permission(self, request, obj=None):
        # Only allow superuser to delete instances
        if request.user.is_superuser:
            return True
        return False

@admin.register(Student)
class StuddentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.local_fields]
    search_fields = ('name', 'admission_number')

    def has_delete_permission(self, request, obj=None):
        # Only allow superuser to delete instances
        if request.user.is_superuser:
            return True
        return False
