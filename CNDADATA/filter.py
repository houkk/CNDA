# -*- coding: utf-8 -*-
from models import *
import rest_framework_filters as filters
class TbAdminisareaFilter(filters.FilterSet):
    """
    行政区划代码表
    """
    adminisareacode = filters.AllLookupsFilter(name="adminisareacode", lookup_type='contains')
    adminisareaprovince = filters.AllLookupsFilter(name="adminisareaprovince", lookup_type='contains')
    adminisareacounty = filters.AllLookupsFilter(name="adminisareacounty", lookup_type='contains')
    adminisareacity = filters.AllLookupsFilter(name="adminisareacity", lookup_type='contains')
    adminisarearemarks = filters.AllLookupsFilter(name="adminisarearemarks", lookup_type='contains')
    class Meta:
        model = TbAdminisarea



class TbUserFilter(filters.FilterSet):
    """
    用户实体，记录用户基本信息
    """
    username = filters.AllLookupsFilter(name="username", lookup_type='contains')
    usersex = filters.AllLookupsFilter(name="usersex", lookup_type='contains')
    userage = filters.AllLookupsFilter(name="userage", lookup_type='contains')
    userphonenumber = filters.AllLookupsFilter(name="userphonenumber", lookup_type='contains')
    email = filters.AllLookupsFilter(name="email", lookup_type='contains')
    userrank = filters.AllLookupsFilter(name="userrank", lookup_type='contains')
    userwroktype = filters.AllLookupsFilter(name="userwroktype", lookup_type='contains')
    userbmiindex = filters.AllLookupsFilter(name="userbmiindex", lookup_type='contains')
    temp_adminisareaid = filters.RelatedFilter(TbAdminisareaFilter, name='temp_adminisareaid')
    class Meta:
        model = TbUser


class TbCommondiseaseinfoFilter(filters.FilterSet):
    """
    常见疾病信息表
    """
    commondiname = filters.AllLookupsFilter(name="commondiname", lookup_type='contains')
    diseaseexplain = filters.AllLookupsFilter(name="diseaseexplain", lookup_type='contains')
    class Meta:
        model = TbCommondiseaseinfo

class TbCommondiseasetypeFilter(filters.FilterSet):
    """
    常见疾病类别表
    """
    commonditypename = filters.AllLookupsFilter(name="commonditypename", lookup_type='contains')
    commonditypecode = filters.AllLookupsFilter(name="commonditypecode", lookup_type='contains')
    diclassifyexplain = filters.AllLookupsFilter(name="diclassifyexplain", lookup_type='contains')
    class Meta:
        model = TbCommondiseasetype

class TbCommonfoodinfoFilter(filters.FilterSet):
    """
    常见食物信息表
    """
    commonfoodname = filters.AllLookupsFilter(name="commonfoodname", lookup_type='contains')
    commonfoodexplain = filters.AllLookupsFilter(name="commonfoodexplain", lookup_type='contains')
    class Meta:
        model = TbCommonfoodinfo

class TbFoodwidecategoriesFilter(filters.FilterSet):
    """
    食物大类表
    """
    foodwidecatename = filters.AllLookupsFilter(name="foodwidecatename", lookup_type='contains')
    foodwidecateexplain = filters.AllLookupsFilter(name="foodwidecateexplain", lookup_type='contains')

    class Meta:
        model = TbFoodwidecategories

class TbCommonfoodtypeFilter(filters.FilterSet):
    """
    常见食物类别表
    """
    commonfoodtypename = filters.AllLookupsFilter(name="commonfoodtypename", lookup_type='contains')
    commonfoodtypecode = filters.AllLookupsFilter(name="commonfoodtypecode", lookup_type='contains')
    foodtypeexplain = filters.AllLookupsFilter(name="foodtypeexplain", lookup_type='contains')
    class Meta:
        model = TbCommonfoodtype

class TbCommonnutrientintakeFilter(filters.FilterSet):
    """
    营养素每日摄入量
    """
    nutrientname = filters.AllLookupsFilter(name="nutrientname", lookup_type='contains')
    nutrientintakemax = filters.AllLookupsFilter(name="nutrientintakemax", lookup_type='contains')
    nutrientintakemin = filters.AllLookupsFilter(name="nutrientintakemin", lookup_type='contains')
    maxagefor = filters.AllLookupsFilter(name="maxagefor", lookup_type='contains')
    minagefor = filters.AllLookupsFilter(name="minagefor", lookup_type='contains')
    nutrientintakeremarks = filters.AllLookupsFilter(name="nutrientintakeremarks", lookup_type='contains')
    class Meta:
        model = TbCommonnutrientintake

class TbConstituteidentifyresultFilter(filters.FilterSet):
    """
    体质辨识结果记录表
    """
    constituteidentifytime = filters.AllLookupsFilter(name="constituteidentifytime", lookup_type='contains')
    constituteidentifyremarks = filters.AllLookupsFilter(name="constituteidentifyremarks", lookup_type='contains')
    constituteidentifyresult = filters.AllLookupsFilter(name="constituteidentifyresult", lookup_type='contains')
    class Meta:
        model = TbConstituteidentifyresult

class TbCtreatmentrecordsFilter(filters.FilterSet):
    """
    记录用户中医诊疗信息
    """
    integral_spirit = filters.AllLookupsFilter(name="integral_spirit", lookup_type='contains')
    integral_look = filters.AllLookupsFilter(name="integral_look", lookup_type='contains')
    integral_shape = filters.AllLookupsFilter(name="integral_shape", lookup_type='contains')
    part_head = filters.AllLookupsFilter(name="part_head", lookup_type='contains')
    part_organs = filters.AllLookupsFilter(name="part_organs", lookup_type='contains')
    part_chest = filters.AllLookupsFilter(name="part_chest", lookup_type='contains')
    part_tonguenature = filters.AllLookupsFilter(name="part_tonguenature", lookup_type='contains')
    part_fur = filters.AllLookupsFilter(name="part_fur", lookup_type='contains')
    pulsecondition = filters.AllLookupsFilter(name="pulsecondition", lookup_type='contains')
    inquiry_feel = filters.AllLookupsFilter(name="inquiry_feel", lookup_type='contains')
    inquiry_eating = filters.AllLookupsFilter(name="inquiry_eating", lookup_type='contains')
    inquiry_habit = filters.AllLookupsFilter(name="inquiry_habit", lookup_type='contains')
    healthcareguid = filters.AllLookupsFilter(name="healthcareguid", lookup_type='contains')
    examinationtime = filters.AllLookupsFilter(name="examinationtime", lookup_type='contains')
    examinationlocation = filters.AllLookupsFilter(name="examinationlocation", lookup_type='contains')
    examinationresult = filters.AllLookupsFilter(name="examinationresult", lookup_type='contains')
    examinationremarks = filters.AllLookupsFilter(name="examinationremarks", lookup_type='contains')
    class Meta:
        model = TbCtreatmentrecords

class TbDataacquiretypeFilter(filters.FilterSet):
    """
    采集数据分类表
    """
    acqdatatypename = filters.AllLookupsFilter(name="acqdatatypename", lookup_type='contains')
    acqdatatypeexplain = filters.AllLookupsFilter(name="acqdatatypeexplain", lookup_type='contains')
    class Meta:
        model = TbDataacquiretype

class TbDataacquisitionFilter(filters.FilterSet):
    """
    设备数据采集代码表
    """
    acquiredataname = filters.AllLookupsFilter(name="acquiredataname", lookup_type='contains')
    acquiredataexplain = filters.AllLookupsFilter(name="acquiredataexplain", lookup_type='contains')
    class Meta:
        model = TbDataacquisition

class TbDeviceacquiredatarecordsFilter(filters.FilterSet):
    """
    智能设备采集数据记录表
    """
    deviceacqdatavalue = filters.AllLookupsFilter(name="deviceacqdatavalue", lookup_type='contains')
    class Meta:
        model = TbDeviceacquiredatarecords

class TbDeviceparacodeFilter(filters.FilterSet):
    """
    设备参数代码表
    """
    parametercode = filters.AllLookupsFilter(name="parametercode", lookup_type='contains')
    parametername = filters.AllLookupsFilter(name="parametername", lookup_type='contains')
    parametermean = filters.AllLookupsFilter(name="parametermean", lookup_type='contains')
    class Meta:
        model = TbDeviceparacode

