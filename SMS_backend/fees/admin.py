from django.db import models
from django.contrib import admin
from fees.models import Fees, StudentFee, FeeReceipt, StudentFeeReceipt
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.

admin.site.register(StudentFeeReceipt)

class student_feesInline(admin.TabularInline):
    model = FeeReceipt.student_fees.through

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Fees._meta.local_fields]
    search_fields = ('academic_year', 'type', 'amount')

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

@admin.register(StudentFee)
class StuddentFeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentFee._meta.local_fields]
    search_fields = ('status', 'student', 'fee')

    def has_delete_permission(self, request, obj=None):
        # Only allow superuser to delete instances
        if request.user.is_superuser:
            return True
        return False

@admin.register(FeeReceipt)
class FeeReceiptAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FeeReceipt._meta.local_fields]
    # search_fields = ('status', 'student', 'fee')
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('verbose name', is_stacked=False)},
    }

    inlines = [student_feesInline]
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)

    #     # Access the Many-to-Many field
    #     tags = form.cleaned_data['student_fees']  # Assuming 'tags' is the name of the Many-to-Many field in the form

    #     # Add related tags to the Many-to-Many field
    #     obj.student_fees.set(tags)
    #     print('obj in admin:', obj.student_fees)

    # def has_delete_permission(self, request, obj=None):
        # Only allow superuser to delete instances
        # if request.user.is_superuser:
            # return True
        # return False

