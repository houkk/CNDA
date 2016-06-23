#-*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from login import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', views.login),   #相当于第二个login  http://127.0.0.1:8080/login/login(this)
    #url(r'^loginaction/$', login, {'template_name':'back/dashboard/main/main.html'})
    url(r'^loginaction/$', login, {'template_name':'back/dashboard/main/login.html','extra_context':{'error_message':'该账户不存在，请重新输入- -|||'}}), #login函数接受2个参数，template_name 代表登陆不成功返回的界面；extra_context的value是一个字典格式，带回登陆不成功的消息
    url(r'^loginsuccess/$', views.loginsuccess),                                                                                                        #还有一个参数杂是setting里面的LOGIN_REDIRECT_URL，代表成功以后跳转的页面,默认是 /account/profile
    url(r'^tableview/$', views.tableview),
    url(r'^logoutview/$', logout, {'template_name':'back/dashboard/main/login.html'})     #退出登陆状态，删除session 里面的个人信息，然后跳转到登陆界面
)
