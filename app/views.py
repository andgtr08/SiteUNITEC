"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import *
from datetime import datetime

def index(request):
    return render(request, "index.html")

def restrito(request):
    return render(request, "restrito.html")

def ListaCurso(request):
    return render(request, "ListaCursos.html")
