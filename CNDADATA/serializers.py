# -*- coding: utf-8 -*-
import datetime
import decimal
from django.db import transaction
from rest_framework.validators import UniqueValidator
import simplejson
from models import *
from rest_framework import serializers


class TbPicturelistSerializer(serializers.ModelSerializer):
    """
    图片列表
    """
    originalpicturepath = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False)
    class Meta:
        model = TbPicturelist
        fields = (
            'picturelocationid', 'originalpicturepath', 'smallpicturepath', 'pictureclass', 'picturename',
            'picturetitle', 'pictureusecode', 'pictureremarks',
        )


class TbAdminisareaSerializer(serializers.ModelSerializer):
    """
    行政区划代码表
    """
    class Meta:
        model = TbAdminisarea
        fields = (
            'adminisareaid', 'adminisareacode', 'adminisareaprovince', 'adminisareacity', 'adminisareacounty',
            'adminisarearemarks',
        )

class TbAverageamountstdSerializer(serializers.ModelSerializer):
    """
    平均量计算标准
    """
    #amountbegintime = serializers.
    class Meta:
        model = TbAverageamountstd
        fields = (
            'amountstdid', 'amountnumofdays', 'averageamountremarks', 'amountbegintime', 'amountstoptime',
        )


class TbCommondiseaseinfoSerializer(serializers.ModelSerializer):
    """
    常见疾病信息表
    """

    class Meta:
        model = TbCommondiseaseinfo
        fields = (
            'commondiseaseid', 'temp_commonditypeid', 'commondiname', 'diseaseexplain',
        )

class TbCommondiseasetypeSerializer(serializers.ModelSerializer):
    """
    常见疾病类别表
    """

    class Meta:
        model = TbCommondiseasetype
        fields = (
            'commonditypeid', 'commonditypename', 'commonditypecode', 'diclassifyexplain',
        )

class TbCommonfoodinfoSerializer(serializers.ModelSerializer):
    """
    常见食物信息表
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    #temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbCommonfoodinfo
        fields = (
            'commonfoodid', 'commonfoodname', 'temp_commonfoodtypeid', 'commonfoodexplain', 'temp_foodnutritionid',
            'temp_picturelocationid',
        )
        extra_kwargs = {
            'temp_picturelocationid': {'required': False},

        }

class TbFoodwidecategoriesSerializer(serializers.ModelSerializer):
    """
    食物大类表
    """
    class Meta:
        model = TbFoodwidecategories

class TbCommonfoodtypeSerializer(serializers.ModelSerializer):
    """
    常见食物类别表
    """
    class Meta:
        model = TbCommonfoodtype
        fields = (
            'commonfoodtypeid', 'commonfoodtypename', 'commonfoodtypecode', 'foodtypeexplain', 'temp_foodwidecategoryid',
        )

class TbCommonnutrientintakeSerializer(serializers.ModelSerializer):
    """
    营养素每日摄入量
    """
    temp_unitattributeid = serializers.SlugRelatedField(queryset=TbMeasurementunit.objects.all(), slug_field='unitname')
    class Meta:
        model = TbCommonnutrientintake
        fields = (
            'nutrientid', 'nutrientname', 'nutrientintakemax', 'nutrientintakemin', 'maxagefor',
            'minagefor', 'nutrientintakeremarks', 'temp_unitattributeid',
        )


class TbUserSerializer(serializers.ModelSerializer):
    """
    用户实体，记录用户基本信息
    """
    last_login = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbUser
        fields = (
            'userid', 'username', 'usersex', 'userage', 'password', 'name', 'last_login',
            'userphonenumber', 'email', 'userrank', 'userwroktype', 'userbmiindex', 'is_admin',
            'temp_sleepfeatureid', 'temp_exercisefeatureid', 'temp_eatingfeatureid', 'temp_adminisareaid',
            'temp_picturelocationid',
        )


class TbConstituteidentifyresultSerializer(serializers.ModelSerializer):
    """
    体质辨识结果记录表
    """
    constituteidentifytime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbConstituteidentifyresult
        fields = (
            'identifyresultid', 'temp_userid', 'temp_physiqueinfoid', 'constituteidentifytime', 'constituteidentifyremarks',
            'constituteidentifyresult', 'constituteldentifyflag',
        )

class TbCtreatmentrecordsSerializer(serializers.ModelSerializer):
    """
    记录用户中医诊疗信息
    """
    examinationtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbCtreatmentrecords
        fields = (
            'tcmexaminationid', 'integral_spirit', 'integral_look', 'integral_shape', 'part_head',
            'part_organs','part_chest', 'part_tonguenature', 'part_fur', 'pulsecondition',
            'inquiry_feel', 'inquiry_eating', 'inquiry_habit','healthcareguid', 'temp_userid',
            'temp_doctorid', 'examinationtime','examinationlocation',
            'examinationresult', 'examinationremarks',
        )

class TbDataacquiretypeSerializer(serializers.ModelSerializer):
    """
    采集数据分类表
    """

    class Meta:
        model = TbDataacquiretype
        fields = (
            'acqdatatypeid', 'acqdatatypename', 'acqdatatypeexplain',
        )

class TbDataacquisitionSerializer(serializers.ModelSerializer):
    """
    设备数据采集代码表
    """
    class Meta:
        model = TbDataacquisition
        fields = (
            'acquiredataid', 'acquiredataname', 'acquiredataexplain', 'temp_acqdatatypeid',
        )

class TbDeviceacquiredatarecordsSerializer(serializers.ModelSerializer):
    """
    智能设备采集数据记录表
    """
    class Meta:
        model = TbDeviceacquiredatarecords
        fields = (
            'deviceacqrecordid', 'temp_intelligentdeviceid', 'temp_acquiredataid', 'deviceacqdatavalue', 'temp_unitattributeid',
        )

class TbDeviceparacodeSerializer(serializers.ModelSerializer):
    """
    设备参数代码表
    """
    class Meta:
        model = TbDeviceparacode
        fields = (
            'deviceparacodeid', 'parametercode', 'parametername', 'parametermean',
        )

class TbDeviceparamappSerializer(serializers.ModelSerializer):
    """
    针对不同设备有不同参数
    """
    temp_intelligentdeviceid = serializers.SlugRelatedField(queryset=TbIntelligentdeviceinfo.objects.all(), slug_field='intelligentdevicename')
    temp_deviceparacodeid = serializers.SlugRelatedField(queryset=TbDeviceparacode.objects.all(), slug_field='parametername')
    class Meta:
        model = TbDeviceparamapp
        fields = (
            'deviceparamappid', 'temp_intelligentdeviceid', 'temp_deviceparacodeid', 'deviceparavalue',
        )

class TbDiagnosistrendsrecordsSerializer(serializers.ModelSerializer):
    """
    诊断动态记录表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbDiagnosistrendsrecords
        fields = (
            'diatrendid', 'temp_userid', 'temp_diagnosisobjid', 'temp_doctorid', 'diatrendres',
            'diatrendresexplain', 'diatrendtime', 'diatrendplace', 'temp_locationinfoid',
        )

