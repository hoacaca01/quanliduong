from django.contrib import admin
from .models import Street

admin.site.register(Street)

# from import_export import resources
# from import_export.admin import ImportExportModelAdmin
#
# class StreetResource(resources.ModelResource):
#     class Meta:
#         model = Street
#
# @admin.register(Street)
# class StreetAdmin(ImportExportModelAdmin):
#     resource_class = StreetResource