class TbDeviceparamappFilter(filters.FilterSet):
    """
    针对不同设备有不同参数
    """
    deviceparavalue = filters.AllLookupsFilter(name="deviceparavalue", lookup_type='contains')
    class Meta:
        model = TbDeviceparamapp

class TbDiagnosistrendsrecordsFilter(filters.FilterSet):
    """
    诊断动态记录表
    """
    diatrendres = filters.AllLookupsFilter(name="diatrendres", lookup_type='contains')
    diatrendresexplain = filters.AllLookupsFilter(name="diatrendresexplain", lookup_type='contains')
    diatrendtime = filters.AllLookupsFilter(name="diatrendtime", lookup_type='contains')
    diatrendplace = filters.AllLookupsFilter(name="diatrendplace", lookup_type='contains')
    class Meta:
        model = TbDiagnosistrendsrecords

class TbDietaryrecordsFilter(filters.FilterSet):
    """
    饮食信息记录表
    """
    foodtypename = filters.AllLookupsFilter(name="foodtypename", lookup_type='contains')
    foodname = filters.AllLookupsFilter(name="foodname", lookup_type='contains')
    eatingamount = filters.AllLookupsFilter(name="eatingamount", lookup_type='contains')
    unitname = filters.AllLookupsFilter(name="unitname", lookup_type='contains')
    eatingtime = filters.AllLookupsFilter(name="eatingtime", lookup_type='contains')
    eatingrecordsuptime = filters.AllLookupsFilter(name="eatingrecordsuptime", lookup_type='contains')
    eatinginforemarks = filters.AllLookupsFilter(name="eatinginforemarks", lookup_type='contains')
    eatingstateback = filters.AllLookupsFilter(name="eatingstateback", lookup_type='contains')
    intelligentdevicecode = filters.AllLookupsFilter(name="intelligentdevicecode", lookup_type='contains')
    temp_userid = filters.RelatedFilter(TbUserFilter, name='temp_userid')
    class Meta:
        model = TbDietaryrecords

class TbDoctorexpertiseinfoFilter(filters.FilterSet):
    """
    医生专长信息表
    """
    doctorexpertisetitle = filters.AllLookupsFilter(name="doctorexpertisetitle", lookup_type='contains')
    doctorexpertiseexplain = filters.AllLookupsFilter(name="doctorexpertiseexplain", lookup_type='contains')
    class Meta:
        model = TbDoctorexpertiseinfo

class TbDoctorexpertisetypeFilter(filters.FilterSet):
    """
    医生专长分类代码表
    """
    doctorexptypename = filters.AllLookupsFilter(name="doctorexptypename", lookup_type='contains')
    doctorexptypecode = filters.AllLookupsFilter(name="doctorexptypecode", lookup_type='contains')
    doctorexptypeexplain = filters.AllLookupsFilter(name="doctorexptypeexplain", lookup_type='contains')
    class Meta:
        model = TbDoctorexpertisetype

class TbEatinganalysisFilter(filters.FilterSet):
    """
    饮食状况分析表
    """
    energyintake = filters.AllLookupsFilter(name="energyintake", lookup_type='contains')
    moistureintake = filters.AllLookupsFilter(name="moistureintake", lookup_type='contains')
    proteinintake = filters.AllLookupsFilter(name="proteinintake", lookup_type='contains')
    fatintake = filters.AllLookupsFilter(name="fatintake", lookup_type='contains')
    ironintake = filters.AllLookupsFilter(name="ironintake", lookup_type='contains')
    potassiumintake = filters.AllLookupsFilter(name="potassiumintake", lookup_type='contains')
    zincintake = filters.AllLookupsFilter(name="zincintake", lookup_type='contains')
    magnesiumintake = filters.AllLookupsFilter(name="magnesiumintake", lookup_type='contains')
    copperintake = filters.AllLookupsFilter(name="copperintake", lookup_type='contains')
    chomuimintake = filters.AllLookupsFilter(name="chomuimintake", lookup_type='contains')
    mangaesiumintake = filters.AllLookupsFilter(name="mangaesiumintake", lookup_type='contains')
    molybdenumintake = filters.AllLookupsFilter(name="molybdenumintake", lookup_type='contains')
    iodineintake = filters.AllLookupsFilter(name="iodineintake", lookup_type='contains')
    phosphrusintake = filters.AllLookupsFilter(name="phosphrusintake", lookup_type='contains')
    seleniumintake = filters.AllLookupsFilter(name="seleniumintake", lookup_type='contains')
    fluorineintake = filters.AllLookupsFilter(name="fluorineintake", lookup_type='contains')
    cholesterolintake = filters.AllLookupsFilter(name="cholesterolintake", lookup_type='contains')
    saturatedintake = filters.AllLookupsFilter(name="saturatedintake", lookup_type='contains')
    acidregurgitationintake = filters.AllLookupsFilter(name="acidregurgitationintake", lookup_type='contains')
    biotinintake = filters.AllLookupsFilter(name="biotinintake", lookup_type='contains')
    cholineintake = filters.AllLookupsFilter(name="cholineintake", lookup_type='contains')
    class Meta:
        model = TbEatinganalysis

class TbEatingpreferrecordsFilter(filters.FilterSet):
    """
    饮食偏好记录表
    """
    foodtypename = filters.AllLookupsFilter(name="foodtypename", lookup_type='contains')
    foodname = filters.AllLookupsFilter(name="foodname", lookup_type='contains')
    preference = filters.AllLookupsFilter(name="preference", lookup_type='contains')
    averageintake = filters.AllLookupsFilter(name="averageintake", lookup_type='contains')
    eatingoftenstarttime = filters.AllLookupsFilter(name="eatingoftenstarttime", lookup_type='contains')
    eatingoftenovertime = filters.AllLookupsFilter(name="eatingoftenovertime", lookup_type='contains')
    class Meta:
        model = TbEatingpreferrecords

class TbEatingsetmealinfoFilter(filters.FilterSet):
    """
    饮食套餐信息表
    """
    foodtypecontent = filters.AllLookupsFilter(name="foodtypecontent", lookup_type='contains')
    setmealname = filters.AllLookupsFilter(name="setmealname", lookup_type='contains')
    setmealexplain = filters.AllLookupsFilter(name="setmealexplain", lookup_type='contains')
    class Meta:
        model = TbEatingsetmealinfo



class TbExercisetypeFilter(filters.FilterSet):
    """
    运动类型名
    """
    exercisetypename = filters.AllLookupsFilter(name="exercisetypename", lookup_type='contains')
    exercisetypeexplain = filters.AllLookupsFilter(name="exercisetypeexplain", lookup_type='contains')
    exercisetypecode = filters.AllLookupsFilter(name="exercisetypecode", lookup_type='contains')
    exercisetyperemarks = filters.AllLookupsFilter(name="exercisetyperemarks", lookup_type='contains')

    class Meta:
        model = TbExercisetype



class TbExerciseinfoFilter(filters.FilterSet):
    """
    运动实体信息表
    """
    exercisename = filters.AllLookupsFilter(name="exercisename", lookup_type='contains')
    exercisetypename = filters.AllLookupsFilter(name="exercisetypename", lookup_type='contains')
    energywaste = filters.AllLookupsFilter(name="energywaste", lookup_type='contains')
    exercisetip = filters.AllLookupsFilter(name="exercisetip", lookup_type='contains')
    exerciseaffect = filters.AllLookupsFilter(name="exerciseaffect", lookup_type='contains')
    class Meta:
        model = TbExerciseinfo

class TbExercisepreferrecordsFilter(filters.FilterSet):
    """
    运动偏好记录表
    """
    exercisetype = filters.AllLookupsFilter(name="exercisetype", lookup_type='contains')
    exercisename = filters.AllLookupsFilter(name="exercisename", lookup_type='contains')
    exercisedescribe = filters.AllLookupsFilter(name="exercisedescribe", lookup_type='contains')
    class Meta:
        model = TbExercisepreferrecords


class TbExpendedhealthpropertiesFilter(filters.FilterSet):
    """
    扩张健康属性表
    """
    healthpropertyname = filters.AllLookupsFilter(name="healthpropertyname", lookup_type='contains')
    healthpropertyexplain = filters.AllLookupsFilter(name="healthpropertyexplain", lookup_type='contains')
    healthpropertyremarks = filters.AllLookupsFilter(name="healthpropertyremarks", lookup_type='contains')

    class Meta:
        model = TbExpendedhealthproperties