class TbDietaryrecordsSerializer(serializers.ModelSerializer):
    """
    饮食信息记录表
    """
    eatingovertime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    eatingtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    eatingrecordsuptime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    #temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbDietaryrecords
        fields = (
            'eatingrecordid', 'foodtypename', 'foodname', 'eatingamount', 'unitname',
            'eatingtime', 'eatingrecordsuptime', 'eatinginforemarks', 'temp_userid', 'eatingstateback',
            'temp_foodnutritionid', 'temp_locationinfoid', 'temp_intelligentdeviceid', 'intelligentdevicecode', 'eatingupflag',
            'setmealcode', 'eatingovertime',
        )

    def create(self, validated_data):
        with transaction.atomic():
            tbdietaryrecords = TbDietaryrecords.objects.create(**validated_data)
            temp_foodnutritionid = validated_data['temp_foodnutritionid']
            eatingamount = validated_data['eatingamount']
            eatinganalysis = {}
            if temp_foodnutritionid and eatingamount:
                foodnutritincontent = TbFoodnutritioncontent.objects.filter(foodnutritionid=temp_foodnutritionid.foodnutritionid)
                edibleparts = foodnutritincontent[0].edibleparts/100.0
                result = decimal.Decimal(eatingamount)/decimal.Decimal(100.0)*decimal.Decimal(edibleparts)
                eatinganalysis['energyintake'] = round(result*foodnutritincontent[0].foodenergy, 2)
                eatinganalysis['energyunit'] = foodnutritincontent[0].energyunit
                eatinganalysis['moistureintake'] = round(result*foodnutritincontent[0].foodmoisture, 2)
                eatinganalysis['moistureunit'] = foodnutritincontent[0].moistureyunit
                eatinganalysis['proteinintake'] = round(result*foodnutritincontent[0].proteincontent, 2)
                eatinganalysis['proteinunit'] = foodnutritincontent[0].proteinyunit
                eatinganalysis['fatintake'] = round(result*foodnutritincontent[0].fatcontent, 2)
                eatinganalysis['fatunit'] = foodnutritincontent[0].fatyunit
                eatinganalysis['fiberintake'] = round(result*foodnutritincontent[0].fibercontent, 2)
                eatinganalysis['fiberunit'] = foodnutritincontent[0].fiberyunit
                eatinganalysis['carbohydrateintake'] = round(result*foodnutritincontent[0].carbohydratecontent, 2)
                eatinganalysis['carbohydrateunit'] = foodnutritincontent[0].carbohydrateyunit
                eatinganalysis['vitaminaintake'] = round(result*foodnutritincontent[0].vitaminacontent, 2)
                eatinganalysis['vitaminaunit'] = foodnutritincontent[0].vitaminaunit
                eatinganalysis['vitaminb1intake'] = round(result*foodnutritincontent[0].vitaminb1content, 2)
                eatinganalysis['vitaminb1unit'] = foodnutritincontent[0].vitaminb1unit
                eatinganalysis['vitaminb2intake'] = round(result*foodnutritincontent[0].vitaminb2content, 2)
                eatinganalysis['vitaminb2unit'] = foodnutritincontent[0].vitaminb2unit
                eatinganalysis['vitaminb6intake'] = round(result*foodnutritincontent[0].vitaminb6content, 2)
                eatinganalysis['vitaminb6unit'] = foodnutritincontent[0].vitaminb6unit
                eatinganalysis['vitaminb12intake'] = round(result*foodnutritincontent[0].vitaminb12content, 2)
                eatinganalysis['vitaminb12unit'] = foodnutritincontent[0].vitaminb12unit
                eatinganalysis['vitamincintake'] = round(result*foodnutritincontent[0].vitaminccontent, 2)
                eatinganalysis['vitamincunit'] = foodnutritincontent[0].vitamincunit
                eatinganalysis['vitamindintake'] = round(result*foodnutritincontent[0].vitamindcontent, 2)
                eatinganalysis['vitamindunit'] = foodnutritincontent[0].vitamindunit
                eatinganalysis['vitamineintake'] = round(result*foodnutritincontent[0].vitaminecontent, 2)
                eatinganalysis['vitamineunit'] = foodnutritincontent[0].vitamineunit
                eatinganalysis['vitaminkintake'] = round(result*foodnutritincontent[0].vitaminkcontent, 2)
                eatinganalysis['vitaminkunit'] = foodnutritincontent[0].vitaminkunit
                eatinganalysis['nicotinicacidintake'] = round(result*foodnutritincontent[0].nicotinicacidcontent, 2)
                eatinganalysis['nicotinicacidunit'] = foodnutritincontent[0].nicotinicacidunit
                eatinganalysis['folateintake'] = round(result*foodnutritincontent[0].folatecontent, 2)
                eatinganalysis['folateunit'] = foodnutritincontent[0].folateunit
                eatinganalysis['sodiumintake'] = round(result*foodnutritincontent[0].sodiumcontent, 2)
                eatinganalysis['sodiumunit'] = foodnutritincontent[0].sodiumunit
                eatinganalysis['calciumintake'] = round(result*foodnutritincontent[0].calciumcontent, 2)
                eatinganalysis['calciumunit'] = foodnutritincontent[0].calciumunit
                eatinganalysis['ironintake'] = round(result*foodnutritincontent[0].ironcontent, 2)
                eatinganalysis['ironunit'] = foodnutritincontent[0].ironunit
                eatinganalysis['potassiumintake'] = round(result*foodnutritincontent[0].potassiumcontent, 2)
                eatinganalysis['potassiumunit'] = foodnutritincontent[0].potassiumunit
                eatinganalysis['zincintake'] = round(result*foodnutritincontent[0].zinccontent, 2)
                eatinganalysis['zincunit'] = foodnutritincontent[0].zincunit
                eatinganalysis['magnesiumintake'] = round(result*foodnutritincontent[0].magnesiumcontent, 2)
                eatinganalysis['magnesiumunit'] = foodnutritincontent[0].magnesiumunit
                eatinganalysis['copperintake'] = round(result*foodnutritincontent[0].coppercontent, 2)
                eatinganalysis['copperunit'] = foodnutritincontent[0].copperunit
                eatinganalysis['chomuimintake'] = round(result*foodnutritincontent[0].chromiumcontent, 2)
                eatinganalysis['chomuimunit'] = foodnutritincontent[0].chromiumunit
                eatinganalysis['mangaesiumintake'] = round(result*foodnutritincontent[0].mangaesscontent, 2)
                eatinganalysis['mangaesiumunit'] = foodnutritincontent[0].mangaessunit
                eatinganalysis['molybdenumintake'] = round(result*foodnutritincontent[0].molybdenumcontent, 2)
                eatinganalysis['molybdenumunit'] = foodnutritincontent[0].molybdenumunit
                eatinganalysis['iodineintake'] = round(result*foodnutritincontent[0].iodinecontent, 2)
                eatinganalysis['iodineunit'] = foodnutritincontent[0].iodineunit
                eatinganalysis['phosphrusintake'] = round(result*foodnutritincontent[0].phosphruscontent, 2)
                eatinganalysis['phosphrusunit'] = foodnutritincontent[0].phosphrusunit
                eatinganalysis['seleniumintake'] = round(result*foodnutritincontent[0].seleniumcontent, 2)
                eatinganalysis['seleniumunit'] = foodnutritincontent[0].seleniumunit
                eatinganalysis['fluorineintake'] = round(result*foodnutritincontent[0].fluorinecontent, 2)
                eatinganalysis['fluorineunit'] = foodnutritincontent[0].fluorineunit
                eatinganalysis['cholesterolintake'] = round(result*foodnutritincontent[0].cholesterolcontent, 2)
                eatinganalysis['cholesterolunit'] = foodnutritincontent[0].cholesterounit
                eatinganalysis['saturatedintake'] = round(result*foodnutritincontent[0].saturatedfattyacidcontent, 2)
                eatinganalysis['saturatedunit'] = foodnutritincontent[0].saturatedfattyacidunit
                eatinganalysis['acidregurgitationintake'] = round(result*foodnutritincontent[0].acidregurgitationcontent, 2)
                eatinganalysis['acidregurgitationunit'] = foodnutritincontent[0].acidregurgitationunit
                eatinganalysis['biotinintake'] = round(result*foodnutritincontent[0].biotincontent, 2)
                eatinganalysis['biotinunit'] = foodnutritincontent[0].biotinunit
                eatinganalysis['cholineintake'] = round(result*foodnutritincontent[0].cholinecontent, 2)
                eatinganalysis['cholineunit'] = foodnutritincontent[0].cholineunit
                eatinganalysis['caroteneintake'] = round(result*foodnutritincontent[0].carotenecontent, 2)
                eatinganalysis['caroteneunit'] = foodnutritincontent[0].caroteneunit
                TbEatinganalysis.objects.create(temp_eatingrecordid=tbdietaryrecords, **eatinganalysis)
            return tbdietaryrecords

