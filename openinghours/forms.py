"""Editing form for opening hours

Front-end untrusted end user grade UX aimed at business directory sites.

UX supports up to two sets of opening hours per day optimised for common stories:
nine till five, closed for lunch, open till late, saturday morning-closed on sunday
"""

from django import forms
from datetime import time

def time_choices():
    """Return digital time choices every half hour from 00:00 to 23:30."""
    hours = list(range(0,24))
    times = []
    for h in hours:
        hour = str(h).zfill(2)
        times.append(hour+':00')
        times.append(hour+':30')
    return list(zip(times, times))

TIME_CHOICES = time_choices()

class Slot(forms.Form):
    from_hour = forms.ChoiceField(choices=TIME_CHOICES)
    to_hour   = forms.ChoiceField(choices=TIME_CHOICES)
