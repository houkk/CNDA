# -*- coding: utf-8 -*-
import decimal
from django.core.paginator import Paginator
from rest_framework.settings import api_settings
import simplejson
from models import *
from filter import *
from serializers import *
from specialdatatwo import *
from rest_framework import viewsets
from rest_framework_bulk import BulkModelViewSet
from django.db.models import Sum, Avg, Max
import datetime
from django.shortcuts import HttpResponse
from django.core.serializers import serialize

def TbSportspecial(request):
    teminal = None
    result = {}
    riqi = [6, 5, 4, 3, 2, 1, 0, -1]
    cishu = [6, 5, 4, 3, 2, 1, 0]
    alldata = []
    walkstepnumberaverage = 0
    walkstepnumberfrequency = 0
    runstepnumberaverage = 0
    runstepnumberfrequency = 0
    walkdistanceaverage = 0
    walkdistancefrequency = 0
    rundistanceaverage = 0
    rundistancefrequency = 0
    calorieconsumptionaverage = 0
    calorieconsumptionfrequency = 0
    restingcalorieconsumeaverage = 0
    restingcalorieconsumefrequency = 0
    movecalorieconsumeaverage = 0
    movecalorieconsumefrequency = 0
    crawledflooraverage = 0
    crawledfloorfrequency = 0
    fallitemsaverage = 0
    fallitemsfrequency = 0
    activedurationaverage = 0
    activedurationfrequency = 0
    #longestactivedurationaverage = 0
    #longestactivedurationfrequency = 0
    #longestidledurationaverage = 0
    #longestidledurationfrequency = 0
    singledata = {}
    if request.method == "GET":
        temp_userid = request.GET.get('temp_userid')
        querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m-%d')
        singledata['temp_userid'] = temp_userid
        #data = TbSportinforecords.objects.all().order_by('-sportovertime')[0:1]
        #nearbytime = data[0].sportovertime
        #today = datetime.datetime.strptime(datetime.date.strftime(str(querytime), '%Y-%m-%d'), '%Y-%m-%d')
        try:
            for i in range(len(cishu)):
                down = querytime-datetime.timedelta(days=riqi[i])
                up = querytime-datetime.timedelta(days=riqi[i+1])
                summ = TbSportinforecords.objects.filter(
                    temp_userid=temp_userid,
                    sportovertime__gte=down,
                    sportovertime__lte=up
                ).aggregate(
                    walkdistance=Sum('walkdistance'),
                    walkstepnumber=Sum('walkstepnumber'),
                    runstepnumber=Sum('runstepnumber'),
                    rundistance=Sum('rundistance'),
                    calorieconsumption=Sum('calorieconsumption'),

                    restingcalorieconsume=Sum('restingcalorieconsume'),
                    movecalorieconsume=Sum('movecalorieconsume'),
                    crawledfloor=Sum('crawledfloor'),
                    fallitems=Sum('fallitems'),
                    activeduration=Sum('activeduration'),
                    longestactiveduration=Max('longestactiveduration'),
                    longestidleduration=Max('longestidleduration')

                )
                if summ['walkstepnumber']:
                    singledata['walkstepnumber'] = summ['walkstepnumber']
                    walkstepnumberaverage += summ['walkstepnumber']
                    walkstepnumberfrequency += 1
                else:
                    singledata['walkstepnumber'] = 0
                    walkstepnumberaverage += 0
                    walkstepnumberfrequency += 0
                if summ['restingcalorieconsume']:
                    singledata['restingcalorieconsume'] = summ['restingcalorieconsume']
                    restingcalorieconsumeaverage += summ['restingcalorieconsume']
                    restingcalorieconsumefrequency += 1
                else:
                    singledata['restingcalorieconsume'] = 0
                    restingcalorieconsumeaverage += 0
                    restingcalorieconsumefrequency += 0
                if summ['movecalorieconsume']:
                    singledata['movecalorieconsume'] = summ['movecalorieconsume']
                    movecalorieconsumeaverage += summ['movecalorieconsume']
                    movecalorieconsumefrequency += 1
                else:
                    singledata['movecalorieconsume'] = 0
                    movecalorieconsumeaverage += 0
                    movecalorieconsumefrequency += 0
                if summ['crawledfloor']:
                    singledata['crawledfloor'] = summ['crawledfloor']
                    crawledflooraverage += summ['crawledfloor']
                    crawledfloorfrequency += 1
                else:
                    singledata['crawledfloor'] = 0
                    crawledflooraverage += 0
                    crawledfloorfrequency += 0
                if summ['fallitems']:
                    singledata['fallitems'] = summ['fallitems']
                    fallitemsaverage += summ['fallitems']
                    fallitemsfrequency += 1
                else:
                    singledata['fallitems'] = 0
                    fallitemsaverage += 0
                    fallitemsfrequency += 0
                if summ['activeduration']:
                    singledata['activeduration'] = summ['activeduration']
                    activedurationaverage += summ['activeduration']
                    activedurationfrequency += 1
                else:
                    singledata['activeduration'] = 0
                    activedurationaverage += 0
                    activedurationfrequency += 0
                if summ['longestactiveduration']:
                    singledata['longestactiveduration'] = summ['longestactiveduration']
                else:
                    singledata['longestactiveduration'] = 0
                if summ['longestidleduration']:
                    singledata['longestidleduration'] = summ['longestidleduration']
                else:
                    singledata['longestidleduration'] = 0
                if summ['runstepnumber']:
                    singledata['runstepnumber'] = summ['runstepnumber']
                    runstepnumberaverage += summ['runstepnumber']
                    runstepnumberfrequency += 1
                else:
                    singledata['runstepnumber'] = 0
                    runstepnumberaverage += 0
                    runstepnumberfrequency += 0
                if summ['walkdistance']:
                    singledata['walkdistance'] = summ['walkdistance']
                    walkdistanceaverage += summ['walkdistance']
                    walkdistancefrequency += 1
                else:
                    singledata['walkdistance'] = 0
                    walkdistanceaverage += 0
                    walkdistancefrequency += 0
                if summ['rundistance']:
                    singledata['rundistance'] = summ['rundistance']
                    rundistanceaverage += summ['rundistance']
                    rundistancefrequency += 1
                else:
                    singledata['rundistance'] = 0
                    rundistanceaverage += 0
                    rundistancefrequency += 0
                if summ['calorieconsumption']:
                    singledata['calorieconsumption'] = summ['calorieconsumption']
                    calorieconsumptionaverage += summ['calorieconsumption']
                    calorieconsumptionfrequency += 1
                else:
                    singledata['calorieconsumption'] = 0
                    calorieconsumptionaverage += 0
                    calorieconsumptionfrequency += 0
                singledata['sporttime'] = datetime.date.strftime(down, '%Y-%m-%d')
                alldata.append(singledata.copy())
            if walkstepnumberfrequency == 0:
                walkstepnumberaverage = 0
                walkdistanceaverage = 0
            else:
                walkstepnumberaverage = walkstepnumberaverage/walkstepnumberfrequency
                walkdistanceaverage = walkdistanceaverage/walkdistancefrequency
            if runstepnumberfrequency == 0:
                runstepnumberaverage = 0
                rundistanceaverage = 0
            else:
                runstepnumberaverage = runstepnumberaverage/runstepnumberfrequency
                rundistanceaverage = rundistanceaverage/rundistancefrequency
            if calorieconsumptionfrequency == 0:
                calorieconsumptionaverage = 0
            else:
                calorieconsumptionaverage = calorieconsumptionaverage/calorieconsumptionfrequency
            if restingcalorieconsumefrequency == 0:
                restingcalorieconsumeaverage = 0
            else:
                restingcalorieconsumeaverage = restingcalorieconsumeaverage/restingcalorieconsumefrequency
            if movecalorieconsumefrequency == 0:
                movecalorieconsumeaverage = 0
            else:
                movecalorieconsumeaverage = movecalorieconsumeaverage/movecalorieconsumefrequency
            if crawledfloorfrequency == 0:
                crawledflooraverage = 0
            else:
                crawledflooraverage = crawledflooraverage/crawledfloorfrequency
            if fallitemsfrequency == 0:
                fallitemsaverage = 0
            else:
                fallitemsaverage = fallitemsaverage/fallitemsfrequency
            if activedurationfrequency == 0:
                activedurationaverage = 0
            else:
                activedurationaverage = activedurationaverage/activedurationfrequency
            result['alldata'] = alldata
            result['walkstepnumberaverage'] = walkstepnumberaverage
            result['walkdistanceaverage'] = round(walkdistanceaverage, 2)
            result['runstepnumberaverage'] = runstepnumberaverage
            result['rundistanceaverage'] = round(rundistanceaverage, 2)
            result['calorieconsumptionaverage'] = round(calorieconsumptionaverage, 2)
            result['restingcalorieconsumeaverage'] = round(restingcalorieconsumeaverage, 2)
            result['movecalorieconsumeaverage'] = round(movecalorieconsumeaverage, 2)
            result['crawledflooraverage'] = crawledflooraverage
            result['fallitemsaverage'] = fallitemsaverage
            result['activedurationaverage'] = round(activedurationaverage, 1)

            # print "walkdistanceaverage", walkdistanceaverage
            # print "runstepnumberaverage", runstepnumberaverage
            # print "rundistanceaverage", rundistanceaverage
            # print "calorieconsumptionaverage", calorieconsumptionaverage
            # print "walkstepnumberaverage", walkstepnumberaverage
            teminal = simplejson.dumps(result)
        except Exception as e:
            teminal = e.message
    else:
        teminal = False
    return HttpResponse(teminal)


