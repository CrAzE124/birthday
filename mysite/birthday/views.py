from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Birthday, RSVP, REFRESHMENT_CHOICES
from .forms import BirthdayForm

# Create your views here.
def index(req):
    return HttpResponse('hello world')

def birthday(req):
    if req.method == 'POST':
        form = BirthdayForm(req.POST)

        form.save()
    
    birthdays = Birthday.objects.all()

    return render(req, 'birthday/birthday.html', {
        'birthdays': birthdays,
        'refreshment_choices': REFRESHMENT_CHOICES
    })

def rsvp(req, event_id):
    birthday = get_object_or_404(Birthday, pk=event_id)
    rsvps = RSVP.objects.filter(birthday=event_id)

    return render(req, 'birthday/rsvp.html', {
        'birthday': birthday,
        'rsvps': rsvps
    })