class TbDoctorexpertiseinfoSerializer(serializers.ModelSerializer):
    """
    医生专长信息表
    """
    class Meta:
        model = TbDoctorexpertiseinfo
        fields = (
            'doctorexpertiseid', 'doctorexpertisetitle', 'doctorexpertiseexplain', 'temp_doctorexptypeid',
        )

class TbDoctorexpertisetypeSerializer(serializers.ModelSerializer):
    """
    医生专长分类代码表
    """
    class Meta:
        model = TbDoctorexpertisetype
        fields = (
            'doctorexptypeid', 'doctorexptypename', 'doctorexptypecode', 'doctorexptypeexplain',
        )

class TbEatinganalysisSerializer(serializers.ModelSerializer):
    """
    饮食状况分析表
    """
    class Meta:
        model = TbEatinganalysis
        #fields = (
        #    'eatinganalysisid', 'energyintake', 'moistureintake', 'proteinintake', 'fatintake',
        #    'fiberintake', 'carbohydrateintake', 'vitaminaintake', 'vitaminb1intake', 'vitaminb2intake',
        #    'vitaminb6intake', 'vitaminb12intake', 'vitamincintake', 'vitamindintake', 'vitamineintake',
        #    'vitaminkintake', 'nicotinicacidintake', 'folateintake', 'sodiumintake', 'calciumintake',
        #    'ironintake', 'potassiumintake', 'zincintake', 'magnesiumintake', 'copperintake',
        #    'chomuimintake', 'mangaesiumintake', 'molybdenumintake', 'iodineintake', 'phosphrusintake',
        #    'seleniumintake', 'fluorineintake', 'cholesterolintake', 'saturatedintake', 'acidregurgitationintake',
        #    'biotinintake', 'cholineintake', 'temp_eatingrecordid',
        #)

class TbEatingpreferrecordsSerializer(serializers.ModelSerializer):
    """
    饮食偏好记录表
    """
    additemtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbEatingpreferrecords
        fields = (
            'eatingpreferid', 'foodtypename', 'foodname', 'preference', 'averageintake',
            'temp_foodnutritionid', 'temp_userid', 'eatingoftenstarttime', 'eatingoftenovertime', 'temp_locationinfoid',
            'additemtime', 'currentlypreferflag',
        )

class TbEatingsetmealinfoSerializer(serializers.ModelSerializer):
    """
    饮食套餐信息表
    """
    class Meta:
        model = TbEatingsetmealinfo
        fields = (
            'setmealinfoid', 'foodtypecontent', 'setmealname', 'setmealexplain',

        )


class TbExercisetypeSerializer(serializers.ModelSerializer):
    """
    运动类型名
    """
    class Meta:
        model = TbExercisetype
        fields = (
            'exercisetypeid', 'exercisetypename', 'exercisetypeexplain', 'exercisetypecode', 'exercisetyperemarks',
        )



