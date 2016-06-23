# -*- coding: utf-8 -*-
import decimal
from django.core.paginator import Paginator
import simplejson
from models import *
from rest_framework import serializers
from filter import *
from serializers import *
from rest_framework import viewsets
from rest_framework_bulk import BulkModelViewSet
from django.db.models import Sum, Avg, Max
import datetime
from django.shortcuts import HttpResponse



def TbSportseven(temp_userid, querytime):
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
    # longestactivedurationaverage = 0
    # longestactivedurationfrequency = 0
    # longestidledurationaverage = 0
    # longestidledurationfrequency = 0
    singledata = {}
    temp_userid = temp_userid
    querytime = querytime
    print temp_userid
    print querytime
    result['temp_userid'] = temp_userid
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
                # longestactivedurationaverage += summ['longestactiveduration']
                # longestactivedurationfrequency += 1
            else:
                singledata['longestactiveduration'] = 0
                # longestactivedurationaverage += 0
                # longestactivedurationfrequency += 0
            if summ['longestidleduration']:
                singledata['longestidleduration'] = summ['longestidleduration']
                # longestidledurationaverage += summ['longestidleduration']
                # longestidledurationfrequency += 1
            else:
                singledata['longestidleduration'] = 0
                # longestidledurationaverage += 0
                # longestidledurationfrequency += 0
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
    return HttpResponse(teminal)


