# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response

# Create your views here.
def test(req):
    return render_to_response('index.html')