class TbExerciseinfoSerializer(serializers.ModelSerializer):
    """
    运动实体信息表
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbExerciseinfo
        fields = (
            'exerciseid', 'exercisename', 'exercisetypename', 'energywaste', 'exercisetip',
            'exerciseaffect', 'temp_picturelocationid', 'temp_exercisetypeid',
        )

class TbExercisepreferrecordsSerializer(serializers.ModelSerializer):
    """
    运动偏好记录表
    """
    additemtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbExercisepreferrecords
        fields = (
            'exercisepreferenceid', 'exercisetype', 'exercisename', 'exercisedescribe', 'temp_exerciseid',
            'temp_userid', 'temp_locationinfoid', 'additemtime', 'currentlypreferflag',
        )

class TbExpendedhealthpropertiesSerializer(serializers.ModelSerializer):
    """
    扩张健康属性表
    """
    class Meta:
        model = TbExpendedhealthproperties



class TbFoodfeatureSerializer(serializers.ModelSerializer):
    """
    饮食特征信息表
    """
    latelymaintentime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbFoodfeature
        #fields = (
        #    'eatingfeatureid', 'eatinghabitsdetermine', 'temp_userid', 'eatinghabitanalysis', 'averageenergyintake',
        #    'averagemoistureintake', 'averageproteinintake', 'averagefatintake', 'averagefiberintake', 'averagecarbohydrateintake',
        #    'averagevitaminaintake', 'averagevitaminb1intake', 'averagevitaminb2intake', 'averagevitaminb6intake', 'averagevitaminb12intake',
        #    'averagevitamincintake', 'averagevitamindintake', 'averagevitamineintake', 'averagevitaminkintake', 'averagenicotinicacidintake',
        #    'averagefolateintake', 'averagesodiumintake', 'averagecalciumintake', 'averageironintake', 'averagepotassiumintake',
        #    'averagezincintake', 'averagemagnesiumintake', 'averagecopperintake', 'averagechomuimintake', 'averagemangaesiumintake',
        #    'averagemolybdenumintake', 'averageiodineintake', 'averagephosphrusintake', 'averageseleniumintake', 'averagefluorineintake',
        #    'averagecholesterolintake', 'averagesaturatedintake', 'averageacidregurgitationintake', 'averagebiotinintake', 'averagecholineintake',
        #    'temp_unitattributeid',
        #)

class TbFoodnutritionelementSerializer(serializers.ModelSerializer):
    """
    常见食物营养成分元素表
    """
    class Meta:
        model = TbFoodnutritionelement


class TbFoodnutritioncontentSerializer(serializers.ModelSerializer):
    """
    食物营养含量信息表
    """
    class Meta:
        model = TbFoodnutritioncontent
        #fields = (
        #    'foodnutritionid', 'foodenergy', 'foodmoisture', 'proteincontent', 'fatcontent',
        #    'fibercontent', 'carbohydratecontent', 'vitaminacontent', 'vitaminb1content', 'vitaminb2content',
        #    'vitaminb6content', 'vitaminb12content', 'vitaminccontent', 'vitamindcontent', 'vitaminecontent',
        #    'vitaminkcontent', 'nicotinicacidcontent', 'folatecontent', 'sodiumcontent', 'calciumcontent',
        #    'ironcontent', 'potassiumcontent', 'zinccontent', 'magnesiumcontent', 'coppercontent',
        #    'chromiumcontent', 'mangaesscontent', 'molybdenumcontent', 'iodinecontent', 'phosphruscontent',
        #    'seleniumcontent', 'fluorinecontent', 'cholesterolcontent', 'saturatedfattyacidcontent', 'acidregurgitationcontent',
        #    'biotincontent', 'cholinecontent', 'temp_unitattributeid',
        #)

class TbHealthindicatorinfoSerializer(serializers.ModelSerializer):
    """
    健康指标信息表
    """
    class Meta:
        model = TbHealthindicatorinfo
        fields = (
            'healthindicatorid', 'healthindicatorname', 'healthindicatorvalue', 'healthindicatorchange', 'indicatorchangeexplain',
            'temp_healthtrendid',
        )

class TbHealthknowledgetypeSerializer(serializers.ModelSerializer):
    """
    养生知识类别表
    """
    class Meta:
        model = TbHealthknowledgetype
        fields = (
            'healthknowltypeid', 'healthknowltypename', 'healthknowltypecode', 'healthknowltypeexp', 'healthknowltyperemarks',
        )

class TbHealthknowledgelimitedSerializer(serializers.ModelSerializer):
    """
    养生知识限定条件表
    """


    class Meta:
        model = TbHealthknowledgelimited
        fields = (
            'healthknowllimitedid', 'healthknowllimitedattname', 'healthknowllimitedstatus', 'healthknowllimitedstatuslevel', 'temp_healthknowledgeid',
            'healthknowllimitedexp', 'healthknowllimitedremarks', 'healthknowllimitedvalue',
        )


class TbHealthsuggestionsSerializer(serializers.ModelSerializer):
    """
    健康建议表
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbHealthsuggestions
        fields = (
            'healthsuggestid', 'healthsuggestcontent', 'healthsuggesttitle', 'healthsuggestremarks', 'temp_healthsuggtypeid',
            'healthsuggestflag', 'healthsuggestcode', 'temp_picturelocationid',
        )



class TbHealthsuggestlimitedSerializer(serializers.ModelSerializer):
    """
    健康建议限定条件表
    """

    class Meta:
        model = TbHealthsuggestlimited
        fields = (
            'healthsuggestlimitedid', 'suggestlimitedattrname', 'suggestlimitedstatus', 'suggestlimitedstatuslevel',
            'suggestlimitedexplain', 'suggestlimitedremarks', 'suggestlimitedvalue',
        )


class TbHealthsuggtypeSerializer(serializers.ModelSerializer):
    """
    健康建议类别表
    """
    class Meta:
        model = TbHealthsuggtype
        fields = (
            'healthsuggtypeid', 'healthsuggtypename', 'healthsuggtypecode', 'suggclassifyexpla', 'healthsuggtyperemarks',
        )