def sportsingletwo(userid, down, up):
    result = {}
    alldata = []
    singledata = {}
    terminal = None
    try:
        summ = TbSportinforecords.objects\
            .filter(
                temp_userid=userid,
                sportovertime__gte=down,
                sportovertime__lte=up
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
        result['querytime'] = datetime.date.strftime(down, '%Y-%m-%d')
        result['temp_userid'] = userid

        summ1 = TbSportinforecords.objects.filter(temp_userid=userid, sportovertime__gte=down, sportovertime__lte=up).order_by('sportovertime')
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
        else:
            result['sportbegintime'] = None
            result['sportovertime'] = None
            singledata["sportbegintime"] = None
            singledata["sportovertime"] = None
            singledata["sportanalysis"] = None
            singledata['walkstepnumber'] = 0
            alldata.append(singledata.copy())
        result['alldata'] = alldata
        terminal = simplejson.dumps(result, ensure_ascii=False, encoding='UTF-8')
    except Exception as e:
        terminal = e.message
    return HttpResponse(terminal)
def sportmon(userid, down, up):
    global terminal
    result = {}
    alldata = []
    listjson = {}
    terminal = None
    walkdistance = 0
    walkstepnumber = 0
    runstepnumber = 0
    rundistance = 0
    calorieconsumption = 0
    restingcalorieconsume = 0
    movecalorieconsume = 0
    crawledfloor = 0
    fallitems = 0
    activeduration = 0
    try:
        userid = userid

        summ = TbSportinforecords.objects.extra(select={"overtime": "to_char(sportovertime, 'yyyy-mm-dd')"})\
            .filter(
                temp_userid=userid,
                sportovertime__gte=down,
                sportovertime__lte=up
            )\
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
                walkdistance += sum1['walkdistance']
            else:
                listjson['walkdistance'] = 0
                walkdistance += 0
            if sum1['walkstepnumber']:
                listjson['walkstepnumber'] = sum1['walkstepnumber']
                walkstepnumber += sum1['walkstepnumber']
            else:
                listjson['walkstepnumber'] = 0
                walkstepnumber += 0
            if sum1['runstepnumber']:
                listjson['runstepnumber'] = sum1['runstepnumber']
                runstepnumber += sum1['runstepnumber']
            else:
                listjson['runstepnumber'] = 0
                runstepnumber += 0
            if sum1['rundistance']:
                listjson['rundistance'] = sum1['rundistance']
                rundistance += sum1['rundistance']
            else:
                listjson['rundistance'] = 0
                rundistance += 0
            if sum1['calorieconsumption']:
                listjson['calorieconsumption'] = sum1['calorieconsumption']
                calorieconsumption += sum1['calorieconsumption']
            else:
                listjson['calorieconsumption'] = 0
                calorieconsumption += 0
            if sum1['restingcalorieconsume']:
                listjson['restingcalorieconsume'] = sum1['restingcalorieconsume']
                restingcalorieconsume += sum1['restingcalorieconsume']
            else:
                listjson['restingcalorieconsume'] = 0
                restingcalorieconsume += 0
            if sum1['movecalorieconsume']:
                listjson['movecalorieconsume'] = sum1['movecalorieconsume']
                movecalorieconsume += sum1['movecalorieconsume']
            else:
                listjson['movecalorieconsume'] = 0
                movecalorieconsume += 0
            if sum1['crawledfloor']:
                listjson['crawledfloor'] = sum1['crawledfloor']
                crawledfloor += sum1['crawledfloor']
            else:
                listjson['crawledfloor'] = 0
                crawledfloor += 0
            if sum1['fallitems']:
                listjson['fallitems'] = sum1['fallitems']
                fallitems += sum1['fallitems']
            else:
                listjson['fallitems'] = 0
                fallitems += 0
            if sum1['activeduration']:
                listjson['activeduration'] = sum1['activeduration']
                activeduration += sum1['activeduration']
            else:
                listjson['activeduration'] = 0
                activeduration += 0
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
        result['alldata'] = alldata
        if len(summ):

            result['walkdistance'] = round(walkdistance/len(summ), 2)
            result['walkstepnumber'] = round(walkstepnumber/len(summ), 2)
            result['runstepnumber'] = round(runstepnumber/len(summ), 2)
            result['rundistance'] = round(rundistance/len(summ), 2)
            result['calorieconsumption'] = round(calorieconsumption/len(summ), 2)
            result['restingcalorieconsume'] = round(restingcalorieconsume/len(summ), 2)
            result['movecalorieconsume'] = round(movecalorieconsume/len(summ), 2)
            result['crawledfloor'] = round(crawledfloor/len(summ), 2)
            result['fallitems'] = round(fallitems/len(summ), 2)
            result['activeduration'] = round(activeduration/len(summ), 2)
        else:
            result['walkdistance'] = 0
            result['walkstepnumber'] = 0
            result['runstepnumber'] = 0
            result['rundistance'] = 0
            result['calorieconsumption'] = 0
            result['restingcalorieconsume'] = 0
            result['movecalorieconsume'] = 0
            result['crawledfloor'] = 0
            result['fallitems'] = 0
            result['activeduration'] = 0
        terminal = simplejson.dumps(result, ensure_ascii=False, encoding='UTF-8')
    except Exception as e:
        terminal = e.message
    return HttpResponse(terminal)


def sleepsingletwo(userid, down, up):
    global terminal
    result = {}
    alldata = []
    singdata = {}
    sumsleeptime = 0
    cleartime = 0
    rushuitime = 0
    try:
        userid = userid
        summ = TbSleepinforecords.objects\
            .filter(
                temp_userid=userid,
                sleepover__gte=down,
                sleepover__lte=up
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
        result['querytime'] = str(down)
        result['temp_userid'] = userid
        summ1 = TbSleepinforecords.objects\
            .filter(
                temp_userid=userid,
                sleepover__gte=down,
                sleepover__lte=up
            ).order_by('sleepover')
        if summ1:
            result['sleepbegin'] = str(summ1[0].sleepbegin)
            result['sleepover'] = str(summ1[len(summ1)-1].sleepover)
            for summ11 in summ1:
                summ12 = summ11.sleepdetailprocessrecords.all()
                for summ121 in summ12:
                    singdata['sleepstatusbegintime'] = str(summ121.sleepstatusbegintime)
                    singdata['sleepstatusovertime'] = str(summ121.sleepstatusovertime)
                    singdata['sleepstatusduration'] = summ121.sleepstatusduration
                    singdata['status'] = summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid
                    if summ121.sleepstatusduration:
                        if summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid == 2:
                            cleartime += decimal.Decimal(summ121.sleepstatusduration)
                        if summ121.temp_sleepstatuscategoryid.sleepstatuscategoryid == 1:
                            rushuitime += decimal.Decimal(summ121.sleepstatusduration)
                        alldata.append(singdata.copy())
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
    return HttpResponse(terminal)

def TbSleepseven(userid, querytime):
    global teminal
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
    temp_userid = userid
    result['temp_userid'] = temp_userid
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
            if clear['cleartime']:
                singledata['cleartime'] = clear['cleartime']
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
                sumsleeptimefrequence += 0
                deepsleeptimefrequence += 0
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

        result['alldata'] = alldata
        result['deepsleeptimeaverage'] = round(deepsleeptimeaverage, 1)
        result['shallowsleeptimeaverage'] = round(shallowsleeptimeaverage, 1)
        result['sumsleeptimeaverage'] = round(sumsleeptimeaverage, 1)
        result['waketimesaverage'] = round(waketimesaverage, 1)
        result['cleartimeaverage'] = round(cleartimeaverage, 1)
        result['intosleeptimeaverage'] = round(rushuitimeaverage, 1)
        teminal = simplejson.dumps(result)
    except Exception as e:
        teminal = e.message
    return HttpResponse(teminal)


def sleepmon(userid, down, up):
    result = {}
    alldata = []
    listjson = {}
    global terminal
    deepsleeptimeaverage = 0
    shallowsleeptimeaverage = 0
    sumsleeptimeaverage = 0
    waketimesaverage = 0
    cleartimeaverage = 0
    intosleeptimeaverage = 0
    try:
        userid = userid
        summ = TbSleepinforecords.objects.extra(select={"overtime": "to_char(sleepover, 'yyyy-mm-dd')"})\
            .filter(
                temp_userid=userid,
                sleepover__gte=down,
                sleepover__lte=up
            )\
            .values('overtime')\
            .order_by('overtime')\
            .annotate(
                deepsleeptime=Sum('deepsleeptime'),
                shallowsleeptime=Sum('shallowsleeptime'),
                waketimes=Sum('waketimes'),
            )
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
                cleartimeaverage += clear['cleartime']
                sumsleeptimeaverage += clear['cleartime']
            else:
                listjson['cleartime'] = 0
                cleartimeaverage += 0
                sumsleeptimeaverage += 0
            if rushui['rushuitime']:
                listjson['intosleeptime'] = rushui['rushuitime']
                intosleeptimeaverage += rushui['rushuitime']
                sumsleeptimeaverage += rushui['rushuitime']
            else:
                listjson['intosleeptime'] = 0
                intosleeptimeaverage += 0
                sumsleeptimeaverage += 0

            if sum1['deepsleeptime']:
                listjson['deepsleeptime'] = sum1['deepsleeptime']
                deepsleeptimeaverage += sum1['deepsleeptime']
                sumsleeptimeaverage += sum1['deepsleeptime']
            else:
                listjson['deepsleeptime'] = 0
                deepsleeptimeaverage += 0
                sumsleeptimeaverage += 0
            if sum1['shallowsleeptime']:
                listjson['shallowsleeptime'] = sum1['shallowsleeptime']
                shallowsleeptimeaverage += sum1['shallowsleeptime']
                sumsleeptimeaverage += sum1['shallowsleeptime']
            else:
                listjson['shallowsleeptime'] = 0
                shallowsleeptimeaverage += 0
                sumsleeptimeaverage += 0
            if sum1['waketimes']:
                listjson['waketimes'] = sum1['waketimes']
                waketimesaverage += sum1['waketimes']
            else:
                listjson['waketimes'] = 0
                waketimesaverage += 0

            listjson['overtime'] = sum1['overtime']
            listjson['sumsleepime'] = listjson['deepsleeptime']\
                                       + listjson['shallowsleeptime']\
                                       + listjson['cleartime']\
                                       + listjson['intosleeptime']
            alldata.append(listjson.copy())
        result['alldata'] = alldata
        if len(summ):
            result['deepsleeptimeaverage'] = round(deepsleeptimeaverage/len(summ), 2)
            result['shallowsleeptimeaverage'] = round(shallowsleeptimeaverage/len(summ), 2)
            result['cleartimeaverage'] = round(cleartimeaverage/len(summ), 2)
            result['intosleeptimeaverage'] = round(intosleeptimeaverage/len(summ), 2)
            result['sumsleeptimeaverage'] = round(sumsleeptimeaverage/len(summ), 2)
            result['waketimesaverage'] = round(waketimesaverage/len(summ), 2)
        else:
            result['deepsleeptimeaverage'] = 0
            result['shallowsleeptimeaverage'] = 0
            result['cleartimeaverage'] = 0
            result['intosleeptimeaverage'] = 0
            result['sumsleeptimeaverage'] = 0
            result['sumsleeptimeaverage'] = 0
            result['waketimesaverage'] = 0

        terminal = simplejson.dumps(result)
    except Exception as e:
        terminal = e.message
    return HttpResponse(terminal)

def eatingsingle(userid, down, up):
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
    try:
        userid = userid
        result['temp_userid'] = userid
        summ = TbDietaryrecords.objects\
            .filter(
                temp_userid=userid,
                eatingtime__gte=down,
                eatingtime__lte=up
            )
        count = TbDietaryrecords.objects.extra(select={"uptime": "to_char(eatingtime, 'yyyy-mm-dd')"})\
            .filter(
                temp_userid=userid,
                eatingtime__gte=down,
                eatingtime__lte=up
            ).values('uptime').order_by('uptime')\
            .annotate(
                energy=Sum('eatingrecord__energyintake'),
            ).count()
        summelement = TbDietaryrecords.objects\
            .filter(
                temp_userid=userid,
                eatingtime__gte=down,
                eatingtime__lte=up
            ).aggregate(
                energy=Sum('eatingrecord__energyintake'),
                moisture=Sum('eatingrecord__moistureintake'),
                protein=Sum('eatingrecord__proteinintake'),
                fat=Sum('eatingrecord__fatintake'),
                cholesterol=Sum('eatingrecord__cholesterolintake'),
                saturated=Sum('eatingrecord__saturatedintake'),
            )
        if summelement['energy']:
            result['能量'] = round(summelement['energy']/decimal.Decimal(count), 2)
        else:
            result['能量'] = 0
        if summelement['moisture']:
            result['水分'] = round(summelement['moisture']/decimal.Decimal(count), 2)
        else:
            result['水分'] = 0
        if summelement['protein']:
            result['蛋白质'] = round(summelement['protein']/decimal.Decimal(count), 2)
        else:
            result['蛋白质'] = 0
        if summelement['fat']:
            result['脂肪'] = round(summelement['fat']/decimal.Decimal(count), 2)
        else:
            result['脂肪'] = 0
        if summelement['cholesterol']:
            result['胆固醇'] = round(summelement['cholesterol']/decimal.Decimal(count), 2)
        else:
            result['胆固醇'] = 0
        if summelement['saturated']:
            result['饱和脂肪酸'] = round(summelement['saturated']/count, 2)
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
    except Exception as e:
        termianl = simplejson.dumps({'error': e.message})
    return termianl