def sportsingle(request):
    result = {}
    alldata = []
    singledata = {}
    terminal = None
    if request.method == 'GET':
        if request.GET.get("temp_userid") and request.GET.get("querytime"):
            try:
                userid = request.GET.get("temp_userid")
                querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m-%d')
                nexttime = querytime+datetime.timedelta(days=1)
                summ = TbSportinforecords.objects\
                    .filter(
                        temp_userid=userid,
                        sportovertime__gte=querytime,
                        sportovertime__lte=nexttime
                    )\
                    .aggregate(
                        walkdistance=Sum('walkdistance'),
                        walkstepnumber=Sum('walkstepnumber'),
                        runstepnumber=Sum('runstepnumber'),
                        rundistance=Sum('rundistance'),
                        calorieconsumption=Sum('calorieconsumption'),
                        restingcalorieconsume=Sum('restingcalorieconsume'),
                        movecalorieconsume=Sum('movecalorieconsume'),
                        crawledfloor=Sum('crawledfloor'),
                        fallitems=Sum('fallitems'),
                        activeduration=Sum('activeduration'),
                        longestactiveduration=Max('longestactiveduration'),
                        longestidleduration=Max('longestidleduration')
                    )
                if summ['walkdistance']:
                    result['walkdistance'] = summ['walkdistance']
                else:
                    result['walkdistance'] = 0
                if summ['walkstepnumber']:
                    result['walkstepnumber'] = summ['walkstepnumber']
                else:
                    result['walkstepnumber'] = 0
                if summ['runstepnumber']:
                    result['runstepnumber'] = summ['runstepnumber']
                else:
                    result['runstepnumber'] = 0
                if summ['rundistance']:
                    result['rundistance'] = summ['rundistance']
                else:
                    result['rundistance'] = 0
                if summ['calorieconsumption']:
                    result['calorieconsumption'] = summ['calorieconsumption']
                else:
                    result['calorieconsumption'] = 0
                if summ['restingcalorieconsume']:
                    result['restingcalorieconsume'] = summ['restingcalorieconsume']
                else:
                    result['restingcalorieconsume'] = 0
                if summ['movecalorieconsume']:
                    result['movecalorieconsume'] = summ['movecalorieconsume']
                else:
                    result['movecalorieconsume'] = 0
                if summ['crawledfloor']:
                    result['crawledfloor'] = summ['crawledfloor']
                else:
                    result['crawledfloor'] = 0
                if summ['fallitems']:
                    result['fallitems'] = summ['fallitems']
                else:
                    result['fallitems'] = 0
                if summ['activeduration']:
                    result['activeduration'] = summ['activeduration']
                else:
                    result['activeduration'] = 0
                if summ['longestactiveduration']:
                    result['longestactiveduration'] = summ['longestactiveduration']
                else:
                    result['longestactiveduration'] = 0
                if summ['longestidleduration']:
                    result['longestidleduration'] = summ['longestidleduration']
                else:
                    result['longestidleduration'] = 0
                result['querytime'] = datetime.date.strftime(querytime, '%Y-%m-%d')
                result['temp_userid'] = userid
                summ1 = TbSportinforecords.objects.filter(temp_userid=userid, sportovertime__gte=querytime, sportovertime__lte=nexttime).order_by('sportovertime')
                count = TbSportinforecords.objects.filter(temp_userid=userid, sportovertime__gte=querytime, sportovertime__lte=nexttime).order_by('sportovertime').count()
                i = 0
                if summ1:
                    result['sportbegintime'] = str(summ1[0].sportbegintime)
                    result['sportovertime'] = str(summ1[len(summ1)-1].sportovertime)
                    for summ11 in summ1:
                        singledata["sportbegintime"] = str(summ11.sportbegintime)
                        singledata["sportovertime"] = str(summ11.sportovertime)
                        singledata["sportanalysis"] = summ11.sportanalysis
                        if summ11.walkstepnumber:
                            singledata['walkstepnumber'] = summ11.walkstepnumber
                        else:
                            singledata['walkstepnumber'] = 0
                        alldata.append(singledata.copy())
                        if count > 1:
                            if i < count-1:
                                begintime = summ1[i].sportovertime
                                overtime = summ1[i+1].sportbegintime
                                if (overtime-begintime).seconds > 1:
                                    while (overtime-begintime).seconds > 3600:
                                        singledata["sportbegintime"] = str(begintime)
                                        singledata["sportovertime"] = str(begintime+datetime.timedelta(hours=1))
                                        singledata["sportanalysis"] = ''
                                        singledata['walkstepnumber'] = 0
                                        alldata.append(singledata.copy())
                                        begintime += datetime.timedelta(hours=1)
                                    else:
                                        singledata["sportbegintime"] = str(begintime)
                                        singledata["sportovertime"] = str(overtime)
                                        singledata["sportanalysis"] = ''
                                        singledata['walkstepnumber'] = 0
                                        alldata.append(singledata.copy())
                            i += 1
                result['alldata'] = alldata
                terminal = simplejson.dumps(result, ensure_ascii=False, encoding='UTF-8')
            except Exception as e:
                terminal = e.message
        else:
            terminal = None
    else:
        terminal = None
    return HttpResponse(terminal)

def sportall(request):

    alldata = []
    listjson = {}
    terminal = None
    if request.method == "GET":
        userid = request.GET.get("temp_userid")

        summ = TbSportinforecords.objects.extra(select={"overtime": "to_char(sportovertime, 'yyyy-mm-dd')"})\
            .filter(temp_userid=userid)\
            .values('overtime')\
            .order_by('overtime')\
            .annotate(
                walkdistance=Sum('walkdistance'),
                walkstepnumber=Sum('walkstepnumber'),
                runstepnumber=Sum('runstepnumber'),
                rundistance=Sum('rundistance'),
                calorieconsumption=Sum('calorieconsumption'),
                restingcalorieconsume=Sum('restingcalorieconsume'),
                movecalorieconsume=Sum('movecalorieconsume'),
                crawledfloor=Sum('crawledfloor'),
                fallitems=Sum('fallitems'),
                activeduration=Sum('activeduration'),
                longestactiveduration=Max('longestactiveduration'),
                longestidleduration=Max('longestidleduration')
            )
        for sum1 in summ:
            if sum1['walkdistance']:
                listjson['walkdistance'] = sum1['walkdistance']
            else:
                listjson['walkdistance'] = 0
            if sum1['walkstepnumber']:
                listjson['walkstepnumber'] = sum1['walkstepnumber']
            else:
                listjson['walkstepnumber'] = 0
            if sum1['runstepnumber']:
                listjson['runstepnumber'] = sum1['runstepnumber']
            else:
                listjson['runstepnumber'] = 0
            if sum1['rundistance']:
                listjson['rundistance'] = sum1['rundistance']
            else:
                listjson['rundistance'] = 0
            if sum1['calorieconsumption']:
                listjson['calorieconsumption'] = sum1['calorieconsumption']
            else:
                listjson['calorieconsumption'] = 0
            if sum1['restingcalorieconsume']:
                listjson['restingcalorieconsume'] = sum1['restingcalorieconsume']
            else:
                listjson['restingcalorieconsume'] = 0
            if sum1['movecalorieconsume']:
                listjson['movecalorieconsume'] = sum1['movecalorieconsume']
            else:
                listjson['movecalorieconsume'] = 0
            if sum1['crawledfloor']:
                listjson['crawledfloor'] = sum1['crawledfloor']
            else:
                listjson['crawledfloor'] = 0
            if sum1['fallitems']:
                listjson['fallitems'] = sum1['fallitems']
            else:
                listjson['fallitems'] = 0
            if sum1['activeduration']:
                listjson['activeduration'] = sum1['activeduration']
            else:
                listjson['activeduration'] = 0
            if sum1['longestactiveduration']:
                listjson['longestactiveduration'] = sum1['longestactiveduration']
            else:
                listjson['longestactiveduration'] = 0
            if sum1['longestidleduration']:
                listjson['longestidleduration'] = sum1['longestidleduration']
            else:
                listjson['longestidleduration'] = 0

            listjson['overtime'] = sum1['overtime']
            alldata.append(listjson.copy())
        terminal = simplejson.dumps(alldata)
    else:
        terminal = False
    return HttpResponse(terminal)
