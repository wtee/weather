from django.contrib import admin
from cancellations.models import Cancellation
from cancellations.models import Organization

class CancelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['cancel_date', 'type_of_cancel', 'details']}),
        (None, {'fields': ['organization']}),
    ]

class OrgAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['org_name', 'address']}),
    ]
  
admin.site.register(Cancellation, CancelAdmin)
admin.site.register(Organization, OrgAdmin)
