from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import Visit

from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
import datetime, time


def storage_information_view(request):
    
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        duration = visit.get_duration()
        is_strange = visit.is_long()
    
        non_closed_visits.append(
            {
                "who_entered": visit.passcard,
                "entered_at": visit.entered_at,
                "duration": duration,
                'is_strange':  is_strange
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
