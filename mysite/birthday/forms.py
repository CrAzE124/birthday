from django.forms import ModelForm, DateTimeField
from .models import Birthday, RSVP

class BirthdayForm(ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'


class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        exclude = ['celebration']