class TbHealthtrendrecordsSerializer(serializers.ModelSerializer):
    """
    记录用户健康趋势
    """
    healthanalysistime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbHealthtrendrecords
        fields = (
            'healthtrendid', 'heaanalysistitle', 'healthanalysistime', 'healthtrendanalysiresult', 'temp_healthknowledgeid',
            'healthtrendanalysisremarks', 'temp_userid',
        )



class TbHealthsuggestionsmappSerializer(serializers.ModelSerializer):
    """
    用户健康建议映射表
    """
    healthsuggesttime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbHealthsuggestionsmapp
        fields = (
            'healthsuggestmappid', 'healthsuggcontent', 'temp_userid', 'temp_healthsuggestid', 'healthsuggestreason',
            'healthsuggesttime', 'healthsuggestremarks', 'checktosee',
        )

class TbHealthsuggestionsmapptwoSerializer(serializers.ModelSerializer):
    """
    用户健康建议映射表
    """
    healthsuggesttime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    #temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbHealthsuggestionsmapp
        fields = (
            'healthsuggestmappid', 'healthsuggcontent', 'temp_userid', 'temp_healthsuggestid', 'healthsuggestreason',
            'healthsuggesttime', 'healthsuggestremarks', 'checktosee',
        )


class TbHealthwarningtypeSerializer(serializers.ModelSerializer):
    """
    健康预警类别表
    """


    class Meta:
        model = TbHealthwarningtype
        fields = (
            'healthwarningtypeid', 'healthwarningname', 'healthwarningtypecode', 'healthwarningtypeexp', 'healthwarningtyperemarks',
        )


class TbHealthwarningmessSerializer(serializers.ModelSerializer):
    """
    健康预警信息表
    """
    class Meta:
        model = TbHealthwarningmess
        fields = (
            'healthwarningmessid', 'healthwarningtitle', 'healthwarningcontent', 'healthwarningremarks', 'temp_healthsuggestid',
            'temp_healthwarningtypeid',
        )



class TbUserhealthattrmappSerializer(serializers.ModelSerializer):
    """
    用户健康属性映射表
    """
    updatetime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbUserhealthattrmapp




class TbUserhealthwarningmappSerializer(serializers.ModelSerializer):
    """
    用户预警映射表
    """
    healthwarningtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')

    class Meta:
        model = TbUserhealthwarningmapp
        fields = (
            'userhealthwarningid', 'healthwarningcontent', 'healthwarningtime', 'healthwarningreason', 'temp_userid',
            'healthwarningremarks', 'temp_healthwarningmessid', 'checktosee',
        )



class TbHospitaldoctorrelSerializer(serializers.ModelSerializer):
    """
    医院医生关系表
    """
    temp_doctorid = serializers.SlugField(validators=[UniqueValidator(queryset=TbHospitaldoctorrel.objects.all())])
    class Meta:
        model = TbHospitaldoctorrel
        fields = (
            'hospitaldocrelid', 'temp_hospitalid', 'temp_doctorid', 'temp_hospitalofficeid', 'workduty',
        )
        # extra_kwargs = {
        #     'temp_doctorid': {'required': False, 'read_only': True},
        #     'hospitaldocrelid': {'required': False, 'read_only': True},
        #
        # }
class TbHospitalinfoSerializer(serializers.ModelSerializer):
    """
    医院信息表
    """
    temp_picturelocationid = serializers.ImageField(read_only=True, source='temp_picturelocationid.originalpicturepath', allow_null=True)
    class Meta:
        model = TbHospitalinfo
        fields = (
            'hospitalid', 'hospitalname', 'hospitalexplain', 'temp_locationinfoid', 'hospitalrank',
            'temp_adminisareaid', 'temp_picturelocationid',
        )



class TbHospitalofficesinfoSerializer(serializers.ModelSerializer):
    """
    医院科室信息表
    """
    class Meta:
        model = TbHospitalofficesinfo
        fields = (
            'hospitalofficeid', 'hospitalofficename', 'hospitalofficeexplain',
        )

class TbIdentificationissuessSerializer(serializers.ModelSerializer):
    """
    体质辨识问卷项目表
    """
    class Meta:
        model = TbIdentificationissuess
        fields = (
            'identifyissueid', 'temp_physiqueinfoid', 'identifyissuecontent', 'identifyissueremarks',
        )

class TbIdentifychoicesSerializer(serializers.ModelSerializer):
    """
    体质辨识选项表
    """
    class Meta:
        model = TbIdentifychoices
        fields = (
            'identifychoiceid', 'identifychoicevalue', 'scriptdescribe',
        )

class TbIdentifydiseaserelSerializer(serializers.ModelSerializer):
    """
    记录体质和疾病的关系
    """
    class Meta:
        model = TbIdentifydiseaserel
        fields = (
            'identifydirelid', 'temp_physiqueinfoid', 'temp_commondiseaseid', 'identifydirelexplain',
        )

class TbIntelligentdeviceinfoSerializer(serializers.ModelSerializer):
    """
    智能设备基本信息表
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbIntelligentdeviceinfo
        fields = (
            'intelligentdeviceid', 'intelligentdevicetype', 'intelligentdevicename', 'intelligentdeviceweight', 'intelligentdevicecolor',
            'intelligentdevicefunction', 'intelligentdevicecode', 'temp_picturelocationid',
        )

class TbLocationinfoSerializer(serializers.ModelSerializer):
    """
    地理位置相关信息
    """
    class Meta:
        model = TbLocationinfo
        fields = (
            'locationinfoid', 'locationlongitude', 'locationlatitude', 'reallocation', 'locationremarks',
            'locationprovince', 'locationcity', 'locationclassify', 'locationcounty',
        )

class TbManagerSerializer(serializers.ModelSerializer):
    """
    管理员实体，记录管理员基本信息
    """
    class Meta:
        model = TbManager
        fields = (
            'managerid', 'managername', 'managerpassword', 'managerunit',
        )


class TbMeasurementunitSerializer(serializers.ModelSerializer):
    """
    项目中用到的计量单位在此记录
    """

    class Meta:
        model = TbMeasurementunit
        fields = (
            'unitattributeid', 'unitattributename', 'unitlevel', 'unitname', 'hexadecimal',
            'unitremarks',
        )


class TbMedicalhistoryrecordsSerializer(serializers.ModelSerializer):
    """
    记录用户病史
    """
    treatmenttime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbMedicalhistoryrecords
        fields = (
            'medicalhistoryrecordid', 'diseasetype', 'diseasename', 'diseaseseverity', 'treatmentinfo',
            'treatmentdoctor', 'treatmentunit', 'treatmentlocation', 'treatmentresult', 'recoverydegree',
            'treatmenttime', 'treatmentremarks', 'temp_userid', 'temp_doctorid', 'temp_medicineuseinfoid',
            'temp_commondiseaseid',
        )

class TbMedicineinfoSerializer(serializers.ModelSerializer):
    """
    中药信息表
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbMedicineinfo
        fields = (
            'chinesemedicineid', 'medicinename', 'medicinegeneraltype', 'medicinetoxicity', 'medicinesubtype', 'medicineproperty',
            'medicinetaste', 'indicationsfunction', 'channeltropism', 'clinicalapplication', 'medicinegenera',
            'prescriptionname', 'generaldosage', 'generalusage', 'withmedicine', 'comment',
            'prescriptionsexample', 'medicineremarks', 'medicinecode', 'temp_picturelocationid',
        )