class TbFoodfeatureFilter(filters.FilterSet):
    """
    饮食特征信息表
    """
    eatinghabitsdetermine = filters.AllLookupsFilter(name="eatinghabitsdetermine", lookup_type='contains')
    eatinghabitanalysis = filters.AllLookupsFilter(name="eatinghabitanalysis", lookup_type='contains')
    averageenergyintake = filters.AllLookupsFilter(name="averageenergyintake", lookup_type='contains')
    averagemoistureintake = filters.AllLookupsFilter(name="averagemoistureintake", lookup_type='contains')
    averageproteinintake = filters.AllLookupsFilter(name="averageproteinintake", lookup_type='contains')
    averagefatintake = filters.AllLookupsFilter(name="averagefatintake", lookup_type='contains')
    averagefiberintake = filters.AllLookupsFilter(name="averagefiberintake", lookup_type='contains')
    averagecarbohydrateintake = filters.AllLookupsFilter(name="averagecarbohydrateintake", lookup_type='contains')
    averagevitaminaintake = filters.AllLookupsFilter(name="averagevitaminaintake", lookup_type='contains')
    averagevitaminb1intake = filters.AllLookupsFilter(name="averagevitaminb1intake", lookup_type='contains')
    averagevitaminb2intake = filters.AllLookupsFilter(name="averagevitaminb2intake", lookup_type='contains')
    averagevitaminb6intake = filters.AllLookupsFilter(name="averagevitaminb6intake", lookup_type='contains')
    averagevitaminb12intake = filters.AllLookupsFilter(name="averagevitaminb12intake", lookup_type='contains')
    averagevitamincintake = filters.AllLookupsFilter(name="averagevitamincintake", lookup_type='contains')
    averagevitamindintake = filters.AllLookupsFilter(name="averagevitamindintake", lookup_type='contains')
    averagevitamineintake = filters.AllLookupsFilter(name="averagevitamineintake", lookup_type='contains')
    averagevitaminkintake = filters.AllLookupsFilter(name="averagevitaminkintake", lookup_type='contains')
    averagenicotinicacidintake = filters.AllLookupsFilter(name="averagenicotinicacidintake", lookup_type='contains')
    averagefolateintake = filters.AllLookupsFilter(name="averagefolateintake", lookup_type='contains')
    averagesodiumintake = filters.AllLookupsFilter(name="averagesodiumintake", lookup_type='contains')
    averagecalciumintake = filters.AllLookupsFilter(name="averagecalciumintake", lookup_type='contains')
    averageironintake = filters.AllLookupsFilter(name="averageironintake", lookup_type='contains')
    averagepotassiumintake = filters.AllLookupsFilter(name="averagepotassiumintake", lookup_type='contains')
    averagezincintake = filters.AllLookupsFilter(name="averagezincintake", lookup_type='contains')
    averagemagnesiumintake = filters.AllLookupsFilter(name="averagemagnesiumintake", lookup_type='contains')
    averagecopperintake = filters.AllLookupsFilter(name="averagecopperintake", lookup_type='contains')
    averagechomuimintake = filters.AllLookupsFilter(name="averagechomuimintake", lookup_type='contains')
    averagemangaesiumintake = filters.AllLookupsFilter(name="averagemangaesiumintake", lookup_type='contains')
    averagemolybdenumintake = filters.AllLookupsFilter(name="averagemolybdenumintake", lookup_type='contains')
    averageiodineintake = filters.AllLookupsFilter(name="averageiodineintake", lookup_type='contains')
    averagephosphrusintake = filters.AllLookupsFilter(name="averagephosphrusintake", lookup_type='contains')
    averageseleniumintake = filters.AllLookupsFilter(name="averageseleniumintake", lookup_type='contains')
    averagefluorineintake = filters.AllLookupsFilter(name="averagefluorineintake", lookup_type='contains')
    averagecholesterolintake = filters.AllLookupsFilter(name="averagecholesterolintake", lookup_type='contains')
    averagesaturatedintake = filters.AllLookupsFilter(name="averagesaturatedintake", lookup_type='contains')
    averageacidregurgitationintake = filters.AllLookupsFilter(name="averageacidregurgitationintake", lookup_type='contains')
    averagebiotinintake = filters.AllLookupsFilter(name="averagebiotinintake", lookup_type='contains')
    averagecholineintake = filters.AllLookupsFilter(name="averagecholineintake", lookup_type='contains')
    class Meta:
        model = TbFoodfeature

class TbFoodnutritionelementFilter(filters.FilterSet):
    """
    常见食物营养成分元素表
    """
    elementzh = filters.AllLookupsFilter(name="elementzh", lookup_type='contains')
    elementen = filters.AllLookupsFilter(name="elementen", lookup_type='contains')

    class Meta:
        model = TbFoodnutritionelement



class TbFoodnutritioncontentFilter(filters.FilterSet):
    """
    食物营养含量信息表
    """
    foodenergy = filters.AllLookupsFilter(name="foodenergy", lookup_type='contains')
    foodmoisture = filters.AllLookupsFilter(name="foodmoisture", lookup_type='contains')
    proteincontent = filters.AllLookupsFilter(name="proteincontent", lookup_type='contains')
    fatcontent = filters.AllLookupsFilter(name="fatcontent", lookup_type='contains')
    fibercontent = filters.AllLookupsFilter(name="fibercontent", lookup_type='contains')
    carbohydratecontent = filters.AllLookupsFilter(name="carbohydratecontent", lookup_type='contains')
    vitaminacontent = filters.AllLookupsFilter(name="vitaminacontent", lookup_type='contains')
    vitaminb1content = filters.AllLookupsFilter(name="vitaminb1content", lookup_type='contains')
    vitaminb2content = filters.AllLookupsFilter(name="vitaminb2content", lookup_type='contains')
    vitaminb6content = filters.AllLookupsFilter(name="vitaminb6content", lookup_type='contains')
    vitaminb12content = filters.AllLookupsFilter(name="vitaminb12content", lookup_type='contains')
    vitaminccontent = filters.AllLookupsFilter(name="vitaminccontent", lookup_type='contains')
    vitamindcontent = filters.AllLookupsFilter(name="vitamindcontent", lookup_type='contains')
    vitaminecontent = filters.AllLookupsFilter(name="vitaminecontent", lookup_type='contains')
    vitaminkcontent = filters.AllLookupsFilter(name="vitaminkcontent", lookup_type='contains')
    nicotinicacidcontent = filters.AllLookupsFilter(name="nicotinicacidcontent", lookup_type='contains')
    folatecontent = filters.AllLookupsFilter(name="folatecontent", lookup_type='contains')
    sodiumcontent = filters.AllLookupsFilter(name="sodiumcontent", lookup_type='contains')
    calciumcontent = filters.AllLookupsFilter(name="calciumcontent", lookup_type='contains')
    ironcontent = filters.AllLookupsFilter(name="ironcontent", lookup_type='contains')
    potassiumcontent = filters.AllLookupsFilter(name="potassiumcontent", lookup_type='contains')
    zinccontent = filters.AllLookupsFilter(name="zinccontent", lookup_type='contains')
    magnesiumcontent = filters.AllLookupsFilter(name="magnesiumcontent", lookup_type='contains')
    coppercontent = filters.AllLookupsFilter(name="coppercontent", lookup_type='contains')
    chromiumcontent = filters.AllLookupsFilter(name="chromiumcontent", lookup_type='contains')
    mangaesscontent = filters.AllLookupsFilter(name="mangaesscontent", lookup_type='contains')
    molybdenumcontent = filters.AllLookupsFilter(name="molybdenumcontent", lookup_type='contains')
    iodinecontent = filters.AllLookupsFilter(name="iodinecontent", lookup_type='contains')
    phosphruscontent = filters.AllLookupsFilter(name="phosphruscontent", lookup_type='contains')
    seleniumcontent = filters.AllLookupsFilter(name="seleniumcontent", lookup_type='contains')
    fluorinecontent = filters.AllLookupsFilter(name="fluorinecontent", lookup_type='contains')
    cholesterolcontent = filters.AllLookupsFilter(name="cholesterolcontent", lookup_type='contains')
    saturatedfattyacidcontent = filters.AllLookupsFilter(name="saturatedfattyacidcontent", lookup_type='contains')
    acidregurgitationcontent = filters.AllLookupsFilter(name="acidregurgitationcontent", lookup_type='contains')
    biotincontent = filters.AllLookupsFilter(name="biotincontent", lookup_type='contains')
    cholinecontent = filters.AllLookupsFilter(name="cholinecontent", lookup_type='contains')
    class Meta:
        model = TbFoodnutritioncontent

