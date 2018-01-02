from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.urls import reverse

from django.db import IntegrityError, DatabaseError, connection

from .models import *


# Create your views here.
def fighters(request):
    return HttpResponse("Hello there!")
