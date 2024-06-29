from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Street
from .resources import StreetResource

@admin.register(Street)
class StreetAdmin(ImportExportModelAdmin):
    resource_class = StreetResource
