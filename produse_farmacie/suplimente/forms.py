from django.forms import ModelForm
from .models import Medicamente

class MedicamenteForm(ModelForm):
    class Meta:
        model = Medicamente
        fields = '__all__'