class TbMedicineprescriptionSerializer(serializers.ModelSerializer):
    """
    中药方剂表
    """

    class Meta:
        model = TbMedicineprescription
        fields = (
            'medicineprescriptionid', 'medicineprescriptionname', 'prescriptionindications', 'prescriptionusage', 'prescriptionmethod', 'prescriptioncharacters',
            'prescriptionspecification', 'prescriptionstore', 'prescriptioncontraindicat', 'prescriptiontheories', 'prescriptionextract',
            'prescriptionremarks', 'prescriptiontag',
        )


class TbMedicineprescriptionmappSerializer(serializers.ModelSerializer):
    """
    药品方剂映射表
    """


    class Meta:
        model = TbMedicineprescriptionmapp
        fields = (
            'medprescriptmappid', 'temp_chinesemedicineid', 'temp_medicineprescriptionid', 'medicineamount', 'medprescriptmappremarks',
        )


class TbMedicineuseinfoSerializer(serializers.ModelSerializer):
    """
    记录用户诊疗过程中的用药信息
    """
    class Meta:
        model = TbMedicineuseinfo
        fields = (
            'medicineuseinfoid', 'medicineusetype', 'medicineusename', 'medicineusedose', 'medicineuseremarks',
            'temp_tcmexaminationid', 'temp_unitattributeid', 'prescriptiontag', 'temp_chinesemedicineid',
        )


class TbMovementdetailrecordsSerializer(serializers.ModelSerializer):
    """
    运动详细过程记录表
    """
    movementstarttime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    movementstoptime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbMovementdetailrecords


class TbMycollectionSeria(serializers.ModelSerializer):
    """
    我的收藏
    """
    class Meta:
        model = TbMycollection
        fields = (
            'mycollectionid', 'collectionclass', 'collectioncode', 'temp_userid',
        )



class TbPhoneappinfoSerializer(serializers.ModelSerializer):
    """
    手机应用实体部分信息
    """
    class Meta:
        model = TbPhoneappinfo
        fields = (
            'appinfoid', 'apptype', 'appname', 'apptag', 'appotherinfo',
        )

class TbPhoneinfoSerializer(serializers.ModelSerializer):
    """
    手机监控特征信息表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbPhoneinfo
        fields = (
            'phoneinfoid', 'phoneuniqunum', 'phonenum', 'temp_userid',
        )

class TbPhonemonitorrecordsSerializer(serializers.ModelSerializer):
    """
    手机监控记录表
    """
    appopentime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    appclosetime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    recordproducttime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbPhonemonitorrecords
        fields = (
            'phoneappmonitorrecordid', 'temp_appinfoid', 'appopentime', 'appclosetime', 'appusetime',
            'temp_locationinfoid', 'temp_phoneinfoid', 'recordproducttime',
        )

class TbPhonepreferuserecordsSerializer(serializers.ModelSerializer):
    """
    手机使用偏好记录
    """
    additemtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbPhonepreferuserecords
        fields = (
            'phonepreferuseid', 'oftenusebeginat', 'oftenuseovertime', 'temp_locationinfoid', 'temp_appinfoid',
            'temp_userid', 'temp_amountstdid', 'additemtime', 'currentlypreferflag',
        )

class TbPhysiqueinfoSerializer(serializers.ModelSerializer):
    """
    体质信息表
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbPhysiqueinfo
        fields = (
            'physiqueinfoid', 'tablescoreheight', 'tablescorelow', 'switchscoreheight', 'switchscorelow',
            'generacharacter', 'shapefeature', 'commonmanifest', 'mentalcharacter', 'incidencetendency',
            'adaptivecapacity', 'physicaltypename', 'physicaltypecode', 'adjustmethod', 'multiplepeople',
            'physicalinterpretation', 'physicalreason', 'physicaladjustmethod', 'foodallowtaboo',
            'temp_picturelocationid',
        )



class TbRecommendedconditionsmappSerializer(serializers.ModelSerializer):
    """
    健康建议条件限定映射表
    """
    class Meta:
        model = TbRecommendedconditionsmapp


class TbSetmealfoodmappSerializer(serializers.ModelSerializer):
    """
    套餐食物映射表
    """
    class Meta:
        model = TbSetmealfoodmapp
        fields = (
            'mealfoodmapid', 'temp_commonfoodid', 'temp_setmealinfoid', 'mealfoodmapremarks',
        )

class TbSleepdetailprocessrecordsSerializer(serializers.ModelSerializer):
    """
    睡眠详细过程记录表
    """
    sleepstatusbegintime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    sleepstatusovertime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbSleepdetailprocessrecords


