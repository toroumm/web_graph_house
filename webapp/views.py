# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import json, os
# Create your views here.


def view_get_example(request):

    return render(request, 'webapp/example.html')

def view_get_json(request):

    with open('webapp/templates/webapp/readme.json') as jo:
        arquivo = json.load(jo)

    return JsonResponse(arquivo)#render(request,'webapp/example.html')