from email.mime import image
import imp
from django import forms
from. models import Vendor
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name','vendor_license']