class TbHealthindicatorinfoFilter(filters.FilterSet):
    """
    健康指标信息表
    """
    healthindicatorname = filters.AllLookupsFilter(name="healthindicatorname", lookup_type='contains')
    healthindicatorvalue = filters.AllLookupsFilter(name="healthindicatorvalue", lookup_type='contains')
    healthindicatorchange = filters.AllLookupsFilter(name="healthindicatorchange", lookup_type='contains')
    indicatorchangeexplain = filters.AllLookupsFilter(name="indicatorchangeexplain", lookup_type='contains')
    class Meta:
        model = TbHealthindicatorinfo

class TbHealthknowledgetypeFilter(filters.FilterSet):
    """
    养生知识类别表
    """
    healthknowltypename = filters.AllLookupsFilter(name="healthknowltypename", lookup_type='contains')
    healthknowltypecode = filters.AllLookupsFilter(name="healthknowltypecode", lookup_type='contains')
    healthknowltypeexp = filters.AllLookupsFilter(name="healthknowltypeexp", lookup_type='contains')
    healthknowltyperemarks = filters.AllLookupsFilter(name="healthknowltyperemarks", lookup_type='contains')
    class Meta:
        model = TbHealthknowledgetype


class TbHealthknowledgelimitedFilter(filters.FilterSet):
    """
    养生知识限定条件表
    """

    healthknowllimitedattname = filters.AllLookupsFilter(name="healthknowllimitedattname", lookup_type='contains')
    healthknowllimitedstatus = filters.AllLookupsFilter(name="healthknowllimitedstatus", lookup_type='contains')
    healthknowllimitedstatuslevel = filters.AllLookupsFilter(name="healthknowllimitedstatuslevel", lookup_type='contains')
    healthknowllimitedexp = filters.AllLookupsFilter(name="healthknowllimitedexp", lookup_type='contains')
    healthknowllimitedremarks = filters.AllLookupsFilter(name="healthknowllimitedremarks", lookup_type='contains')
    class Meta:
        model = TbHealthknowledgelimited

class TbHealthsuggtypeFilter(filters.FilterSet):
    """
    健康建议类别表
    """
    healthsuggtypename = filters.AllLookupsFilter(name="healthsuggtypename", lookup_type='contains')
    healthsuggtypecode = filters.AllLookupsFilter(name="healthsuggtypecode", lookup_type='contains')
    suggclassifyexpla = filters.AllLookupsFilter(name="suggclassifyexpla", lookup_type='contains')
    healthsuggtyperemarks = filters.AllLookupsFilter(name="healthsuggtyperemarks", lookup_type='contains')
    class Meta:
        model = TbHealthsuggtype

class TbHealthsuggestionsFilter(filters.FilterSet):
    """
    健康建议表
    """
    healthsuggesttitle = filters.AllLookupsFilter(name="healthsuggesttitle", lookup_type='contains')
    healthsuggestcontent = filters.AllLookupsFilter(name="healthsuggestcontent", lookup_type='contains')
    temp_healthsuggtypeid = filters.RelatedFilter(TbHealthsuggtypeFilter, name='temp_healthsuggtypeid')
    class Meta:
        model = TbHealthsuggestions




class TbHealthsuggestionsmappFilter(filters.FilterSet):
    """
    用户健康建议映射表
    """
    healthsuggcontent = filters.AllLookupsFilter(name="healthsuggcontent", lookup_type='contains')
    healthsuggestreason = filters.AllLookupsFilter(name="healthsuggestreason", lookup_type='contains')
    healthsuggesttime = filters.AllLookupsFilter(name="healthsuggesttime", lookup_type='contains')
    healthsuggestremarks = filters.AllLookupsFilter(name="healthsuggestremarks", lookup_type='contains')

    class Meta:
        model = TbHealthsuggestionsmapp







class TbHealthsuggestlimitedFilter(filters.FilterSet):
    """
    健康建议限定条件表
    """
    suggestlimitedattrname = filters.AllLookupsFilter(name="suggestlimitedattrname", lookup_type='contains')
    suggestlimitedvalue = filters.AllLookupsFilter(name="suggestlimitedvalue", lookup_type='contains')
    suggestlimitedexplain = filters.AllLookupsFilter(name="suggestlimitedexplain", lookup_type='contains')
    suggestlimitedremarks = filters.AllLookupsFilter(name="suggestlimitedremarks", lookup_type='contains')
    class Meta:
        model = TbHealthsuggestlimited





class TbHealthtrendrecordsFilter(filters.FilterSet):
    """
    记录用户健康趋势
    """
    heaanalysistitle = filters.AllLookupsFilter(name="heaanalysistitle", lookup_type='contains')
    healthanalysistime = filters.AllLookupsFilter(name="healthanalysistime", lookup_type='contains')
    healthtrendanalysiresult = filters.AllLookupsFilter(name="healthtrendanalysiresult", lookup_type='contains')
    healthtrendanalysisremarks = filters.AllLookupsFilter(name="healthtrendanalysisremarks", lookup_type='contains')
    class Meta:
        model = TbHealthtrendrecords


class TbHealthwarningtypeFilter(filters.FilterSet):
    """
    健康预警类别表
    """
    healthwarningname = filters.AllLookupsFilter(name="healthwarningname", lookup_type='contains')
    healthwarningtypecode = filters.AllLookupsFilter(name="healthwarningtypecode", lookup_type='contains')
    healthwarningtypeexp = filters.AllLookupsFilter(name="healthwarningtypeexp", lookup_type='contains')
    healthwarningtyperemarks = filters.AllLookupsFilter(name="healthwarningtyperemarks", lookup_type='contains')

    class Meta:
        model = TbHealthwarningtype



class TbHealthwarningmessFilter(filters.FilterSet):
    """
    健康预警信息表
    """

    healthwarningtitle = filters.AllLookupsFilter(name="healthwarningtitle", lookup_type='contains')
    healthwarningcontent = filters.AllLookupsFilter(name="healthwarningcontent", lookup_type='contains')
    healthwarningremarks = filters.AllLookupsFilter(name="healthwarningremarks", lookup_type='contains')
    class Meta:
        model = TbHealthwarningmess


class TbUserhealthattrmappFilter(filters.FilterSet):
    """
    用户健康属性映射表
    """
    expendhealthattrvalue = filters.AllLookupsFilter(name="expendhealthattrvalue", lookup_type='contains')
    updatetime = filters.AllLookupsFilter(name="updatetime", lookup_type='contains')
    userattrmappingexplain = filters.AllLookupsFilter(name="userattrmappingexplain", lookup_type='contains')
    class Meta:
        model = TbUserhealthattrmapp



class TbUserhealthwarningmappFilter(filters.FilterSet):
    """
    用户预警映射表
    """
    healthwarningcontent = filters.AllLookupsFilter(name="healthwarningcontent", lookup_type='contains')
    healthwarningtime = filters.AllLookupsFilter(name="healthwarningtime", lookup_type='contains')
    healthwarningreason = filters.AllLookupsFilter(name="healthwarningreason", lookup_type='contains')
    healthwarningremarks = filters.AllLookupsFilter(name="healthwarningremarks", lookup_type='contains')
    #temp_userid = filters.AllLookupsFilter(name="temp_userid", lookup_type='contains')

    class Meta:
        model = TbUserhealthwarningmapp




class TbHospitaldoctorrelFilter(filters.FilterSet):
    """
    医院医生关系表
    """
    workduty = filters.AllLookupsFilter(name="workduty", lookup_type='contains')
    class Meta:
        model = TbHospitaldoctorrel

class TbHospitalinfoFilter(filters.FilterSet):
    """
    医院信息表
    """
    hospitalname = filters.AllLookupsFilter(name="hospitalname", lookup_type='contains')
    hospitalexplain = filters.AllLookupsFilter(name="hospitalexplain", lookup_type='contains')
    hospitalrank = filters.AllLookupsFilter(name="hospitalrank", lookup_type='contains')
    class Meta:
        model = TbHospitalinfo

