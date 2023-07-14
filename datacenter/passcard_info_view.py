from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = get_list_or_404(Visit,passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        formatted_duration = visit.format_duration()
        is_strange = visit.is_long()
            
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': formatted_duration,
                'is_strange': is_strange
            },
        )    
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

   