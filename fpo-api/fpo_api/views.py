
import json
import os
from django.http import HttpResponse
from django.shortcuts import render
from api.models.User import User

def health(request):
    """
    Health check for OpenShift
    """
    return HttpResponse(User.objects.count())

