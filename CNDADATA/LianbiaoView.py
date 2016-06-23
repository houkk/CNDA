# -*- coding: utf-8 -*-
import random
import re
import simplejson
from LianBiaoSerializer import *
from models import *
from filter import *
from rest_framework import viewsets
from LianBiaoFilter import *
from rest_framework import generics
import datetime
from django.db.models import Q
from rest_framework_bulk import BulkCreateModelMixin, BulkUpdateModelMixin, BulkModelViewSet
import time

class TbHospitaldoctorrelliaobiaoViewSet(BulkUpdateModelMixin, BulkCreateModelMixin, viewsets.ModelViewSet):
    """
    医院医生关系表
    """
    queryset = TbHospitaldoctorrel.objects.all()
    serializer_class = TbHospitaldoctorrellianbiaoSerializer
    filter_class = TbHospitaldoctorrelFilter




class DoctorviewViewset(viewsets.ReadOnlyModelViewSet):
    """
    中医专家信息视图
    """
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    #queryset = Doctorview.objects.all()
    serializer_class = DoctorviewSerializer
    filter_class = DoctorviewFilter
    def get_queryset(self):
        if self.request._request.GET:
            if self.request._request.GET['id']:
                inputid = self.request._request.GET['id']
                inputid1 = inputid.replace('[', '')
                inputid2 = inputid1.replace(']', '')
                inputid3 = inputid2.replace('{', '')
                inputid4 = inputid3.replace('}', '')
                if inputid4:
                    order = inputid4.split(",")
                else:
                    order = []
                return Doctorview.objects.filter(doctorid__in=order)
            return Doctorview.objects.all()
        return Doctorview.objects.all()

class UserhealthknowledgeViewset(viewsets.ReadOnlyModelViewSet):
    """
    个人养生知识视图
    """
    queryset = Userhealthknowledge.objects.all()
    serializer_class = UserhealthknowledgeSerializer
    filter_class = UserhealthknowledgeFilter


class userhealthknowledge(generics.ListAPIView):

    serializer_class = UserhealthknowledgeSerializer
    def get_queryset(self):
        healthknowltypename = self.kwargs['healthknowltypename']
        return Userhealthknowledge.objects.filter(healthknowltypename__contains=healthknowltypename).order_by('-userknowledgemappid')[0:1]
class TbTcmhealthknowledgedate(generics.ListAPIView):
    serializer_class = TbTcmhealthknowledgeSerializer
    def get_queryset(self):
        down = self.kwargs['down']
        up = self.kwargs['up']
        return TbTcmhealthknowledge.objects.filter(exersuggtime__gte=down, exersuggtime__lte=up)
class TbSportinforecordsSeven(BulkUpdateModelMixin, BulkCreateModelMixin, viewsets.ModelViewSet):

    serializer_class = TbSportinforecordsSerializer
    filter_class = TbSportinforecordsFilter
    #lookup_field = 'temp_userid'
    def get_queryset(self):

        data = TbSportinforecords.objects.all().order_by('-sportrecorduptime')[0:1]
        nearbytime = data[0].sportrecorduptime
        nearbydate = datetime.datetime.strptime(datetime.date.strftime(nearbytime, '%Y-%m-%d'), '%Y-%m-%d')

        downdate = nearbydate-datetime.timedelta(days=6)
        downdatestring = datetime.date.strftime(downdate, '%Y-%m-%d')
        update = nearbydate+datetime.timedelta(days=1)
        realdata = TbSportinforecords.objects.filter(sportrecorduptime__gte=downdate, sportrecorduptime__lte=update)
        if realdata:
            return realdata
        else:
            return ''
    """
import time
class TbSportinforecordsSeven(viewsets.ModelViewSet):
    """
    #记录用户运动数据
    """
    data = TbSportinforecords.objects.all().order_by('-sportrecorduptime')[0:1]
    nearbytime = data[0].sportrecorduptime
    nearbydate = datetime.datetime.strptime(datetime.date.strftime(nearbytime, '%Y-%m-%d'), '%Y-%m-%d')
    downdate = nearbydate-datetime.timedelta(days=100)
    update = nearbydate+datetime.timedelta(days=1)
    realdata = TbSportinforecords.objects.filter(sportrecorduptime__gte=downdate, sportrecorduptime__lte=update)
    queryset = realdata
    serializer_class = TbSportinforecordsSerializer
    filter_class = TbSportinforecordsFilter
    def get_queryset(self):

        userid = self.kwargs['userid']
        data = TbSportinforecords.objects.all().order_by('-sportrecorduptime')[0:1]
        #data = TbSportinforecords.objects.filter(temp_userid=userid).order_by('-sportrecorduptime')[0:1]
        # data = random.sample(TbSportinforecords.objects.filter(temp_userid=userid), 7)
        # result = [TbSportinforecords.objects.filter(temp_userid=userid)[i] for i in data]
        nearbytime = data[0].sportrecorduptime
        print nearbytime

        nearbydate = datetime.datetime.strptime(datetime.date.strftime(nearbytime, '%Y-%m-%d'), '%Y-%m-%d')
        print nearbydate
        downdate = nearbydate-datetime.timedelta(days=6)
        print downdate
        update = nearbydate+datetime.timedelta(days=1)
        print update
        realdata = TbSportinforecords.objects.filter(sportrecorduptime__gte=downdate, sportrecorduptime__lte=update)
        if realdata:
            return realdata
        else:
            return ''
        #print data.sportrecorduptime
    """
class TbHealthtrendrecordsLianbiaoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    记录用户健康趋势
    """
    queryset = TbHealthtrendrecords.objects.all()
    serializer_class = TbHealthtrendrecordsLianbiaoSerializer
    filter_class = TbHealthtrendrecordsFilter

class TbConstituteidentifyresultCombineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    体质辨识结果记录表
    """
    queryset = TbConstituteidentifyresult.objects.all()
    serializer_class = TbConstituteidentifyresultCombineSerializer
    filter_class = TbConstituteidentifyresultFilter

class personaltuijian(viewsets.ReadOnlyModelViewSet):
    """
    记录中医养生知识发布细节，个人推荐，前台
    """
    #queryset = TbTcmhealthknowledge.objects.all()
    serializer_class = TbTcmhealthknowledgeSerializer
    filter_class = TbTcmhealthknowledgeFilter
    def get_queryset(self):
        if self.request._request.GET:
            filtercontent = self.request._request.GET['filtercontent']
            filterdata = TbTcmhealthknowledge.objects.filter(Q(healthknowledgetitle__contains=filtercontent) | Q(healthknowledgecontent__contains=filtercontent)).order_by('-exersuggtime')
            return filterdata
        return TbTcmhealthknowledge.objects.all()

class TbHospitalinfoCombineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    医院信息表
    """
    queryset = TbHospitalinfo.objects.all()
    serializer_class = TbHospitalinfoCombineSerializer
    filter_class = Tbhospitalinfocombinefilter


class TbSetmealfoodmappcombineViewset(viewsets.ReadOnlyModelViewSet):
    """
    套餐食物映射表
    """
    queryset = TbSetmealfoodmapp.objects.all()
    serializer_class = TbSetmealfoodmappcombineSerializer
    filter_class = TbSetmealfoodmappFiler



class TbSleepinforecordscombineViewSet(BulkUpdateModelMixin, BulkCreateModelMixin, viewsets.ModelViewSet):
    """
    记录用户睡眠信息
    """
    paginate_by = 10
    queryset = TbSleepinforecords.objects.all()
    serializer_class = TbSleepinforecordscombineSerializer
    filter_class = TbSleepinforecordsFilter

# class TbHealthsuggestlimitedCombineViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
#     """
#     健康建议限定条件表
#     """
#     #queryset = TbHealthsuggestlimited.objects.all()
#     serializer_class = TbHealthsuggestlimitedCombineSerializer
#     filter_class = TbHealthsuggestlimitedFilter
#
#     def get_queryset(self):
#         alldata = []
#         singledata = {}
#         if self.request._request.GET:
#             temp_userid = self.request._request.GET['temp_userid']
#             suggestlimitedvalue = self.request._request.GET['suggestlimitedvalue']
#             suggestlimitedattrname = self.request._request.GET['suggestlimitedattrname']
#
#             filterdatas = TbHealthsuggestlimited.objects.filter(
#                 suggestlimitedvalue=suggestlimitedvalue,
#                 suggestlimitedattrname=suggestlimitedattrname
#             )
#             if filterdatas:
#                 for filterdata in filterdatas:
#                     if filterdata.temp_healthsuggestid:
#                         singledata['healthsuggcontent'] = filterdata.temp_healthsuggestid.healthsuggestcontent
#                         singledata['temp_userid'] = temp_userid
#                         singledata['temp_healthsuggestid'] = filterdata.temp_healthsuggestid.healthsuggestid
#                         singledata['healthsuggestreason'] = filterdata.suggestlimitedexplain
#                         singledata['healthsuggesttime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#                         singledata['healthsuggestremarks'] = filterdata.temp_healthsuggestid.healthsuggestremarks
#
#                         alldata.append(singledata)
#                 serializer = TbHealthsuggestionsmappSerializer(data=alldata, many=True)
#                 if serializer.is_valid():
#                     serializer.save()
#         return TbHealthsuggestlimited.objects.all()
class TbRecommendedconditionsmappCombineidViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康建议条件限定映射表
    """
    #queryset = TbRecommendedconditionsmapp.objects.all()
    serializer_class = TbRecommendedconditionsmappcombineSerializer
    filter_class = TbRecommendedconditionsmappcombineFilter
    def get_queryset(self):
        if self.request._request.GET:
            if self.request._request.GET['id']:
                inputid = self.request._request.GET['id']
                print inputid
                inputid1 = inputid.replace('[', '')
                inputid2 = inputid1.replace(']', '')
                inputid3 = inputid2.replace('{', '')
                inputid4 = inputid3.replace('}', '')
                if inputid4:
                    order = inputid4.split(",")
                else:
                    order = []
                return TbRecommendedconditionsmapp.objects.filter(recommendedconditionsmappid__in=order)
            return TbRecommendedconditionsmapp.objects.all()
        return TbRecommendedconditionsmapp.objects.all()
class TbRecommendedconditionsmappCombineViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康建议条件限定映射表
    """
    queryset = TbRecommendedconditionsmapp.objects.all()
    serializer_class = TbRecommendedconditionsmappcombineSerializer
    filter_class = TbRecommendedconditionsmappcombineFilter
