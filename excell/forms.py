
from django import forms
from .models import PartnerFile

class PartnerFileForm(forms.ModelForm):
    class Meta:
        model=PartnerFile
        fields=['file_name',]
