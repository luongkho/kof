from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.urls import reverse
from django.template.loader import render_to_string

from django.db import IntegrityError, DatabaseError, connection

from .models import *


# Create your views here.
def fighters(request):
    # Get all filters
    quality = 0
    if request.method == 'GET':
        quality = request.GET.get('quality', quality)
        quality = int(quality)
        if 16 > quality > 10:
            filter_fighters = Fighter.objects.filter(quality=quality)
        else:
            filter_fighters = Fighter.objects.all()
            quality = 0
    else:
        filter_fighters = Fighter.objects.all()

    # Build response
    filter = {
        'quality': list(Fighter.objects.values('quality').order_by('quality').distinct())
    }
    chosen = {
        'quality': quality
    }

    # Return data
    if request.GET.get('ajax', False):
        html = ''
        for fighter in filter_fighters:
            html += render_to_string('kof/fighter.html', {'fighter': fighter})
        data_response = {'filter': filter, 'chosen': chosen, 'html': html}
        return JsonResponse({'status': True, 'data': data_response})
    else:
        data_response = {'filter': filter, 'chosen': chosen, 'fighters': filter_fighters}
        return render(request, 'kof/fighters.html', data_response)
