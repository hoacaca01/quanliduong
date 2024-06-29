from import_export import resources
from .models import Street

class StreetResource(resources.ModelResource):
    class Meta:
        model = Street
        # fields = ('stt', 'name', 'category', 'description', 'importance_level', 'significance', 'longitude', 'latitude')