class TbSleepinforecordsSerializer(serializers.ModelSerializer):
    """
    记录用户睡眠信息
    """
    sleepbegin = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    sleepover = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    sleeprecorduptime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbSleepinforecords
        fields = (
            'sleeprecordid', 'airhumidity', 'ambienttemperature', 'ambientnoise', 'sleepbegin',
            'sleepover', 'deepsleeptime', 'shallowsleeptime', 'sleepremarks', 'sleeprecorduptime',
            'temp_userid', 'temp_locationinfoid', 'waketimes', 'temp_intelligentdeviceid', 'intelligentdevicecode',
            'sleepuploadflag', 'awaketime',
        )
    def create(self, validated_data):
        with transaction.atomic():
            temp_userid = validated_data['temp_userid'].userid
            sleepbegin = validated_data['sleepbegin']
            validator = TbSleepinforecords.objects.filter(temp_userid=temp_userid, sleepbegin=sleepbegin)

            sleepinforecords = None
            if validator:
                validator[0].airhumidity = validated_data['airhumidity']
                validator[0].ambienttemperature = validated_data['ambienttemperature']
                validator[0].ambientnoise = validated_data['ambientnoise']
                validator[0].sleepbegin = validated_data['sleepbegin']
                validator[0].sleepover = validated_data['sleepover']
                validator[0].deepsleeptime = validated_data['deepsleeptime']
                validator[0].shallowsleeptime = validated_data['shallowsleeptime']
                validator[0].sleepremarks = validated_data['sleepremarks']
                validator[0].sleeprecorduptime = validated_data['sleeprecorduptime']
                validator[0].temp_userid = validated_data['temp_userid']
                validator[0].temp_locationinfoid = validated_data['temp_locationinfoid']
                validator[0].temp_locationinfoid = validated_data['temp_locationinfoid']
                validator[0].waketimes = validated_data['waketimes']
                validator[0].temp_intelligentdeviceid = validated_data['temp_intelligentdeviceid']
                validator[0].intelligentdevicecode = validated_data['intelligentdevicecode']
                validator[0].sleepuploadflag = validated_data['sleepuploadflag']
                validator[0].awaketime = validated_data['awaketime']
                validator[0].save()
                sleepinforecords = validator[0]
            else:
                sleepinforecords = TbSleepinforecords.objects.create(**validated_data)
            return sleepinforecords


class TbSleeppreferrecordsSerializer(serializers.ModelSerializer):
    """
    记录用户睡眠偏好，如：睡眠时间，可向用户推送相关信息
    """
    sleepfeatureaddtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbSleeppreferrecords
        fields = (
            'sleeppreferid', 'prefersleepbeginat', 'prefersleepoverat', 'temp_locationinfoid', 'temp_userid',
            'sleepfeatureaddtime', 'currentlypreferflag',
        )


class TbSleepstatuscategorySerializer(serializers.ModelSerializer):
    """
    睡眠状态类别表
    """
    class Meta:
        model = TbSleepstatuscategory



class TbSportinforecordsSerializer(serializers.ModelSerializer):
    """
    记录用户运动数据
    """
    sportbegintime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    sportovertime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    sportrecorduptime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbSportinforecords
        fields = (
            'sportrecordid', 'walkstepnumber', 'runstepnumber', 'walkdistance', 'rundistance',
            'calorieconsumption', 'sportbegintime', 'sportovertime', 'sportrecorduptime', 'sportinforemarks',
            'sportanalysis', 'temp_userid', 'temp_locationinfoid', 'sport_mode', 'temp_intelligentdeviceid',
            'intelligentdevicecode', 'uploadflag', 'restingcalorieconsume', 'movecalorieconsume', 'crawledfloor',
            'fallitems', 'activeduration', 'longestactiveduration', 'longestidleduration', 'temp_exerciseid',
        )

    def create(self, validated_data):
        with transaction.atomic():
            temp_userid = validated_data['temp_userid'].userid
            sportbegintime = validated_data['sportbegintime']
            validator = TbSportinforecords.objects.filter(temp_userid=temp_userid, sportbegintime=sportbegintime)
            sportinforecords = None
            if validator:
                validator[0].walkstepnumber = validated_data['walkstepnumber']
                validator[0].runstepnumber = validated_data['runstepnumber']
                validator[0].walkdistance = validated_data['walkdistance']
                validator[0].rundistance = validated_data['rundistance']
                validator[0].calorieconsumption = validated_data['calorieconsumption']
                validator[0].sportbegintime = validated_data['sportbegintime']
                validator[0].sportovertime = validated_data['sportovertime']
                validator[0].sportrecorduptime = validated_data['sportrecorduptime']
                validator[0].sportinforemarks = validated_data['sportinforemarks']
                validator[0].sportanalysis = validated_data['sportanalysis']
                validator[0].temp_userid = validated_data['temp_userid']
                validator[0].temp_locationinfoid = validated_data['temp_locationinfoid']
                validator[0].sport_mode = validated_data['sport_mode']
                validator[0].temp_intelligentdeviceid = validated_data['temp_intelligentdeviceid']
                validator[0].intelligentdevicecode = validated_data['intelligentdevicecode']
                validator[0].uploadflag = validated_data['uploadflag']
                validator[0].restingcalorieconsume = validated_data['restingcalorieconsume']
                validator[0].movecalorieconsume = validated_data['movecalorieconsume']
                validator[0].crawledfloor = validated_data['crawledfloor']
                validator[0].fallitems = validated_data['fallitems']
                validator[0].activeduration = validated_data['activeduration']
                validator[0].longestactiveduration = validated_data['longestactiveduration']
                validator[0].longestidleduration = validated_data['longestidleduration']
                validator[0].temp_exerciseid = validated_data['temp_exerciseid']
                validator[0].save()
                sportinforecords = validator[0]
            else:
                sportinforecords = TbSportinforecords.objects.create(**validated_data)
            return sportinforecords



class TbStatisticofclickSerializer(serializers.ModelSerializer):
    """
    点击量统计表
    """
    class Meta:
        model = TbStatisticofclick
        fields = (
            'statisticclickid', 'clickclass', 'clickitem', 'praiseyn', 'statisticclickremarks',
            'temp_userid', 'ipaddress',
        )

class TbSupervisorylevelSerializer(serializers.ModelSerializer):
    """
    管理员管理权限、范围
    """
    class Meta:
        model = TbSupervisorylevel
        fields = (
            'superlevelid', 'temp_managerid', 'temp_adminisareaid', 'managerrank',
        )

