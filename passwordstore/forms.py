from .models import Passwordstore
from django.forms import ModelForm

class PasswordstoreForm(ModelForm):
    class Meta:
        model = Passwordstore
        fields ='__all__'