def sportallmon(request):

    alldata = []
    listjson = {}
    terminal = None
    if request.method == "GET":
        userid = request.GET.get("temp_userid")

        querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m').strftime('%Y-%m')
        summ = TbSportinforecords.objects.extra(select={"overtime": "to_char(sportovertime, 'yyyy-mm-dd')"})\
            .filter(temp_userid=userid, sportovertime__contains=querytime)\
            .values('overtime')\
            .order_by('overtime')\
            .annotate(
                walkdistance=Sum('walkdistance'),
                walkstepnumber=Sum('walkstepnumber'),
                runstepnumber=Sum('runstepnumber'),
                rundistance=Sum('rundistance'),
                calorieconsumption=Sum('calorieconsumption'),
                restingcalorieconsume=Sum('restingcalorieconsume'),
                movecalorieconsume=Sum('movecalorieconsume'),
                crawledfloor=Sum('crawledfloor'),
                fallitems=Sum('fallitems'),
                activeduration=Sum('activeduration'),
                longestactiveduration=Max('longestactiveduration'),
                longestidleduration=Max('longestidleduration')
            )
        if summ:
            for sum1 in summ:
                if sum1['walkdistance']:
                    listjson['walkdistance'] = sum1['walkdistance']
                else:
                    listjson['walkdistance'] = 0
                if sum1['walkstepnumber']:
                    listjson['walkstepnumber'] = sum1['walkstepnumber']
                else:
                    listjson['walkstepnumber'] = 0
                if sum1['runstepnumber']:
                    listjson['runstepnumber'] = sum1['runstepnumber']
                else:
                    listjson['runstepnumber'] = 0
                if sum1['rundistance']:
                    listjson['rundistance'] = sum1['rundistance']
                else:
                    listjson['rundistance'] = 0
                if sum1['calorieconsumption']:
                    listjson['calorieconsumption'] = sum1['calorieconsumption']
                else:
                    listjson['calorieconsumption'] = 0
                if sum1['restingcalorieconsume']:
                    listjson['restingcalorieconsume'] = sum1['restingcalorieconsume']
                else:
                    listjson['restingcalorieconsume'] = 0
                if sum1['movecalorieconsume']:
                    listjson['movecalorieconsume'] = sum1['movecalorieconsume']
                else:
                    listjson['movecalorieconsume'] = 0
                if sum1['crawledfloor']:
                    listjson['crawledfloor'] = sum1['crawledfloor']
                else:
                    listjson['crawledfloor'] = 0
                if sum1['fallitems']:
                    listjson['fallitems'] = sum1['fallitems']
                else:
                    listjson['fallitems'] = 0
                if sum1['activeduration']:
                    listjson['activeduration'] = sum1['activeduration']
                else:
                    listjson['activeduration'] = 0
                if sum1['longestactiveduration']:
                    listjson['longestactiveduration'] = sum1['longestactiveduration']
                else:
                    listjson['longestactiveduration'] = 0
                if sum1['longestidleduration']:
                    listjson['longestidleduration'] = sum1['longestidleduration']
                else:
                    listjson['longestidleduration'] = 0

                listjson['overtime'] = sum1['overtime']
                alldata.append(listjson.copy())
        else:
            listjson['overtime'] = None
            listjson['longestidleduration'] = 0
            listjson['longestactiveduration'] = 0
            listjson['activeduration'] = 0
            listjson['fallitems'] = 0
            listjson['crawledfloor'] = 0
            listjson['movecalorieconsume'] = 0
            listjson['restingcalorieconsume'] = 0
            listjson['calorieconsumption'] = 0
            listjson['rundistance'] = 0
            listjson['runstepnumber'] = 0
            listjson['walkstepnumber'] = 0
            listjson['walkdistance'] = 0
            alldata.append(listjson.copy())
        terminal = simplejson.dumps(alldata)
    else:
        terminal = False
    return HttpResponse(terminal)
def eatingallmon(request):
    alldata = []
    singledata = {}
    result = {}
    global termianl, elementunit
    try:
        if request.method == "GET":
            userid = request.GET.get("temp_userid")
            querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m').strftime('%Y-%m')
            if request.GET.get('element'):
                element = request.GET.get("element")
                if element == 'moisture':
                    elementunit = 'moisturey'
                elif element == 'protein':
                    elementunit = 'proteiny'
                elif element == 'fat':
                    elementunit = 'faty'
                elif element == 'fiber':
                    elementunit = 'fibery'
                elif element == 'carbohydrate':
                    elementunit = 'carbohydratey'
                elif element == 'cholesterol':
                    elementunit = 'cholestero'
                elif element == 'saturated':
                    elementunit = 'saturatedfattyacid'
                elif element == 'chomuim':
                    elementunit = 'chromium'
                elif element == 'mangaesium':
                    elementunit = 'mangaess'
                else:
                    elementunit = element
                summ = TbDietaryrecords.objects.extra(select={"uptime": "to_char(eatingtime, 'yyyy-mm-dd')"})\
                    .filter(temp_userid=userid, eatingtime__contains=querytime)\
                    .values('uptime').order_by('uptime')\
                    .annotate(
                        intake=Sum('eatingrecord__'+element+'intake')
                    )
                unit = TbFoodnutritioncontent.objects.values(elementunit+'unit')[0:1]
                if summ:
                    for summ1 in summ:
                        singledata['uptime'] = str(summ1['uptime'])
                        if summ1['intake']:
                            singledata["intake"] = round(summ1['intake'], 2)
                            singledata["unit"] = unit[0][elementunit+'unit']
                        else:
                            singledata["intake"] = 0
                        alldata.append(singledata.copy())
                else:
                    singledata['uptime'] = None
                    singledata["intake"] = 0
                    singledata["unit"] =None
                    alldata.append(singledata.copy())
                termianl = alldata
            else:
                count = TbDietaryrecords.objects.extra(select={"uptime": "to_char(eatingtime, 'yyyy-mm-dd')"})\
                    .filter(temp_userid=userid, eatingtime__contains=querytime)\
                    .values('uptime').order_by('uptime')\
                    .annotate(
                        energy=Sum('eatingrecord__energyintake'),
                    ).count()
                summelement = TbDietaryrecords.objects\
                    .filter(
                        temp_userid=userid,
                        eatingtime__contains=querytime
                    ).aggregate(
                        energy=Sum('eatingrecord__energyintake'),
                        moisture=Sum('eatingrecord__moistureintake'),
                        protein=Sum('eatingrecord__proteinintake'),
                        fat=Sum('eatingrecord__fatintake'),
                        cholesterol=Sum('eatingrecord__cholesterolintake'),
                        saturated=Sum('eatingrecord__saturatedintake'),
                    )
                if summelement and count > 0:
                    result['能量'] = round(summelement['energy']/count, 2)
                    result['水分'] = round(summelement['moisture']/count, 2)
                    result['蛋白质'] = round(summelement['protein']/count, 2)
                    result['脂肪'] = round(summelement['fat']/count, 2)
                    result['胆固醇'] = round(summelement['cholesterol']/count, 2)
                    result['饱和脂肪酸'] = round(summelement['saturated']/count, 2)
                else:
                    result['能量'] = 0
                    result['水分'] = 0
                    result['蛋白质'] = 0
                    result['脂肪'] = 0
                    result['胆固醇'] = 0
                    result['饱和脂肪酸'] = 0
                termianl = result
        else:
            termianl = False
    except Exception as e:
        termianl = simplejson.dumps({"error": e.message})
    return HttpResponse(simplejson.dumps(termianl, ensure_ascii=False, encoding='utf-8'))
