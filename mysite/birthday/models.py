from django.db import models

REFRESHMENT_CHOICES = (
    ('tea_biscuits', 'Tea & Biscuts'),
    ('finger_lunch', 'Finger Lunch'),
    ('sit_down', 'Sit Down Lunch'),
)

# Create your models here.
class Birthday(models.Model):
    name = models.CharField(max_length=255)
    birthday_message = models.TextField()
    date = models.DateTimeField()
    duration = models.IntegerField()
    venue = models.CharField(max_length=255)
    refreshment = models.CharField(max_length=255, choices=REFRESHMENT_CHOICES)
    scheduler_name = models.CharField(max_length=255)
    scheduler_email = models.EmailField(max_length=255)
    scheduler_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class RSVP(models.Model):
    rsvp_name = models.CharField(max_length=255)
    rsvp_email = models.EmailField(max_length=255)
    rsvp_number = models.CharField(max_length=10)
    having_refreshments = models.BooleanField()
    celebration = models.ForeignKey(to=Birthday, on_delete=models.CASCADE)

    def __str__(self):
        return self.rsvp_name