class TbTcmdcotorsinfoSerializer(serializers.ModelSerializer):
    """
    中医专家信息表
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbTcmdcotorsinfo
        fields = (
            'doctorid', 'doctorname', 'doctorsex', 'doctorage', 'professionalrands',
            'doctorworktime', 'doctorsynopsis', 'researcharea', 'researchfindings', 'temp_adminisareaid',
            'temp_doctorexpertiseid', 'doctorcode', 'temp_picturelocationid',
        )

class TbTcmdiagnosisobjSerializer(serializers.ModelSerializer):
    """
    诊断对象表
    """
    class Meta:
        model = TbTcmdiagnosisobj
        fields = (
            'diagnosisobjid', 'diagnosisobjname', 'diagnosisobjexplain', 'temp_diagnosistypeid',
        )

class TbTcmdiagnosistypeSerializer(serializers.ModelSerializer):
    """
    中医诊断分类表
    """
    class Meta:
        model = TbTcmdiagnosistype
        fields = (
            'diagnosistypeid', 'diagnosistypename', 'diagnosistypecode', 'diagnosistypeexplain',
        )
class TbTcmhealthknowledgeSerializer(serializers.ModelSerializer):
    """
    记录中医养生知识发布细节
    """
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    #temp_healthknowltypeid = TbHealthknowledgetypeSerializer()
    exersuggtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbTcmhealthknowledge
        fields = (
            'healthknowledgeid', 'healthknowledgetitle', 'healthknowledgecontent', 'exersuggtime', 'temp_managerid',
            'healthknowledgeremarks', 'temp_healthknowltypeid', 'healthknowledgecode', 'healthknowledgeflag', 'temp_picturelocationid',
        )




class TbUseranswerrecordsSerializer(serializers.ModelSerializer):
    """
    用户答题记录表
    """
    answertime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbUseranswerrecords
        fields = (
            'issuescoremappid', 'temp_identifyissueid', 'temp_identifychoiceid', 'temp_userid',
            'getscore', 'answerflag', 'answertime',
        )

class TbUserexercisefeatureSerializer(serializers.ModelSerializer):
    """
    用户运动的特征信息，如：身高等
    """
    class Meta:
        model = TbUserexercisefeature
        fields = (
            'exercisefeatureid', 'height', 'weight', 'steplength', 'runsteplength',
            'standardweight', 'datauptime', 'exercisefeatureremarks',  'motilityindex',
            'exercisehabitsdetermine', 'exercisehabitanalysis', 'averageexcitetime', 'exercisetypeprefer',
        )



class TbUserknowledgemappSerializer(serializers.ModelSerializer):
    """
    用户养生知识映射表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    healthknowledgetime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbUserknowledgemapp
        fields = (
            'userknowledgemappid', 'temp_userid', 'healthknowledgecontent', 'temp_healthknowledgeid', 'healthknowledgereason',
            'healthknowledgetime', 'healthknowledgeremarks',
        )



class TbUserreviewstatSerializer(serializers.ModelSerializer):
    """
    用户评论统计表
    """
    class Meta:
        model = TbUserreviewstat
        fields = (
            'userreviewstatid', 'userreviewclass', 'userreviewitem', 'userreviewcontent', 'userreviewremarks',
            'temp_userid',
        )



class TbUsersleepfeatureSerializer(serializers.ModelSerializer):
    """
    用户睡眠特征信息（包括睡眠环境：温度、湿度、噪声情况等）
    """
    latelymaintentime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbUsersleepfeature
        fields = (
            'sleepfeatureid', 'airhumidity', 'ambienttemperature', 'ambientnoise', 'bedtimehabits',
            'goodbedtimehabits', 'siestahabit',  'averagesleeptime', 'sleephabitdetermination',
            'sleepindex', 'sleephabitanalysis', 'temp_locationinfoid', 'latelymaintentime',
        )



class TbVariousindicatorstandardSerializer(serializers.ModelSerializer):
    """
    各类指标标准表
    """

    class Meta:
        model = TbVariousindicatorstandard
        fields = (
            'indicatorstandardid', 'indicatorname', 'indicatorcode', 'indicatorstatus', 'indicatorvalue',
            'indicatorremarks',
        )


class TbVariousindicatorlimitedSerializer(serializers.ModelSerializer):
    """
    各类标准限定表
    """

    class Meta:
        model = TbVariousindicatorlimited
        fields = (
            'indicatorlimitedid', 'temp_indicatorstandardid', 'indicatorstandardname', 'indicatorstandardstatus', 'indicatorstandardcode',
            'indicatorstandardvalue', 'indicatorstandardstatuslevel',
        )


class TbIndicatorusermappSerializer(serializers.ModelSerializer):
    """
    指标用户映射表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')

    class Meta:
        model = TbIndicatorusermapp
        fields = (
            'indicatorusermappid', 'temp_userid', 'temp_indicatorstandardid', 'userindicatorvalue', 'userindicatorexp',
            'userindicatorremarks',
        )



class TbWesmedicineexamitemSerializer(serializers.ModelSerializer):
    """
    西医体检项目表
    """
    class Meta:
        model = TbWesmedicineexamitem
        fields = (
            'westmedicineexamid', 'westmedicineitemname', 'wesmedicineitemexpl',
        )

class TbWtreatmentrecordsSerializer(serializers.ModelSerializer):
    """
    西医诊疗记录表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbWtreatmentrecords
        fields = (
            'wtreatmentrecordid', 'temp_westmedicineexamid', 'wesexamresultval', 'temp_userid',
        )



class TbExpertcollectSerilizer(serializers.ModelSerializer):
    """
    专家收藏表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    collectiontime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = TbExpertcollect
class TbHealthrecommendscollectionSerializer(serializers.ModelSerializer):
    """
    养生建议收藏表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    collectiontime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = TbHealthrecommendscollection

class TbHealthknowledgecollectionSerializer(serializers.ModelSerializer):
    """
    养生知识收藏表
    """
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    collectiontime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = TbHealthknowledgecollection


class TbFoodmedicinaleffecttypeSerializer(serializers.ModelSerializer):
    """
    食物药用功效类别
    """

    class Meta:
        model = TbFoodmedicinaleffecttype

class TbFoodmedicinalpropSerializer(serializers.ModelSerializer):
    """
    食物药用属性表
    """

    class Meta:
        model = TbFoodmedicinalprop


class TbFoodmedicinalpropmappSerializer(serializers.ModelSerializer):
    """
    食物药用属性映射表
    """

    class Meta:
        model = TbFoodmedicinalpropmapp