def sleepallmon(request):
    alldata = []
    listjson = {}
    global terminal
    if request.method == "GET":
        userid = request.GET.get("temp_userid")
        querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m').strftime('%Y-%m')
        summ = TbSleepinforecords.objects.extra(select={"overtime": "to_char(sleepover, 'yyyy-mm-dd')"})\
            .filter(
                temp_userid=userid,
                sleepover__contains=querytime,
            )\
            .values('overtime')\
            .order_by('overtime')\
            .annotate(
                deepsleeptime=Sum('deepsleeptime'),
                shallowsleeptime=Sum('shallowsleeptime'),
                waketimes=Sum('waketimes'),
            )
        if summ:
            for sum1 in summ:
                clear = TbSleepinforecords.objects.filter(
                    temp_userid=userid,
                    sleepover__contains=sum1['overtime'],
                    sleepdetailprocessrecords__temp_sleepstatuscategoryid__sleepstatuscategoryid=2
                ).aggregate(
                    cleartime=Sum('sleepdetailprocessrecords__sleepstatusduration')
                )
                rushui = TbSleepinforecords.objects.filter(
                    temp_userid=userid,
                    sleepover__contains=sum1['overtime'],
                    sleepdetailprocessrecords__temp_sleepstatuscategoryid__sleepstatuscategoryid=1
                ).aggregate(
                    rushuitime=Sum('sleepdetailprocessrecords__sleepstatusduration')
                )
                if clear['cleartime']:
                    listjson['cleartime'] = clear['cleartime']
                else:
                    listjson['cleartime'] = 0
                if rushui['rushuitime']:
                    listjson['intosleeptime'] = rushui['rushuitime']
                else:
                    listjson['intosleeptime'] = 0

                if sum1['deepsleeptime']:
                    listjson['deepsleeptime'] = sum1['deepsleeptime']
                else:
                    listjson['deepsleeptime'] = 0
                if sum1['shallowsleeptime']:
                    listjson['shallowsleeptime'] = sum1['shallowsleeptime']
                else:
                    listjson['shallowsleeptime'] = 0
                if sum1['waketimes']:
                    listjson['waketimes'] = sum1['waketimes']
                else:
                    listjson['waketimes'] = 0
                listjson['overtime'] = sum1['overtime']
                listjson['sumsleepime'] = listjson['deepsleeptime']\
                                           + listjson['shallowsleeptime']\
                                           + listjson['cleartime']\
                                           + listjson['intosleeptime']
                alldata.append(listjson.copy())
        else:
            listjson['overtime'] = None
            listjson['sumsleepime'] = 0
            listjson['waketimes'] = 0
            listjson['shallowsleeptime'] = 0
            listjson['deepsleeptime'] = 0
            listjson['cleartime'] = 0
            listjson['cleartime'] = 0
            alldata.append(listjson.copy())
        terminal = simplejson.dumps(alldata)
    else:
        terminal = False
    return HttpResponse(terminal)

def sleepsingle(request):
    print request.user
    global terminal, sleepbegin, sleepover
    result = {}
    alldata = []
    singdata = {}
    sumsleeptime = 0
    cleartime = 0
    rushuitime = 0

    if request.method == 'GET':
        if request.GET.get("temp_userid") and request.GET.get("querytime"):
            try:
                userid = request.GET.get("temp_userid")
                querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m-%d')
                nexttime = querytime+datetime.timedelta(days=1)
                summ = TbSleepinforecords.objects\
                    .filter(
                        temp_userid=userid,
                        sleepover__gte=querytime,
                        sleepover__lte=nexttime
                    )\
                    .order_by('sleepover')\
                    .aggregate(
                        deepsleeptime=Sum('deepsleeptime'),
                        shallowsleeptime=Sum('shallowsleeptime'),
                        waketimes=Sum('waketimes'),
                    )
                if summ['deepsleeptime']:
                    result['deepsleeptime'] = summ['deepsleeptime']
                    sumsleeptime += summ['deepsleeptime']
                else:
                    result['deepsleeptime'] = 0
                    sumsleeptime += 0
                if summ['shallowsleeptime']:
                    result['shallowsleeptime'] = summ['shallowsleeptime']
                    sumsleeptime += summ['shallowsleeptime']
                else:
                    result['shallowsleeptime'] = 0
                    sumsleeptime += 0
                if summ['waketimes']:
                    result['waketimes'] = summ['waketimes']
                else:
                    result['waketimes'] = 0
                result['querytime'] = datetime.date.strftime(querytime, '%Y-%m-%d')
                result['temp_userid'] = userid
                summ1 = TbSleepinforecords.objects\
                    .filter(
                        temp_userid=userid,
                        sleepover__gte=querytime,
                        sleepover__lte=nexttime
                    ).order_by('sleepover')
                count = TbSleepinforecords.objects\
                    .filter(
                        temp_userid=userid,
                        sleepover__gte=querytime,
                        sleepover__lte=nexttime
                    ).count()
                i = 0
                if summ1:
                    result['sleepbegin'] = str(summ1[0].sleepbegin)
                    result['sleepover'] = str(summ1[count-1].sleepover)
                    for summ11 in summ1:
                        summ12 = summ11.sleepdetailprocessrecords.all()
                        for summ121 in summ12:
                            begintime = summ121.sleepstatusbegintime
                            overtime = summ121.sleepstatusovertime
                            while (overtime-begintime).seconds/60 > 15:
                                singdata['sleepstatusbegintime'] = str(begintime)
                                singdata['sleepstatusduration'] = 15
                                singdata['sleepstatusovertime'] = str(begintime+datetime.timedelta(minutes=15))
                                singdata['status'] = summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid
                                alldata.append(singdata.copy())
                                begintime += datetime.timedelta(minutes=15)
                            else:
                                singdata['sleepstatusbegintime'] = str(begintime)
                                singdata['sleepstatusduration'] = (overtime-begintime).seconds/60
                                singdata['sleepstatusovertime'] = str(overtime)
                                singdata['status'] = summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid
                                alldata.append(singdata.copy())
                            #singdata['sleepstatusbegintime'] = str(summ121.sleepstatusbegintime)
                            #singdata['sleepstatusovertime'] = str(summ121.sleepstatusovertime)
                            #singdata['sleepstatusduration'] = summ121.sleepstatusduration
                            #singdata['status'] = summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid
                            if summ121.sleepstatusduration:
                                if summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid == 2:
                                    cleartime += decimal.Decimal(summ121.sleepstatusduration)
                                if summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid == 1:
                                    rushuitime += decimal.Decimal(summ121.sleepstatusduration)
                        if count > 1:
                            if i < count-1:
                                begintime = summ1[i].sleepover
                                overtime = summ1[i+1].sleepbegin
                                if (overtime-begintime).seconds > 0:
                                    while (overtime-begintime).seconds/60 > 15:
                                        singdata['sleepstatusbegintime'] = str(begintime)
                                        singdata['sleepstatusduration'] = 15
                                        singdata['sleepstatusovertime'] = str(begintime+datetime.timedelta(minutes=15))
                                        singdata['status'] = 0
                                        alldata.append(singdata.copy())
                                        begintime += datetime.timedelta(minutes=15)
                                    else:
                                        singdata['sleepstatusbegintime'] = str(begintime)
                                        singdata['sleepstatusduration'] = (overtime-begintime).seconds/60
                                        singdata['sleepstatusovertime'] = str(overtime)
                                        singdata['status'] = 0
                                        alldata.append(singdata.copy())
                            i += 1
                else:
                    result['sleepbegin'] = None
                    result['sleepover'] = None
                    singdata['sleepstatusbegintime'] = None
                    singdata['sleepstatusovertime'] = None
                    singdata['sleepstatusduration'] = 0
                    singdata['status'] = None
                    alldata.append(singdata.copy())
                result['cleartime'] = cleartime
                result['intosleeptime'] = rushuitime
                result['sumsleeptime'] = sumsleeptime+cleartime+rushuitime
                result['alldata'] = alldata
                terminal = simplejson.dumps(result, ensure_ascii=False, encoding='UTF-8')
            except Exception as e:
                terminal = e.message
        else:
            terminal = None
    else:
        terminal = None
    return HttpResponse(terminal)
