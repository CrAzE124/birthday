from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Birthday, RSVP, REFRESHMENT_CHOICES
from .forms import BirthdayForm, RSVPForm


# Create your views here.
def index(req):
    return render(req, 'birthday/index.html', {})


def birthday(req):
    if req.method == 'POST':
        form = BirthdayForm(req.POST)

        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/birthday/events')
    else:
        form = BirthdayForm()
    
    birthdays = Birthday.objects.all()

    return render(req, 'birthday/birthday.html', {
        'form': form,
        'birthdays': birthdays,
        'refreshment_choices': REFRESHMENT_CHOICES
    })


def rsvp(req, event_id):
    if req.method == 'POST':
        form = RSVPForm(req.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.celebration_id = event_id

            instance.save()

            return HttpResponseRedirect('/birthday/events')
    else:
        form = RSVPForm()

    birthday = get_object_or_404(Birthday, pk=event_id)
    rsvps = RSVP.objects.filter(celebration_id=event_id)

    return render(req, 'birthday/rsvp.html', {
        'form': form,
        'birthday': birthday,
        'rsvps': rsvps
    })