class TbHospitalofficesinfoFilter(filters.FilterSet):
    """
    医院科室信息表
    """
    hospitalofficename = filters.AllLookupsFilter(name="hospitalofficename", lookup_type='contains')
    hospitalofficeexplain = filters.AllLookupsFilter(name="hospitalofficeexplain", lookup_type='contains')
    class Meta:
        model = TbHospitalofficesinfo

class TbIdentificationissuessFilter(filters.FilterSet):
    """
    体质辨识问卷项目表
    """
    identifyissuecontent = filters.AllLookupsFilter(name="identifyissuecontent", lookup_type='contains')
    identifyissueremarks = filters.AllLookupsFilter(name="identifyissueremarks", lookup_type='contains')
    class Meta:
        model = TbIdentificationissuess

class TbIdentifychoicesFilter(filters.FilterSet):
    """
    体质辨识选项表
    """
    identifychoicevalue = filters.AllLookupsFilter(name="identifychoicevalue", lookup_type='contains')
    scriptdescribe = filters.AllLookupsFilter(name="scriptdescribe", lookup_type='contains')
    class Meta:
        model = TbIdentifychoices

class TbIdentifydiseaserelFilter(filters.FilterSet):
    """
    记录体质和疾病的关系
    """
    identifydirelexplain = filters.AllLookupsFilter(name="identifydirelexplain", lookup_type='contains')
    class Meta:
        model = TbIdentifydiseaserel

class TbIntelligentdeviceinfoFilter(filters.FilterSet):
    """
    智能设备基本信息表
    """
    intelligentdevicetype = filters.AllLookupsFilter(name="intelligentdevicetype", lookup_type='contains')
    intelligentdevicename = filters.AllLookupsFilter(name="intelligentdevicename", lookup_type='contains')
    intelligentdeviceweight = filters.AllLookupsFilter(name="intelligentdeviceweight", lookup_type='contains')
    intelligentdevicecolor = filters.AllLookupsFilter(name="intelligentdevicecolor", lookup_type='contains')
    intelligentdevicefunction = filters.AllLookupsFilter(name="intelligentdevicefunction", lookup_type='contains')
    intelligentdevicecode = filters.AllLookupsFilter(name="intelligentdevicecode", lookup_type='contains')
    class Meta:
        model = TbIntelligentdeviceinfo

class TbLocationinfoFilter(filters.FilterSet):
    """
    地理位置相关信息
    """
    locationlongitude = filters.AllLookupsFilter(name="locationlongitude", lookup_type='contains')
    locationlatitude = filters.AllLookupsFilter(name="locationlatitude", lookup_type='contains')
    reallocation = filters.AllLookupsFilter(name="reallocation", lookup_type='contains')
    locationremarks = filters.AllLookupsFilter(name="locationremarks", lookup_type='contains')
    locationprovince = filters.AllLookupsFilter(name="locationprovince", lookup_type='contains')
    locationcity = filters.AllLookupsFilter(name="locationcity", lookup_type='contains')
    locationclassify = filters.AllLookupsFilter(name="locationclassify", lookup_type='contains')
    locationcounty = filters.AllLookupsFilter(name="locationcounty", lookup_type='contains')
    class Meta:
        model = TbLocationinfo

class TbManagerFilter(filters.FilterSet):
    """
    管理员实体，记录管理员基本信息
    """
    managername = filters.AllLookupsFilter(name="managername", lookup_type='contains')
    managerunit = filters.AllLookupsFilter(name="managerunit", lookup_type='contains')
    class Meta:
        model = TbManager

class TbMeasurementunitFilter(filters.FilterSet):
    """
    项目中用到的计量单位在此记录
    """
    unitattributename = filters.AllLookupsFilter(name="unitattributename", lookup_type='contains')
    unitlevel = filters.AllLookupsFilter(name="unitlevel", lookup_type='contains')
    unitname = filters.AllLookupsFilter(name="unitname", lookup_type='contains')
    hexadecimal = filters.AllLookupsFilter(name="hexadecimal", lookup_type='contains')
    unitremarks = filters.AllLookupsFilter(name="unitremarks", lookup_type='contains')
    class Meta:
        model = TbMeasurementunit

class TbMedicalhistoryrecordsFilter(filters.FilterSet):
    """
    记录用户病史
    """
    diseasetype = filters.AllLookupsFilter(name="diseasetype", lookup_type='contains')
    diseasename = filters.AllLookupsFilter(name="diseasename", lookup_type='contains')
    diseaseseverity = filters.AllLookupsFilter(name="diseaseseverity", lookup_type='contains')
    treatmentinfo = filters.AllLookupsFilter(name="treatmentinfo", lookup_type='contains')
    treatmentdoctor = filters.AllLookupsFilter(name="treatmentdoctor", lookup_type='contains')
    treatmentunit = filters.AllLookupsFilter(name="treatmentunit", lookup_type='contains')
    treatmentlocation = filters.AllLookupsFilter(name="treatmentlocation", lookup_type='contains')
    treatmentresult = filters.AllLookupsFilter(name="treatmentresult", lookup_type='contains')
    recoverydegree = filters.AllLookupsFilter(name="recoverydegree", lookup_type='contains')
    treatmenttime = filters.AllLookupsFilter(name="treatmenttime", lookup_type='contains')
    treatmentremarks = filters.AllLookupsFilter(name="treatmentremarks", lookup_type='contains')
    class Meta:
        model = TbMedicalhistoryrecords

class TbMedicineinfoFilter(filters.FilterSet):
    """
    中药信息表
    """
    medicinename = filters.AllLookupsFilter(name="medicinename", lookup_type='contains')
    medicinegeneraltype = filters.AllLookupsFilter(name="medicinegeneraltype", lookup_type='contains')
    medicinesubtype = filters.AllLookupsFilter(name="medicinesubtype", lookup_type='contains')
    medicinetoxicity = filters.AllLookupsFilter(name="medicinetoxicity", lookup_type='contains')
    medicineproperty = filters.AllLookupsFilter(name="medicineproperty", lookup_type='contains')
    medicinetaste = filters.AllLookupsFilter(name="medicinetaste", lookup_type='contains')
    indicationsfunction = filters.AllLookupsFilter(name="indicationsfunction", lookup_type='contains')
    channeltropism = filters.AllLookupsFilter(name="channeltropism", lookup_type='contains')
    clinicalapplication = filters.AllLookupsFilter(name="clinicalapplication", lookup_type='contains')
    medicinegenera = filters.AllLookupsFilter(name="medicinegenera", lookup_type='contains')
    prescriptionname = filters.AllLookupsFilter(name="prescriptionname", lookup_type='contains')
    generaldosage = filters.AllLookupsFilter(name="generaldosage", lookup_type='contains')
    generalusage = filters.AllLookupsFilter(name="generalusage", lookup_type='contains')
    withmedicine = filters.AllLookupsFilter(name="withmedicine", lookup_type='contains')
    comment = filters.AllLookupsFilter(name="comment", lookup_type='contains')
    prescriptionsexample = filters.AllLookupsFilter(name="prescriptionsexample", lookup_type='contains')
    medicineremarks = filters.AllLookupsFilter(name="medicineremarks", lookup_type='contains')
    class Meta:
        model = TbMedicineinfo

class TbMedicineprescriptionFilter(filters.FilterSet):
    """
    中药方剂表
    """
    medicineprescriptionname = filters.AllLookupsFilter(name="medicineprescriptionname", lookup_type='contains')
    prescriptionindications = filters.AllLookupsFilter(name="prescriptionindications", lookup_type='contains')
    prescriptionusage = filters.AllLookupsFilter(name="prescriptionusage", lookup_type='contains')
    prescriptionmethod = filters.AllLookupsFilter(name="prescriptionmethod", lookup_type='contains')
    prescriptionspecification = filters.AllLookupsFilter(name="prescriptionspecification", lookup_type='contains')
    prescriptionstore = filters.AllLookupsFilter(name="prescriptionstore", lookup_type='contains')
    prescriptioncontraindicat = filters.AllLookupsFilter(name="prescriptioncontraindicat", lookup_type='contains')
    prescriptiontheories = filters.AllLookupsFilter(name="prescriptiontheories", lookup_type='contains')
    prescriptionextract = filters.AllLookupsFilter(name="prescriptionextract", lookup_type='contains')
    prescriptionremarks = filters.AllLookupsFilter(name="prescriptionremarks", lookup_type='contains')
    prescriptiontag = filters.AllLookupsFilter(name="prescriptiontag", lookup_type='contains')
    class Meta:
        model = TbMedicineprescription