def TbSleepspecial(request):
    teminal = None
    result = {}
    riqi = [6, 5, 4, 3, 2, 1, 0, -1]
    cishu = [6, 5, 4, 3, 2, 1, 0]
    alldata = []
    deepsleeptimeaverage = 0
    deepsleeptimefrequence = 0
    shallowsleeptimeaverage = 0
    shallowsleeptimefrequence = 0
    sumsleeptimeaverage = 0
    sumsleeptimefrequence = 0
    waketimesaverage = 0
    cleartimeaverage = 0
    cleartimefrequence = 0
    rushuitimeaverage = 0
    rushuitimefrequence = 0

    singledata = {}
    if request.method == "GET":
        temp_userid = request.GET.get('temp_userid')
        querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m-%d')
        singledata['temp_userid'] = temp_userid
        #data = TbSportinforecords.objects.all().order_by('-sportovertime')[0:1]
        #nearbytime = data[0].sportovertime
        #today = datetime.datetime.strptime(datetime.date.strftime(str(querytime), '%Y-%m-%d'), '%Y-%m-%d')
        try:
            for i in range(len(cishu)):
                down = querytime-datetime.timedelta(days=riqi[i])
                up = querytime-datetime.timedelta(days=riqi[i+1])
                summ = TbSleepinforecords.objects.filter(
                    temp_userid=temp_userid,
                    sleepover__gte=down,
                    sleepover__lte=up
                ).aggregate(
                    deepsleeptime=Sum('deepsleeptime'),
                    shallowsleeptime=Sum('shallowsleeptime'),
                    waketimes=Sum('waketimes'),
                )
                clear = TbSleepinforecords.objects.filter(
                    temp_userid=temp_userid,
                    sleepover__gte=down,
                    sleepover__lte=up,
                    sleepdetailprocessrecords__temp_sleepstatuscategoryid__sleepstatuscategoryid=2
                ).aggregate(
                    cleartime=Sum('sleepdetailprocessrecords__sleepstatusduration')
                )
                rushui = TbSleepinforecords.objects.filter(
                    temp_userid=temp_userid,
                    sleepover__gte=down,
                    sleepover__lte=up,
                    sleepdetailprocessrecords__temp_sleepstatuscategoryid__sleepstatuscategoryid=1
                ).aggregate(
                    rushuitime=Sum('sleepdetailprocessrecords__sleepstatusduration')
                )

                if rushui['rushuitime']:
                    singledata['intosleeptime'] = rushui['rushuitime']
                    rushuitimeaverage += rushui['rushuitime']
                    rushuitimefrequence += 1
                    sumsleeptimeaverage += rushui['rushuitime']
                else:
                    singledata['intosleeptime'] = 0
                    rushuitimeaverage += 0
                    sumsleeptimeaverage += 0
                    sumsleeptimefrequence += 0
                if clear['cleartime']:
                    singledata['cleartime'] = clear['cleartime']
                    cleartimeaverage += clear['cleartime']
                    cleartimefrequence += 1
                    sumsleeptimeaverage += clear['cleartime']
                else:
                    singledata['cleartime'] = 0
                    cleartimeaverage += 0
                    cleartimefrequence += 0
                    sumsleeptimeaverage += 0
                if summ['deepsleeptime']:
                    singledata['deepsleeptime'] = summ['deepsleeptime']
                    deepsleeptimeaverage += summ['deepsleeptime']
                    sumsleeptimeaverage += summ['deepsleeptime']
                    sumsleeptimefrequence += 1
                    deepsleeptimefrequence += 1
                else:
                    singledata['deepsleeptime'] = 0
                    deepsleeptimeaverage += 0
                    sumsleeptimeaverage += 0
                    deepsleeptimefrequence += 0
                    sumsleeptimefrequence += 0
                if summ['shallowsleeptime']:
                    singledata['shallowsleeptime'] = summ['shallowsleeptime']
                    shallowsleeptimeaverage += summ['shallowsleeptime']
                    sumsleeptimeaverage += summ['shallowsleeptime']
                    shallowsleeptimefrequence += 1
                else:
                    singledata['shallowsleeptime'] = 0
                    shallowsleeptimeaverage += 0
                    sumsleeptimeaverage += 0
                    shallowsleeptimefrequence += 0
                if summ['waketimes']:
                    singledata['waketimes'] = summ['waketimes']
                    waketimesaverage += summ['waketimes']
                else:
                    singledata['waketimes'] = 0
                    waketimesaverage += 0
                singledata['sumsleeptime'] = singledata['shallowsleeptime'] \
                                             + singledata['deepsleeptime'] \
                                             + singledata['cleartime']\
                                             + singledata['intosleeptime']
                singledata['sleeptime'] = datetime.date.strftime(down, '%Y-%m-%d')
                alldata.append(singledata.copy())
            if deepsleeptimefrequence == 0:
                deepsleeptimeaverage = 0
            else:
                deepsleeptimeaverage = deepsleeptimeaverage/deepsleeptimefrequence
            if shallowsleeptimefrequence == 0:
                shallowsleeptimeaverage = 0
            else:
                shallowsleeptimeaverage = shallowsleeptimeaverage/shallowsleeptimefrequence
            if sumsleeptimefrequence == 0:
                sumsleeptimeaverage = 0
                waketimesaverage = 0
            else:
                sumsleeptimeaverage = sumsleeptimeaverage/sumsleeptimefrequence
                waketimesaverage = waketimesaverage/sumsleeptimefrequence
            if cleartimefrequence == 0:
                cleartimeaverage = 0
            else:
                cleartimeaverage = cleartimeaverage/cleartimefrequence
            if rushuitimeaverage == 0:
                rushuitimeaverage = 0
            else:
                rushuitimeaverage = rushuitimeaverage/rushuitimefrequence
            result['deepsleeptimeaverage'] = round(deepsleeptimeaverage, 1)
            result['shallowsleeptimeaverage'] = round(shallowsleeptimeaverage, 1)
            result['sumsleeptimeaverage'] = round(sumsleeptimeaverage, 1)
            result['waketimesaverage'] = round(waketimesaverage, 1)
            result['cleartimeaverage'] = round(cleartimeaverage, 1)
            result['intosleeptimeaverage'] = round(rushuitimeaverage, 1)
            result['alldata'] = alldata

            teminal = simplejson.dumps(result)
        except Exception as e:
            teminal = e.message
    else:
        teminal = False
    return HttpResponse(teminal)


def sleepall(request):
    alldata = []
    listjson = {}
    if request.method == "GET":
        userid = request.GET.get("temp_userid")
        summ = TbSleepinforecords.objects.extra(select={"overtime": "to_char(sleepover, 'yyyy-mm-dd')"})\
            .filter(temp_userid=userid)\
            .values('overtime')\
            .order_by('overtime')\
            .annotate(
                deepsleeptime=Sum('deepsleeptime'),
                shallowsleeptime=Sum('shallowsleeptime'),
            )
        for sum1 in summ:
            if sum1['deepsleeptime']:
                listjson['deepsleeptime'] = sum1['deepsleeptime']
            else:
                listjson['deepsleeptime'] = 0
            if sum1['shallowsleeptime']:
                listjson['shallowsleeptime'] = sum1['shallowsleeptime']
            else:
                listjson['shallowsleeptime'] = 0

            listjson['overtime'] = sum1['overtime']
            listjson['sumtime'] = listjson['deepsleeptime']+listjson['shallowsleeptime']
            alldata.append(listjson.copy())
        terminal = simplejson.dumps(alldata)
    else:
        terminal = False
    return HttpResponse(terminal)


def eatingelement(request):
    alldata = []
    singledata = {}
    global termianl, elementunit
    if request.method == "GET":
        userid = request.GET.get("temp_userid")
        element = request.GET.get("element")
        if element == 'moisture':
            elementunit = 'moisturey'
        elif element == 'protein':
            elementunit = 'proteiny'
        elif element == 'fat':
            elementunit = 'faty'
        elif element == 'fiber':
            elementunit = 'fibery'
        elif element == 'carbohydrate':
            elementunit = 'carbohydratey'
        elif element == 'cholesterol':
            elementunit = 'cholestero'
        elif element == 'saturated':
            elementunit = 'saturatedfattyacid'
        elif element == 'chomuim':
            elementunit = 'chromium'
        elif element == 'mangaesium':
            elementunit = 'mangaess'
        else:
            elementunit = element
        summ = TbDietaryrecords.objects.extra(select={"uptime": "to_char(eatingtime, 'yyyy-mm-dd')"})\
            .filter(temp_userid=userid).values('uptime').order_by('uptime')\
            .annotate(
                intake=Sum('eatingrecord__'+element+'intake')
            )
        # summ = TbDietaryrecords.objects.extra(select={"uptime": "to_char(eatingrecordsuptime, 'yyyy-mm-dd')"})\
        #     .filter(temp_userid=userid).values('uptime', "eatingrecord__"+element+'unit').order_by('uptime')\
        #     .annotate(
        #         intake=Sum('eatingrecord__'+element+'intake')
        #     )
        unit = TbFoodnutritioncontent.objects.values(elementunit+'unit')[0:1]
        for summ1 in summ:
            singledata['uptime'] = str(summ1['uptime'])
            if summ1['intake']:
                singledata["intake"] = round(summ1['intake'], 2)
                singledata["unit"] = unit[0][elementunit+'unit']
            else:
                singledata["intake"] = 0
                singledata["unit"] = None
            alldata.append(singledata.copy())
        termianl = alldata
    else:
        termianl = False
    return HttpResponse(simplejson.dumps(termianl))


