from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.birthday, name='birthday'),
    path('rsvp/<int:event_id>', views.rsvp, name='rsvp')
]
