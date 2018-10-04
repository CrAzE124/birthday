from django.forms import ModelForm
from .models import Birthday

class BirthdayForm(ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'