def eatingtype(request):
    result = {}
    alldata = []
    singledata = {}
    termianl = None
    zaliang = 0
    jianguo = 0
    youzhi = 0
    jianqin = 0
    jiachu = 0
    fish = 0
    egg = 0
    rupin = 0
    fruit = 0
    vegetable = 0
    sugar = 0
    beverage = 0
    alcohol = 0
    tiaowei = 0
    fuhe = 0
    child = 0
    baojian = 0
    other = 0
    if request.method == "GET":
        userid = request.GET.get("temp_userid")
        querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m-%d')
        result['temp_userid'] = userid
        result['querytime'] = datetime.date.strftime(querytime, '%Y-%m-%d')
        nexttime = querytime+datetime.timedelta(days=1)
        summ = TbDietaryrecords.objects\
            .filter(
                temp_userid=userid,
                eatingtime__gte=querytime,
                eatingtime__lte=nexttime
            )
        summelement = TbDietaryrecords.objects\
            .filter(
                temp_userid=userid,
                eatingtime__gte=querytime,
                eatingtime__lte=nexttime,
            ).aggregate(
                energy=Sum('eatingrecord__energyintake'),
                moisture=Sum('eatingrecord__moistureintake'),
                protein=Sum('eatingrecord__proteinintake'),
                fat=Sum('eatingrecord__fatintake'),
                cholesterol=Sum('eatingrecord__cholesterolintake'),
                saturated=Sum('eatingrecord__saturatedintake'),
            )
        if summelement['energy']:
            result['能量'] = summelement['energy']
        else:
            result['能量'] = 0
        if summelement['moisture']:
            result['水分'] = summelement['moisture']
        else:
            result['水分'] = 0
        if summelement['protein']:
            result['蛋白质'] = summelement['protein']
        else:
            result['蛋白质'] = 0
        if summelement['fat']:
            result['脂肪'] = summelement['fat']
        else:
            result['脂肪'] = 0
        if summelement['cholesterol']:
            result['胆固醇'] = summelement['cholesterol']
        else:
            result['胆固醇'] = 0
        if summelement['saturated']:
            result['饱和脂肪酸'] = summelement['saturated']
        else:
            result['饱和脂肪酸'] = 0
        for summ1 in summ:
            eatingamount = summ1.eatingamount
            temp_foodnutritionid = summ1.temp_foodnutritionid.foodnutritionid
            commonfood = TbCommonfoodinfo.objects.filter(commonfoodid=temp_foodnutritionid)
            if eatingamount:
                for summ2 in commonfood:
                    foodwidecategoryid = summ2.temp_commonfoodtypeid.temp_foodwidecategoryid.foodwidecategoryid
                    if foodwidecategoryid == 1:
                        zaliang += eatingamount
                    elif foodwidecategoryid == 2:
                        jianguo += eatingamount
                    elif foodwidecategoryid == 3:
                        youzhi += eatingamount
                    elif foodwidecategoryid == 4:
                        jianqin += eatingamount
                    elif foodwidecategoryid == 5:
                        jiachu += eatingamount
                    elif foodwidecategoryid == 6:
                        fish += eatingamount
                    elif foodwidecategoryid == 7:
                        egg += eatingamount
                    elif foodwidecategoryid == 8:
                        rupin += eatingamount
                    elif foodwidecategoryid == 9:
                        fruit += eatingamount
                    elif foodwidecategoryid == 10:
                        vegetable += eatingamount
                    elif foodwidecategoryid == 11:
                        sugar += eatingamount
                    elif foodwidecategoryid == 12:
                        beverage += eatingamount
                    elif foodwidecategoryid == 13:
                        alcohol += eatingamount
                    elif foodwidecategoryid == 14:
                        tiaowei += eatingamount
                    elif foodwidecategoryid == 15:
                        fuhe += eatingamount
                    elif foodwidecategoryid == 16:
                        child += eatingamount
                    elif foodwidecategoryid == 17:
                        baojian += eatingamount
                    else:
                        other += eatingamount
        singledata['type'] = '全谷杂粮类'
        singledata['value'] = zaliang
        alldata.append(singledata.copy())
        singledata['type'] = '干豆坚果类'
        singledata['value'] = jianguo
        alldata.append(singledata.copy())
        singledata['type'] = '油脂类'
        singledata['value'] = youzhi
        alldata.append(singledata.copy())
        singledata['type'] = '家禽类及其制品类'
        singledata['value'] = jianqin
        alldata.append(singledata.copy())
        singledata['type'] = '家畜类及其制品类'
        singledata['value'] = jiachu
        alldata.append(singledata.copy())
        singledata['type'] = '鱼、水产类'
        singledata['value'] = fish
        alldata.append(singledata.copy())
        singledata['type'] = '蛋类'
        singledata['value'] = egg
        alldata.append(singledata.copy())
        singledata['type'] = '乳品类'
        singledata['value'] = rupin
        alldata.append(singledata.copy())
        singledata['type'] = '水果类'
        singledata['value'] = fruit
        alldata.append(singledata.copy())
        singledata['type'] = '蔬菜类'
        singledata['value'] = vegetable
        alldata.append(singledata.copy())
        singledata['type'] = '糖及糖果零食类'
        singledata['value'] = sugar
        alldata.append(singledata.copy())
        singledata['type'] = '饮料类'
        singledata['value'] = beverage
        alldata.append(singledata.copy())
        singledata['type'] = '酒类'
        singledata['value'] = alcohol
        alldata.append(singledata.copy())
        singledata['type'] = '调味料类'
        singledata['value'] = tiaowei
        alldata.append(singledata.copy())
        singledata['type'] = '复合食品、汤品及汤品类'
        singledata['value'] = fuhe
        alldata.append(singledata.copy())
        singledata['type'] = '婴幼儿食品'
        singledata['value'] = child
        alldata.append(singledata.copy())
        singledata['type'] = '保健食品类'
        singledata['value'] = baojian
        alldata.append(singledata.copy())
        singledata['type'] = '其他'
        singledata['value'] = other
        alldata.append(singledata.copy())
        result['alldata'] = alldata

        termianl = simplejson.dumps(result, ensure_ascii=False, encoding='UTF-8')
    else:
        termianl = False
    return HttpResponse(termianl)



def sleepenv(request):
    alldata = []
    singledata = {}
    termianl = None
    if request.method == "GET":
        userid = request.GET.get("temp_userid")

        summ = TbSleepinforecords.objects.extra(select={"sleepovertime": "to_char(sleepover, 'yyyy-mm-dd')"})\
            .filter(temp_userid=userid)\
            .values('sleepovertime').order_by('sleepovertime')\
            .annotate(
                airhumidity=Avg('airhumidity'),
                ambienttemperature=Avg('ambienttemperature'),
                ambientnoise=Avg('ambientnoise'),
            )

        for summ1 in summ:
            singledata['sleepovertime'] = str(summ1['sleepovertime'])
            if summ1['airhumidity']:
                singledata['airhumidity'] = round(summ1['airhumidity'], 2)
            else:
                singledata['airhumidity'] = 0
            if summ1['ambienttemperature']:
                singledata['ambienttemperature'] = round(summ1['ambienttemperature'], 2)
            else:
                singledata['ambienttemperature'] = 0
            if summ1['ambientnoise']:
                singledata['ambientnoise'] = round(summ1['ambientnoise'], 2)
            else:
                singledata['ambientnoise'] = 0
            alldata.append(singledata.copy())
        termianl = alldata
    else:
        termianl = False
    return HttpResponse(simplejson.dumps(termianl))

def sport(request):
    global down, up, result, termianl
    date1 = datetime.date.today()
    if request.method == 'GET':
        datekey = request.GET.get('date')
        userid = request.GET.get('temp_userid')
        if datekey == "today":
            down = date1
            up = down+datetime.timedelta(days=1)
            result = sportsingletwo(userid, down, up)
        elif datekey == "week":
            result = TbSportseven(userid, date1)
        elif datekey == "month":
            down = date1-datetime.timedelta(days=30)
            up = date1+datetime.timedelta(days=1)
            result = sportmon(userid, down, up)
        else:
            result = simplejson.dumps({'error': 'Flase'})
    return HttpResponse(result)

def sleep(request):
    global down, up, result, termianl
    date1 = datetime.date.today()
    if request.method == 'GET':
        datekey = request.GET.get('date')
        userid = request.GET.get('temp_userid')
        if datekey == "today":
            down = date1
            up = down+datetime.timedelta(days=1)
            result = sleepsingletwo(userid, down, up)
        elif datekey == "week":
            result = TbSleepseven(userid, date1)
        elif datekey == "month":
            down = date1-datetime.timedelta(days=30)
            up = date1+datetime.timedelta(days=1)
            result = sleepmon(userid, down, up)
        else:
            result = simplejson.dumps({'error': 'Flase'})
    return HttpResponse(result)

