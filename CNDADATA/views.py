# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
class DisableCSRFCheck(object):
    """
    屏蔽csrf验证
    """
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)



def index(req):

    return render_to_response('index1.html')
def update(req):

    return render_to_response('update.html')

def index1(req):
    return render_to_response('index1.html')