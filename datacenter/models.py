from django.db import models
import django
from django.utils.timezone import activate

import datetime, time
from datetime import timedelta

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
    
    def get_duration(visit):
        enter = django.utils.timezone.localtime(visit.entered_at, timezone=None)
        out = django.utils.timezone.localtime(visit.leaved_at, timezone=None)
        delta = out - enter 
        return delta

    def is_long(visit, minutes=60):
        delta = visit.get_duration()
        total_minutes = int(delta.total_seconds()//60)    
        return total_minutes>=minutes
        
    def format_duration(visit):
        duration = visit.get_duration()
        minutes = (duration.total_seconds()%3600)//60
        hours = duration.total_seconds()//3600
        formatted_duration = f"{hours} ч {minutes} мин"   
        return formatted_duration