def eating(request):
    global down, up, result, termianl
    date1 = datetime.date.today()
    if request.method == 'GET':
        datekey = request.GET.get('date')
        userid = request.GET.get('temp_userid')
        if datekey == "today":
            down = date1
            up = down+datetime.timedelta(days=1)
            result = eatingsingle(userid, down, up)
        elif datekey == "week":
            down = date1-datetime.timedelta(days=6)
            up = date1+datetime.timedelta(days=1)
            result = eatingsingle(userid, down, up)

        elif datekey == "month":
            down = date1-datetime.timedelta(days=30)
            up = date1+datetime.timedelta(days=1)
            result = eatingsingle(userid, down, up)
        else:
            result = simplejson.dumps({'error': 'Flase'})
    return HttpResponse(result)
def ceshi(request, datekey):
    global down, up
    date1 = datetime.date.today()
    y = date1.year
    m = date1.month
    if datekey == "thisweek":
        down = date1-datetime.timedelta(days=date1.weekday())
        up = date1+datetime.timedelta(days=7-date1.weekday())
    if datekey == "lastweek":
        down = date1-datetime.timedelta(days=date1.weekday()+7)
        up = date1-datetime.timedelta(days=date1.weekday())
    if datekey == "thismonth":
        down = datetime.date(y, m, 1)
        if m == 12:
            up = datetime.date(y+1, 1, 1)
        else:
            up = datetime.date(y, m+1, 1)
    if datekey == "lastmonth":
        up = datetime.date(y, m, 1)
        if m == 1:
            down = datetime.date(y-1, 12, 1)
        else:
            down = datetime.date(y, m-1, 1)
    if datekey == "thisquarter":
        if m in (1, 2, 3):
            down = datetime.date(y, 1, 1)
            up = datetime.date(y, 4, 1)
        elif m in (4, 5, 6):
            down = datetime.date(y, 4, 1)
            up = datetime.date(y, 7, 1)
        elif m in (7, 8, 9):
            down = datetime.date(y, 7, 1)
            up = datetime.date(y, 10, 1)
        else:
            down = datetime.date(y, 10, 1)
            up = datetime.date(y+1, 1, 1)
    print down, up
    result = TbCommonfoodinfo.objects.last()
    print result
    return HttpResponse(result)

def pagetest(request):
    pg = Paginator(TbAdminisarea.objects.all(), 10)
    test = TbAdminisarea.objects.filter()[0:1]
    print test
    #pgnum = request.GET['pgnum']
    print pg
    print pg.count
    print pg.num_pages
    print pg.page_range
    print pg.page(1).object_list
    print '1'
    result = {}
    result['count'] = pg.count
    if pg.page(1).has_next():
        result['next'] = pg.page(1).next_page_number()
    else:
        result['next'] = None
    if pg.page(1).has_previous():
        result['previous'] = pg.page(1).previous_page_number()
    else:
        result['previous'] = None
    results = serialize('json', pg.page(1).object_list)
    alldata = []
    for xresult in simplejson.loads(results):
        alldata.append(xresult['fields'].copy())
    result['results'] = alldata
    termial = simplejson.dumps(result, ensure_ascii=False, encoding='UTF-8')
    return HttpResponse(termial)
def tokentest(request):
    if request.method == 'GET':
        print '1'
        ltoken = request.META['HTTP_AUTHORIZATION']
        ltoken = ltoken.replace('Token', '')
        ltoken = ltoken.replace(' ', '')
        stoken = RestFrameworkToken.objects.filter(key=ltoken)

        print ltoken
        if stoken:
            print stoken[0].user.userid
        else:
            print 'logout'
        print '2'
    return HttpResponse('ok')
def sleeparea(request):
    if request.method == 'GET':
        result = []
        adminisareaprovince = request.GET.get('adminisareaprovince')
        adminisareacity = request.GET.get('adminisareacity')
        adminisareacounty = request.GET.get('adminisareacounty')
        summ = TbSleepinforecords.objects.filter(

                    temp_userid__temp_adminisareaid__adminisareaprovince=adminisareaprovince,
                    temp_userid__temp_adminisareaid__adminisareacity=adminisareacity,
                    temp_userid__temp_adminisareaid__adminisareacounty=adminisareacounty
                )
        # if summ:
        #     for summ1 in summ:
        #         result.append(summ1)
        xx = serialize('json', summ)
        print xx
        for x in simplejson.loads(xx):
            print x
            print x['fields']
            result.append(x['fields'].copy())
        print result
        return HttpResponse(simplejson.dumps(result, ensure_ascii=False, encoding='UTF-8'))
def sleepadmin(request):
    alldata = []
    listjson = {}
    global terminal
    if request.method == "GET":
        code = int(request.GET.get("code"))
        #querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m').strftime('%Y-%m')
        summ = TbSleepinforecords.objects.extra(select={"overtime": "to_char(sleepover, 'yyyy-mm-dd')"})\
            .filter(
                #sleepover__contains=querytime,
                temp_userid__temp_adminisareaid__adminisareacode=code,
            )\
            .values('overtime')\
            .order_by('overtime')\
            .annotate(
                airhumidity=Avg('airhumidity'),
                ambienttemperature=Avg('ambienttemperature'),
                ambientnoise=Avg('ambientnoise'),
                deepsleeptime=Sum('deepsleeptime'),
                shallowsleeptime=Sum('shallowsleeptime'),
            )
        if summ:
            for sum1 in summ:
                count = TbSleepinforecords.objects.extra(select={"userid": "temp_userid_id"})\
                    .filter(
                        temp_userid__temp_adminisareaid__adminisareacode=code,
                        sleepover__contains=sum1['overtime']
                    )\
                    .values('userid')\
                    .order_by('userid')\
                    .annotate(
                        shallowsleeptime=Sum('shallowsleeptime'),
                    ).count()
                listjson['overtime'] = sum1['overtime']
                if sum1['airhumidity']:
                    listjson['airhumidity'] = round(sum1['airhumidity'], 2)
                else:
                    listjson['airhumidity'] = 0
                if sum1['ambienttemperature']:
                    listjson['ambienttemperature'] = round(sum1['ambienttemperature'], 2)
                else:
                    listjson['ambienttemperature'] = 0
                if sum1['ambientnoise']:
                    listjson['ambientnoise'] = round(sum1['ambientnoise'], 2)
                else:
                    listjson['ambientnoise'] = 0
                if sum1['deepsleeptime']:
                    listjson['deepsleeptime'] = round(sum1['deepsleeptime']/count, 2)
                else:
                    listjson['deepsleeptime'] = 0
                if sum1['shallowsleeptime']:
                    listjson['shallowsleeptime'] = round(sum1['shallowsleeptime']/count, 2)
                else:
                    listjson['shallowsleeptime'] = 0
                alldata.append(listjson.copy())
        else:
            listjson['overtime'] = None
            listjson['deepsleeptime'] = 0
            listjson['shallowsleeptime'] = 0
            listjson['ambientnoise'] = 0
            listjson['airhumidity'] = 0
            listjson['ambienttemperature'] = 0
            alldata.append(listjson.copy())
        terminal = simplejson.dumps(alldata)
    else:
        terminal = False
    return HttpResponse(terminal)
def sportadmin(request):
    result = {}
    alldata = []
    singledata = {}
    terminal = None
    if request.method == 'GET':
        if request.GET.get("code"):
            try:
                code = request.GET.get("code")
                summ = TbSportinforecords.objects.extra(select={"overtime": "to_char(sportovertime, 'yyyy-mm-dd')"})\
                    .filter(
                        temp_userid__temp_adminisareaid__adminisareacode=code,
                    )\
                    .values('overtime')\
                    .order_by('overtime')\
                    .annotate(
                        walkdistance=Sum('walkdistance'),
                        walkstepnumber=Sum('walkstepnumber'),
                        runstepnumber=Sum('runstepnumber'),
                        rundistance=Sum('rundistance'),
                        calorieconsumption=Sum('calorieconsumption'),
                    )
                if summ:
                    for sum1 in summ:
                        count = TbSportinforecords.objects.extra(select={"userid": "temp_userid_id"})\
                            .filter(
                                temp_userid__temp_adminisareaid__adminisareacode=code,
                                sportovertime__contains=sum1['overtime']
                            )\
                            .values('userid')\
                            .order_by('userid')\
                            .annotate(
                                walkdistance=Sum('walkdistance'),
                            ).count()
                        singledata['overtime'] = sum1['overtime']
                        if sum1['walkdistance']:
                            singledata['walkdistance'] = round(sum1['walkdistance']/count, 2)
                        else:
                            singledata['walkdistance'] = 0
                        if sum1['walkstepnumber']:
                            singledata['walkstepnumber'] = round(sum1['walkstepnumber']/count, 2)
                        else:
                            singledata['walkstepnumber'] = 0
                        if sum1['runstepnumber']:
                            singledata['runstepnumber'] = round(sum1['runstepnumber']/count, 2)
                        else:
                            singledata['runstepnumber'] = 0
                        if sum1['rundistance']:
                            singledata['rundistance'] = round(sum1['rundistance']/count, 2)
                        else:
                            singledata['rundistance'] = 0
                        if sum1['calorieconsumption']:
                            singledata['calorieconsumption'] = round(sum1['calorieconsumption']/count, 2)
                        else:
                            singledata['calorieconsumption'] = 0
                        alldata.append(singledata.copy())
                else:
                    singledata['overtime'] = None
                    singledata['walkdistance'] = 0
                    singledata['walkstepnumber'] = 0
                    singledata['runstepnumber'] = 0
                    singledata['rundistance'] = 0
                    singledata['calorieconsumption'] = 0
                    alldata.append(singledata.copy())
                terminal = simplejson.dumps(alldata, ensure_ascii=False, encoding='UTF-8')
            except Exception as e:
                terminal = e.message
        else:
            terminal = None
    else:
        terminal = None
    return HttpResponse(terminal)

