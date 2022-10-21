from import_export import resources
from .models import Partner

class PartnerResource(resources.ModelResource):
    class Meta:
        model = Partner