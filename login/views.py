# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse

class DisableCSRFCheck(object):
    """
    屏蔽csrf验证
    """
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
# Create your views here.
def login(request):
    return render(request, 'back/dashboard/main/login.html')

# def loginaction(request):
#     '''
#     用户登陆验证
#     :param request:
#     :return:
#     '''
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username = username, password = password)  #作为用户认证，可以用来判断用户是否已经登陆
#     if user is not None:
#         if user.is_active:
#             auth.login(request, user)
#             return render(request, 'back/dashboard/main/main.html')
#         else:
#             pass
#     else:
#         pass

def loginsuccess(request):
    '''
    登陆成功
    :param request:
    :return:
    '''
    if request.user.is_authenticated():
        print request.user.username
        return render(request, 'back/dashboard/main/main.html')  #允许用户多次登陆
    else:
        return render(request, 'back/dashboard/main/login.html')

@csrf_exempt
def tableview(request):
    '''
    跳转到特定网页的通用方法
    :param request:
    :return:
    '''
    area = request.POST.get('area', '')   #获取POST参数
    t = loader.get_template(area)
    output = t._render(1)   #词句一定要加入，不然html格式会不对,参数1
    return HttpResponse(output)