def eatingelementadmin(request):
    alldata = []
    singledata = {}
    global termianl, elementunit
    if request.method == "GET":
        code = request.GET.get("code")
        element = request.GET.get("element")
        if element == 'moisture':
            elementunit = 'moisturey'
        elif element == 'protein':
            elementunit = 'proteiny'
        elif element == 'fat':
            elementunit = 'faty'
        elif element == 'fiber':
            elementunit = 'fibery'
        elif element == 'carbohydrate':
            elementunit = 'carbohydratey'
        elif element == 'cholesterol':
            elementunit = 'cholestero'
        elif element == 'saturated':
            elementunit = 'saturatedfattyacid'
        elif element == 'chomuim':
            elementunit = 'chromium'
        elif element == 'mangaesium':
            elementunit = 'mangaess'
        else:
            elementunit = element
        summ = TbDietaryrecords.objects.extra(select={"uptime": "to_char(eatingtime, 'yyyy-mm-dd')"})\
            .filter(temp_userid__temp_adminisareaid__adminisareacode=code)\
            .values('uptime').order_by('uptime')\
            .annotate(
                intake=Sum('eatingrecord__'+element+'intake')
            )
        # summ = TbDietaryrecords.objects.extra(select={"uptime": "to_char(eatingrecordsuptime, 'yyyy-mm-dd')"})\
        #     .filter(temp_userid=userid).values('uptime', "eatingrecord__"+element+'unit').order_by('uptime')\
        #     .annotate(
        #         intake=Sum('eatingrecord__'+element+'intake')
        #     )
        unit = TbFoodnutritioncontent.objects.values(elementunit+'unit')[0:1]
        if summ:
            for summ1 in summ:
                count = TbDietaryrecords.objects.extra(select={"userid": "temp_userid_id"})\
                    .filter(
                        temp_userid__temp_adminisareaid__adminisareacode=code,
                        eatingtime__contains=summ1['uptime']
                    )\
                    .values('userid')\
                    .order_by('userid')\
                    .count()
                singledata['uptime'] = str(summ1['uptime'])
                if summ1['intake']:
                    singledata["intake"] = round(summ1['intake']/count, 2)
                    singledata["unit"] = unit[0][elementunit+'unit']
                else:
                    singledata["intake"] = 0
                    singledata["unit"] = None
                alldata.append(singledata.copy())
        else:
            singledata['uptime'] = None
            singledata['intake'] = 0
            singledata['unit'] = None
            alldata.append(singledata.copy())
        termianl = alldata
    else:
        termianl = False
    return HttpResponse(simplejson.dumps(termianl))

def eatingtypeadmin(request):
    alldata = []
    singledata = {}
    termianl = None
    zaliang = 0
    jianguo = 0
    youzhi = 0
    jianqin = 0
    jiachu = 0
    fish = 0
    egg = 0
    rupin = 0
    fruit = 0
    vegetable = 0
    sugar = 0
    beverage = 0
    alcohol = 0
    tiaowei = 0
    fuhe = 0
    child = 0
    baojian = 0
    other = 0
    if request.method == "GET":
        code = request.GET.get("code")
        querytime = datetime.datetime.strptime(request.GET.get('querytime'), '%Y-%m-%d')
        # result['querytime'] = datetime.date.strftime(querytime, '%Y-%m-%d')
        nexttime = querytime+datetime.timedelta(days=1)
        summ = TbDietaryrecords.objects\
            .filter(
                temp_userid__temp_adminisareaid__adminisareacode=code,
                eatingtime__gte=querytime,
                eatingtime__lte=nexttime
            )
        for summ1 in summ:
            eatingamount = summ1.eatingamount
            temp_foodnutritionid = summ1.temp_foodnutritionid.foodnutritionid
            commonfood = TbCommonfoodinfo.objects.filter(commonfoodid=temp_foodnutritionid)
            if eatingamount:
                for summ2 in commonfood:
                    foodwidecategoryid = summ2.temp_commonfoodtypeid.temp_foodwidecategoryid.foodwidecategoryid
                    if foodwidecategoryid == 1:
                        zaliang += eatingamount
                    elif foodwidecategoryid == 2:
                        jianguo += eatingamount
                    elif foodwidecategoryid == 3:
                        youzhi += eatingamount
                    elif foodwidecategoryid == 4:
                        jianqin += eatingamount
                    elif foodwidecategoryid == 5:
                        jiachu += eatingamount
                    elif foodwidecategoryid == 6:
                        fish += eatingamount
                    elif foodwidecategoryid == 7:
                        egg += eatingamount
                    elif foodwidecategoryid == 8:
                        rupin += eatingamount
                    elif foodwidecategoryid == 9:
                        fruit += eatingamount
                    elif foodwidecategoryid == 10:
                        vegetable += eatingamount
                    elif foodwidecategoryid == 11:
                        sugar += eatingamount
                    elif foodwidecategoryid == 12:
                        beverage += eatingamount
                    elif foodwidecategoryid == 13:
                        alcohol += eatingamount
                    elif foodwidecategoryid == 14:
                        tiaowei += eatingamount
                    elif foodwidecategoryid == 15:
                        fuhe += eatingamount
                    elif foodwidecategoryid == 16:
                        child += eatingamount
                    elif foodwidecategoryid == 17:
                        baojian += eatingamount
                    else:
                        other += eatingamount
        singledata['type'] = '全谷杂粮类'
        singledata['value'] = zaliang
        alldata.append(singledata.copy())
        singledata['type'] = '干豆坚果类'
        singledata['value'] = jianguo
        alldata.append(singledata.copy())
        singledata['type'] = '油脂类'
        singledata['value'] = youzhi
        alldata.append(singledata.copy())
        singledata['type'] = '家禽类及其制品类'
        singledata['value'] = jianqin
        alldata.append(singledata.copy())
        singledata['type'] = '家畜类及其制品类'
        singledata['value'] = jiachu
        alldata.append(singledata.copy())
        singledata['type'] = '鱼、水产类'
        singledata['value'] = fish
        alldata.append(singledata.copy())
        singledata['type'] = '蛋类'
        singledata['value'] = egg
        alldata.append(singledata.copy())
        singledata['type'] = '乳品类'
        singledata['value'] = rupin
        alldata.append(singledata.copy())
        singledata['type'] = '水果类'
        singledata['value'] = fruit
        alldata.append(singledata.copy())
        singledata['type'] = '蔬菜类'
        singledata['value'] = vegetable
        alldata.append(singledata.copy())
        singledata['type'] = '糖及糖果零食类'
        singledata['value'] = sugar
        alldata.append(singledata.copy())
        singledata['type'] = '饮料类'
        singledata['value'] = beverage
        alldata.append(singledata.copy())
        singledata['type'] = '酒类'
        singledata['value'] = alcohol
        alldata.append(singledata.copy())
        singledata['type'] = '调味料类'
        singledata['value'] = tiaowei
        alldata.append(singledata.copy())
        singledata['type'] = '复合食品、汤品及汤品类'
        singledata['value'] = fuhe
        alldata.append(singledata.copy())
        singledata['type'] = '婴幼儿食品'
        singledata['value'] = child
        alldata.append(singledata.copy())
        singledata['type'] = '保健食品类'
        singledata['value'] = baojian
        alldata.append(singledata.copy())
        singledata['type'] = '其他'
        singledata['value'] = other
        alldata.append(singledata.copy())

        termianl = simplejson.dumps(alldata, ensure_ascii=False, encoding='UTF-8')
    else:
        termianl = False
    return HttpResponse(termianl)