class TbMedicineprescriptionmappFilter(filters.FilterSet):
    """
    药品方剂映射表
    """

    medicineamount = filters.AllLookupsFilter(name="medicineamount", lookup_type='contains')
    medprescriptmappremarks = filters.AllLookupsFilter(name="medprescriptmappremarks", lookup_type='contains')
    class Meta:
        model = TbMedicineprescriptionmapp




class TbMedicineuseinfoFilter(filters.FilterSet):
    """
    记录用户诊疗过程中的用药信息
    """
    medicineusetype = filters.AllLookupsFilter(name="medicineusetype", lookup_type='contains')
    medicineusename = filters.AllLookupsFilter(name="medicineusename", lookup_type='contains')
    medicineusedose = filters.AllLookupsFilter(name="medicineusedose", lookup_type='contains')
    medicineuseremarks = filters.AllLookupsFilter(name="medicineuseremarks", lookup_type='contains')
    prescriptiontag = filters.AllLookupsFilter(name="prescriptiontag", lookup_type='contains')
    class Meta:
        model = TbMedicineuseinfo

class TbMovementdetailrecordsFilter(filters.FilterSet):
    """
    运动详细过程记录表
    """
    movementstarttime = filters.AllLookupsFilter(name="movementstarttime", lookup_type='contains')
    movementstoptime = filters.AllLookupsFilter(name="movementstoptime", lookup_type='contains')
    movementdetailremarks = filters.AllLookupsFilter(name="movementdetailremarks", lookup_type='contains')

    class Meta:
        model = TbMovementdetailrecords



class TbMycollectionFilter(filters.FilterSet):
    """
    我的收藏
    """
    collectionclass = filters.AllLookupsFilter(name="collectionclass", lookup_type="contains")
    class Meta:
        model = TbMycollection



class TbPhoneappinfoFilter(filters.FilterSet):
    """
    手机应用实体部分信息
    """
    apptype = filters.AllLookupsFilter(name="apptype", lookup_type='contains')
    appname = filters.AllLookupsFilter(name="appname", lookup_type='contains')
    apptag = filters.AllLookupsFilter(name="apptag", lookup_type='contains')
    appotherinfo = filters.AllLookupsFilter(name="appotherinfo", lookup_type='contains')
    class Meta:
        model = TbPhoneappinfo

class TbPhoneinfoFilter(filters.FilterSet):
    """
    手机监控特征信息表
    """
    phoneuniqunum = filters.AllLookupsFilter(name="phoneuniqunum", lookup_type='contains')
    phonenum = filters.AllLookupsFilter(name="phonenum", lookup_type='contains')
    class Meta:
        model = TbPhoneinfo

class TbPhonemonitorrecordsFilter(filters.FilterSet):
    """
    手机监控记录表
    """
    appopentime = filters.AllLookupsFilter(name="appopentime", lookup_type='contains')
    appclosetime = filters.AllLookupsFilter(name="appclosetime", lookup_type='contains')
    appusetime = filters.AllLookupsFilter(name="appusetime", lookup_type='contains')
    class Meta:
        model = TbPhonemonitorrecords

class TbPhonepreferuserecordsFilter(filters.FilterSet):
    """
    手机使用偏好记录
    """
    oftenusebeginat = filters.AllLookupsFilter(name="oftenusebeginat", lookup_type='contains')
    oftenuseovertime = filters.AllLookupsFilter(name="oftenuseovertime", lookup_type='contains')
    class Meta:
        model = TbPhonepreferuserecords

class TbPhysiqueinfoFilter(filters.FilterSet):
    """
    体质信息表
    """
    tablescoreheight = filters.AllLookupsFilter(name="tablescoreheight", lookup_type='contains')
    tablescorelow = filters.AllLookupsFilter(name="tablescorelow", lookup_type='contains')
    switchscoreheight = filters.AllLookupsFilter(name="switchscoreheight", lookup_type='contains')
    switchscorelow = filters.AllLookupsFilter(name="switchscorelow", lookup_type='contains')
    generacharacter = filters.AllLookupsFilter(name="generacharacter", lookup_type='contains')
    shapefeature = filters.AllLookupsFilter(name="shapefeature", lookup_type='contains')
    commonmanifest = filters.AllLookupsFilter(name="commonmanifest", lookup_type='contains')
    mentalcharacter = filters.AllLookupsFilter(name="mentalcharacter", lookup_type='contains')
    incidencetendency = filters.AllLookupsFilter(name="incidencetendency", lookup_type='contains')
    adaptivecapacity = filters.AllLookupsFilter(name="adaptivecapacity", lookup_type='contains')
    physicaltypename = filters.AllLookupsFilter(name="physicaltypename", lookup_type='contains')
    physicalinterpretation = filters.AllLookupsFilter(name="physicalinterpretation", lookup_type='contains')
    physicalreason = filters.AllLookupsFilter(name="physicalreason", lookup_type='contains')
    physicaladjustmethod = filters.AllLookupsFilter(name="physicaladjustmethod", lookup_type='contains')
    foodallowtaboo = filters.AllLookupsFilter(name="foodallowtaboo", lookup_type='contains')

    class Meta:
        model = TbPhysiqueinfo


class TbPicturelistFilter(filters.FilterSet):
    """
    图片列表
    """
    #originalpicturepath = filters.AllLookupsFilter(name="originalpicturepath", lookup_type='contains')
    smallpicturepath = filters.AllLookupsFilter(name="smallpicturepath", lookup_type='contains')
    pictureclass = filters.AllLookupsFilter(name="pictureclass", lookup_type='contains')
    picturename = filters.AllLookupsFilter(name="picturename", lookup_type='contains')
    picturetitle = filters.AllLookupsFilter(name="picturetitle", lookup_type='contains')
    pictureremarks = filters.AllLookupsFilter(name="pictureremarks", lookup_type='contains')
    class Meta:
        model = TbPicturelist

class TbRecommendedconditionsmappFilter(filters.FilterSet):
    """
    健康建议条件限定映射表
    """

    recommendmappremarks = filters.AllLookupsFilter(name="recommendmappremarks", lookup_type='contains')

    class Meta:
        model = TbRecommendedconditionsmapp


class TbSetmealfoodmappFiler(filters.FilterSet):
    """
    套餐食物映射表
    """
    mealfoodmapremarks = filters.AllLookupsFilter(name="mealfoodmapremarks", lookup_type='contains')

    class Meta:
        model = TbSetmealfoodmapp


class TbSleepdetailprocessrecordsFilter(filters.FilterSet):
    """
    睡眠详细过程记录表
    """
    sleepstatusbegintime = filters.AllLookupsFilter(name="sleepstatusbegintime", lookup_type='contains')
    sleepstatusovertime = filters.AllLookupsFilter(name="sleepstatusovertime", lookup_type='contains')
    sleepstatusduration = filters.AllLookupsFilter(name="sleepstatusduration", lookup_type='contains')
    sleepstatusremarks = filters.AllLookupsFilter(name="sleepstatusremarks", lookup_type='contains')

    class Meta:
        model = TbSleepdetailprocessrecords



class TbSleepinforecordsFilter(filters.FilterSet):
    """
    记录用户睡眠信息
    """
    airhumidity = filters.AllLookupsFilter(name="airhumidity", lookup_type='contains')
    ambienttemperature = filters.AllLookupsFilter(name="ambienttemperature", lookup_type='contains')
    ambientnoise = filters.AllLookupsFilter(name="ambientnoise", lookup_type='contains')
    sleepbegin = filters.AllLookupsFilter(name="sleepbegin", lookup_type='contains')
    sleepover = filters.AllLookupsFilter(name="sleepover", lookup_type='contains')
    deepsleeptime = filters.AllLookupsFilter(name="deepsleeptime", lookup_type='contains')
    shallowsleeptime = filters.AllLookupsFilter(name="shallowsleeptime", lookup_type='contains')
    sleepremarks = filters.AllLookupsFilter(name="sleepremarks", lookup_type='contains')
    sleeprecorduptime = filters.AllLookupsFilter(name="sleeprecorduptime", lookup_type='contains')
    waketimes = filters.AllLookupsFilter(name="waketimes", lookup_type='contains')
    intelligentdevicecode = filters.AllLookupsFilter(name="intelligentdevicecode", lookup_type='contains')
    temp_userid = filters.RelatedFilter(TbUserFilter, name='temp_userid')
    class Meta:
        model = TbSleepinforecords

