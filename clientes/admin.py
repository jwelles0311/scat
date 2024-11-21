from django.contrib import admin
from . import models
# Register your models here.

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('corporate_reason', 'address', 'number', 'contact', 'phone', 'cell', )
    search_fields = ('corporate_reason',)

admin.site.register(models.Companies, CompaniesAdmin)