class TbSleeppreferrecordsFilter(filters.FilterSet):
    """
    记录用户睡眠偏好，如：睡眠时间，可向用户推送相关信息
    """
    prefersleepbeginat = filters.AllLookupsFilter(name="prefersleepbeginat", lookup_type='contains')
    prefersleepoverat = filters.AllLookupsFilter(name="prefersleepoverat", lookup_type='contains')
    class Meta:
        model = TbSleeppreferrecords


class TbSleepstatuscategoryFilter(filters.FilterSet):
    """
    睡眠状态类别表
    """
    sleepstatusname = filters.AllLookupsFilter(name="sleepstatusname", lookup_type='contains')
    sleepstatusexplain = filters.AllLookupsFilter(name="sleepstatusexplain", lookup_type='contains')

    class Meta:
        model = TbSleepstatuscategory



class TbSportinforecordsFilter(filters.FilterSet):
    """
    记录用户运动数据
    """
    walkstepnumber = filters.AllLookupsFilter(name="walkstepnumber", lookup_type='contains')
    runstepnumber = filters.AllLookupsFilter(name="runstepnumber", lookup_type='contains')
    walkdistance = filters.AllLookupsFilter(name="walkdistance", lookup_type='contains')
    rundistance = filters.AllLookupsFilter(name="rundistance", lookup_type='contains')
    calorieconsumption = filters.AllLookupsFilter(name="calorieconsumption", lookup_type='contains')
    sportbegintime = filters.AllLookupsFilter(name="sportbegintime", lookup_type='contains')
    sportovertime = filters.AllLookupsFilter(name="sportovertime", lookup_type='contains')
    sportrecorduptime = filters.AllLookupsFilter(name="sportrecorduptime", lookup_type='contains')
    sportinforemarks = filters.AllLookupsFilter(name="sportinforemarks", lookup_type='contains')
    sportanalysis = filters.AllLookupsFilter(name="sportanalysis", lookup_type='contains')
    sport_mode = filters.AllLookupsFilter(name="sport_mode", lookup_type='contains')

    class Meta:
        model = TbSportinforecords


class TbStatisticofclickFilter(filters.FilterSet):
    """
    点击量统计表
    """
    clickclass = filters.AllLookupsFilter(name="clickclass", lookup_type='contains')
    clickitem = filters.AllLookupsFilter(name="clickitem", lookup_type='contains')
    praiseyn = filters.AllLookupsFilter(name="praiseyn", lookup_type='contains')
    statisticclickremarks = filters.AllLookupsFilter(name="statisticclickremarks", lookup_type='contains')
    ipaddress = filters.AllLookupsFilter(name="ipaddress", lookup_type='contains')
    class Meta:
        model = TbStatisticofclick


class TbSupervisorylevelFilter(filters.FilterSet):
    """
    管理员管理权限、范围
    """
    managerrank = filters.AllLookupsFilter(name="managerrank", lookup_type='contains')
    class Meta:
        model = TbSupervisorylevel

class TbTcmdcotorsinfoFilter(filters.FilterSet):
    """
    中医专家信息表
    """
    doctorname = filters.AllLookupsFilter(name="doctorname", lookup_type='contains')
    doctorsex = filters.AllLookupsFilter(name="doctorsex", lookup_type='contains')
    doctorage = filters.AllLookupsFilter(name="doctorage", lookup_type='contains')
    professionalrands = filters.AllLookupsFilter(name="professionalrands", lookup_type='contains')
    doctorworktime = filters.AllLookupsFilter(name="doctorworktime", lookup_type='contains')
    doctorsynopsis = filters.AllLookupsFilter(name="doctorsynopsis", lookup_type='contains')
    researcharea = filters.AllLookupsFilter(name="researcharea", lookup_type='contains')
    researchfindings = filters.AllLookupsFilter(name="researchfindings", lookup_type='contains')
    class Meta:
        model = TbTcmdcotorsinfo

class TbTcmdiagnosisobjFilter(filters.FilterSet):
    """
    诊断对象表
    """
    diagnosisobjname = filters.AllLookupsFilter(name="diagnosisobjname", lookup_type='contains')
    diagnosisobjexplain = filters.AllLookupsFilter(name="diagnosisobjexplain", lookup_type='contains')
    class Meta:
        model = TbTcmdiagnosisobj

class TbTcmdiagnosistypeFilter(filters.FilterSet):
    """
    中医诊断分类表
    """
    diagnosistypename = filters.AllLookupsFilter(name="diagnosistypename", lookup_type='contains')
    diagnosistypecode = filters.AllLookupsFilter(name="diagnosistypecode", lookup_type='contains')
    diagnosistypeexplain = filters.AllLookupsFilter(name="diagnosistypeexplain", lookup_type='contains')
    class Meta:
        model = TbTcmdiagnosistype

class TbTcmhealthknowledgeFilter(filters.FilterSet):
    """
    记录中医养生知识发布细节
    """
    healthknowledgetitle = filters.AllLookupsFilter(name="healthknowledgetitle", lookup_type='contains')
    healthknowledgecontent = filters.AllLookupsFilter(name="healthknowledgecontent", lookup_type='contains')
    exersuggtime = filters.AllLookupsFilter(name="exersuggtime", lookup_type='contains')
    healthknowledgeremarks = filters.AllLookupsFilter(name="healthknowledgeremarks", lookup_type='contains')
    class Meta:
        model = TbTcmhealthknowledge



class TbUseranswerrecordsFilter(filters.FilterSet):
    """
    用户答题记录表
    """
    class Meta:
        model = TbUseranswerrecords

class TbUserexercisefeatureFilter(filters.FilterSet):
    """
    用户运动的特征信息，如：身高等
    """
    height = filters.AllLookupsFilter(name="height")
    weight = filters.AllLookupsFilter(name="weight")
    steplength = filters.AllLookupsFilter(name="steplength")
    runsteplength = filters.AllLookupsFilter(name="runsteplength")
    standardweight = filters.AllLookupsFilter(name="standardweight")
    datauptime = filters.AllLookupsFilter(name="datauptime")
    exercisefeatureremarks = filters.AllLookupsFilter(name="exercisefeatureremarks", lookup_type='contains')
    motilityindex = filters.AllLookupsFilter(name="motilityindex", lookup_type='contains')
    exercisehabitsdetermine = filters.AllLookupsFilter(name="exercisehabitsdetermine", lookup_type='contains')
    exercisehabitanalysis = filters.AllLookupsFilter(name="exercisehabitanalysis", lookup_type='contains')
    averageexcitetime = filters.AllLookupsFilter(name="averageexcitetime", lookup_type='contains')
    exercisetypeprefer = filters.AllLookupsFilter(name="exercisetypeprefer", lookup_type='contains')
    class Meta:
        model = TbUserexercisefeature


class TbUserknowledgemappFilter(filters.FilterSet):
    """
    用户养生知识映射表
    """
    healthknowledgecontent = filters.AllLookupsFilter(name="healthknowledgecontent", lookup_type='contains')
    healthknowledgereason = filters.AllLookupsFilter(name="healthknowledgereason", lookup_type='contains')
    healthknowledgetime = filters.AllLookupsFilter(name="healthknowledgetime", lookup_type='contains')
    healthknowledgeremarks = filters.AllLookupsFilter(name="healthknowledgeremarks", lookup_type='contains')

    class Meta:
        model = TbUserknowledgemapp
        fields = (
            'userknowledgemappid', 'temp_userid', 'healthknowledgecontent', 'temp_healthknowledgeid', 'healthknowledgereason',
            'healthknowledgetime', 'healthknowledgeremarks',
        )



class TbUserreviewstatFilter(filters.FilterSet):
    """
    用户评论统计
    """
    userreviewclass = filters.AllLookupsFilter(name="userreviewclass", lookup_type='contains')
    userreviewitem = filters.AllLookupsFilter(name="userreviewitem", lookup_type='contains')
    userreviewcontent = filters.AllLookupsFilter(name="userreviewcontent", lookup_type='contains')
    userreviewremarks = filters.AllLookupsFilter(name="userreviewremarks", lookup_type='contains')
    class Meta:
        model = TbUserreviewstat


class TbUsersleepfeatureFilter(filters.FilterSet):
    """
    用户睡眠特征信息（包括睡眠环境：温度、湿度、噪声情况等）
    """
    airhumidity = filters.AllLookupsFilter(name="airhumidity", lookup_type='contains')
    ambienttemperature = filters.AllLookupsFilter(name="ambienttemperature", lookup_type='contains')
    ambientnoise = filters.AllLookupsFilter(name="ambientnoise", lookup_type='contains')
    bedtimehabits = filters.AllLookupsFilter(name="bedtimehabits", lookup_type='contains')
    goodbedtimehabits = filters.AllLookupsFilter(name="goodbedtimehabits", lookup_type='contains')
    siestahabit = filters.AllLookupsFilter(name="siestahabit", lookup_type='contains')
    averagesleeptime = filters.AllLookupsFilter(name="averagesleeptime", lookup_type='contains')
    sleephabitdetermination = filters.AllLookupsFilter(name="sleephabitdetermination", lookup_type='contains')
    sleepindex = filters.AllLookupsFilter(name="sleepindex", lookup_type='contains')
    sleephabitanalysis = filters.AllLookupsFilter(name="sleephabitanalysis", lookup_type='contains')
    class Meta:
        model = TbUsersleepfeature

class TbWesmedicineexamitemFilter(filters.FilterSet):
    """
    西医体检项目表
    """
    westmedicineitemname = filters.AllLookupsFilter(name="westmedicineitemname", lookup_type='contains')
    wesmedicineitemexpl = filters.AllLookupsFilter(name="wesmedicineitemexpl", lookup_type='contains')
    class Meta:
        model = TbWesmedicineexamitem

class TbWtreatmentrecordsFilter(filters.FilterSet):
    """
    西医诊疗记录表
    """
    wesexamresultval = filters.AllLookupsFilter(name="wesexamresultval", lookup_type='contains')
    class Meta:
        model = TbWtreatmentrecords


class TbVariousindicatorstandardFilter(filters.FilterSet):
    """
    各类指标标准表
    """
    indicatorname = filters.AllLookupsFilter(name="indicatorname", lookup_type='contains')
    indicatorcode = filters.AllLookupsFilter(name="indicatorcode", lookup_type='contains')
    indicatorstatus = filters.AllLookupsFilter(name="indicatorstatus", lookup_type='contains')
    indicatorvalue = filters.AllLookupsFilter(name="indicatorvalue", lookup_type='contains')
    indicatorremarks = filters.AllLookupsFilter(name="indicatorremarks", lookup_type='contains')
    class Meta:
        model = TbVariousindicatorstandard



class TbVariousindicatorlimitedFilter(filters.FilterSet):
    """
    各类标准限定表
    """
    indicatorstandardname = filters.AllLookupsFilter(name="indicatorstandardname", lookup_type='contains')
    indicatorstandardstatus = filters.AllLookupsFilter(name="indicatorstandardstatus", lookup_type='contains')
    indicatorstandardcode = filters.AllLookupsFilter(name="indicatorstandardcode", lookup_type='contains')
    indicatorstandardvalue = filters.AllLookupsFilter(name="indicatorstandardvalue", lookup_type='contains')
    indicatorstandardstatuslevel = filters.AllLookupsFilter(name="indicatorstandardstatuslevel", lookup_type='contains')
    class Meta:
        model = TbVariousindicatorlimited
        fields = (
            'indicatorlimitedid', 'temp_indicatorstandardid', 'indicatorstandardname', 'indicatorstandardstatus', 'indicatorstandardcode',
            'indicatorstandardvalue', 'indicatorstandardstatuslevel',
        )


class TbIndicatorusermappFilter(filters.FilterSet):
    """
    指标用户映射表
    """
    temp_userid = filters.AllLookupsFilter(name="temp_userid", lookup_type='contains')
    userindicatorvalue = filters.AllLookupsFilter(name="userindicatorvalue", lookup_type='contains')
    userindicatorexp = filters.AllLookupsFilter(name="userindicatorexp", lookup_type='contains')
    userindicatorremarks = filters.AllLookupsFilter(name="userindicatorremarks", lookup_type='contains')
    class Meta:
        model = TbIndicatorusermapp
        fields = (
            'indicatorusermappid', 'temp_userid', 'temp_indicatorstandardid', 'userindicatorvalue', 'userindicatorexp',
            'userindicatorremarks',
        )





class DoctorviewFilter(filters.FilterSet):
    """
    中医专家信息视图
    """
    doctorname = filters.AllLookupsFilter(name="doctorname", lookup_type='contains')
    doctorsex = filters.AllLookupsFilter(name="doctorsex", lookup_type='contains')
    doctorage = filters.AllLookupsFilter(name="doctorage", lookup_type='contains')
    professionalrands = filters.AllLookupsFilter(name="professionalrands", lookup_type='contains')
    doctorworktime = filters.AllLookupsFilter(name="doctorworktime", lookup_type='contains')
    doctorsynopsis = filters.AllLookupsFilter(name="doctorsynopsis", lookup_type='contains')
    researcharea = filters.AllLookupsFilter(name="researcharea", lookup_type='contains')
    researchfindings = filters.AllLookupsFilter(name="researchfindings", lookup_type='contains')
    doctorexptypename = filters.AllLookupsFilter(name="doctorexptypename", lookup_type='contains')
    doctorexpertisetitle = filters.AllLookupsFilter(name="doctorexpertisetitle", lookup_type='contains')
    hospitalname = filters.AllLookupsFilter(name="hospitalname", lookup_type='contains')
    hospitalofficename = filters.AllLookupsFilter(name="hospitalofficename", lookup_type='contains')
    workduty = filters.AllLookupsFilter(name="workduty", lookup_type='contains')
    class Meta:
        model = Doctorview


class TbExpertcollectFilter(filters.FilterSet):
    """
    专家收藏表
    """
    collectiontime = filters.AllLookupsFilter(name="collectiontime", lookup_type='contains')
    collectionremarks = filters.AllLookupsFilter(name="collectionremarks", lookup_type='contains')
    collectioncontentsnapshot = filters.AllLookupsFilter(name="collectioncontentsnapshot", lookup_type='contains')

    class Meta:
        model = TbExpertcollect
class TbHealthrecommendscollectionFilter(filters.FilterSet):
    """
    养生建议收藏表
    """
    collectiontime = filters.AllLookupsFilter(name="collectiontime", lookup_type='contains')
    collectionremarks = filters.AllLookupsFilter(name="collectionremarks", lookup_type='contains')
    collectioncontentsnapshot = filters.AllLookupsFilter(name="collectioncontentsnapshot", lookup_type='contains')

    class Meta:
        model = TbHealthrecommendscollection

class TbHealthknowledgecollectionFilter(filters.FilterSet):
    """
    养生知识收藏表
    """
    collectiontime = filters.AllLookupsFilter(name="collectiontime", lookup_type='contains')
    collectionremarks = filters.AllLookupsFilter(name="collectionremarks", lookup_type='contains')
    collectioncontentsnapshot = filters.AllLookupsFilter(name="collectioncontentsnapshot", lookup_type='contains')

    class Meta:
        model = TbHealthknowledgecollection

class TbFoodmedicinaleffecttypeFilter(filters.FilterSet):
    """
    食物药用功效类别
    """
    medicinaleffecttypename = filters.AllLookupsFilter(name="medicinaleffecttypename", lookup_type='contains')
    medicinaleffecttypeexp = filters.AllLookupsFilter(name="medicinaleffecttypeexp", lookup_type='contains')

    class Meta:
        model = TbFoodmedicinaleffecttype

class TbFoodmedicinalpropFilter(filters.FilterSet):
    """
    食物药用属性表
    """
    medicineproperty = filters.AllLookupsFilter(name="medicineproperty", lookup_type='contains')
    medicineflavor = filters.AllLookupsFilter(name="medicineflavor", lookup_type='contains')
    medicineeffect = filters.AllLookupsFilter(name="medicineeffect", lookup_type='contains')
    medicinepropremarks = filters.AllLookupsFilter(name="medicinepropremarks", lookup_type='contains')

    class Meta:
        model = TbFoodmedicinalprop

class TbFoodmedicinalpropmappFilter(filters.FilterSet):
    """
    食物药用属性映射表
    """
    foodmedicinalpropmappexp = filters.AllLookupsFilter(name="foodmedicinalpropmappexp", lookup_type='contains')

    class Meta:
        model = TbFoodmedicinalpropmapp
