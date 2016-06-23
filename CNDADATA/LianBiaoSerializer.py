# -*- coding: utf-8 -*-
from models import *
from rest_framework import serializers
from serializers import *

class TbPicturelistsimpleSerializer(serializers.ModelSerializer):
    """
    图片列表
    """
    class Meta:
        model = TbPicturelist
        fields = (
            'originalpicturepath', 'picturename',

        )



class TbHospitaldoctorrellianbiaoSerializer(serializers.ModelSerializer):
    """
    医院医生关系表
    """
    temp_hospitalid = serializers.SlugRelatedField(queryset=TbHospitalinfo.objects.all(), slug_field='hospitalname')
    temp_doctorid = serializers.SlugRelatedField(queryset=TbTcmdcotorsinfo.objects.all(), slug_field='doctorname')
    temp_hospitalofficeid = serializers.SlugRelatedField(queryset=TbHospitalofficesinfo.objects.all(), slug_field='hospitalofficename')
    class Meta:
        model = TbHospitaldoctorrel



class DoctorviewSerializer(serializers.ModelSerializer):
    """
    中医专家信息视图
    """
    class Meta:
        model = Doctorview
        fields = (
            'doctorid', 'doctorname', 'doctorsex', 'doctorage', 'professionalrands',
            'doctorworktime', 'doctorsynopsis', 'researcharea', 'researchfindings', 'adminisareaprovince',
            'adminisareacity', 'adminisareacounty', 'doctorexptypename', 'doctorexpertisetitle', 'hospitalname',
            'hospitalofficename', 'workduty', 'temp_picturelocationid',
        )

class UserhealthknowledgeSerializer(serializers.ModelSerializer):
    """
    个人养生知识视图
    """
    temp_picturelistid = serializers.ImageField(read_only=True, source='temp_picturelistid.originalpicturepath', allow_null=True)
    healthknowledgetime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Userhealthknowledge
class TbHealthsuggestionscombinetwoSerializer(serializers.ModelSerializer):
    """
    健康建议表
    """
    temp_picturelocationid = serializers.ImageField(read_only=True, source='temp_picturelocationid.originalpicturepath', allow_null=True)
    temp_healthsuggtypeid = serializers.SlugRelatedField(queryset=TbHealthsuggtype.objects.all(), slug_field='healthsuggtypename')
    class Meta:
        model = TbHealthsuggestions
        fields = (
            'healthsuggestid', 'healthsuggestcontent', 'healthsuggesttitle', 'healthsuggestremarks', 'temp_healthsuggtypeid',
            'healthsuggestflag', 'healthsuggestcode', 'temp_picturelocationid',
        )



class TbHealthsuggestionsmappcombineSerializer(serializers.ModelSerializer):
    """
    用户健康建议映射表
    """
    healthsuggesttime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    temp_healthsuggestid = TbHealthsuggestionscombinetwoSerializer()
    class Meta:
        model = TbHealthsuggestionsmapp
        fields = (
            'healthsuggestmappid', 'healthsuggcontent', 'temp_userid', 'temp_healthsuggestid', 'healthsuggestreason',
            'healthsuggesttime', 'healthsuggestremarks', 'checktosee',
        )




class TbHealthtrendrecordsLianbiaoSerializer(serializers.ModelSerializer):
    """
    记录用户健康趋势
    """
    healthanalysistime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_healthknowledgeid = TbTcmhealthknowledgeSerializer()
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbHealthtrendrecords
        fields = (
            'healthtrendid', 'heaanalysistitle', 'healthanalysistime', 'healthtrendanalysiresult', 'temp_healthknowledgeid',
            'healthtrendanalysisremarks', 'temp_userid',
        )


class TbConstituteidentifyresultCombineSerializer(serializers.ModelSerializer):
    """
    体质辨识结果记录表
    """
    temp_physiqueinfoid = TbPhysiqueinfoSerializer()
    constituteidentifytime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    class Meta:
        model = TbConstituteidentifyresult
        fields = (
            'identifyresultid', 'temp_userid', 'temp_physiqueinfoid', 'constituteidentifytime', 'constituteidentifyremarks',
            'constituteidentifyresult', 'constituteldentifyflag',
        )


class TbHospitalinfoCombineSerializer(serializers.ModelSerializer):
    """
    医院信息表
    """
    temp_picturelocationid = serializers.ImageField(read_only=True, source='temp_picturelocationid.originalpicturepath', allow_null=True)
    temp_adminisareaid = TbAdminisareaSerializer()
    class Meta:
        model = TbHospitalinfo
        fields = (
            'hospitalid', 'hospitalname', 'hospitalexplain', 'temp_locationinfoid', 'hospitalrank',
            'temp_adminisareaid', 'temp_picturelocationid',
        )

class TbCommonfoodinfocombineSerializer(serializers.ModelSerializer):
    """
    常见食物信息表
    """
    temp_picturelocationid = serializers.ImageField(read_only=True, source='temp_picturelocationid.originalpicturepath', allow_null=True)
    temp_commonfoodtypeid = serializers.SlugRelatedField(queryset=TbCommonfoodtype.objects.all(), slug_field='commonfoodtypename')
    class Meta:
        model = TbCommonfoodinfo
        fields = (
            'commonfoodid', 'commonfoodname', 'temp_commonfoodtypeid', 'commonfoodexplain', 'temp_foodnutritionid',
            'temp_picturelocationid',
        )

class TbSetmealfoodmappcombineSerializer(serializers.ModelSerializer):
    """
    套餐食物映射表
    """
    temp_commonfoodid = TbCommonfoodinfocombineSerializer()
    class Meta:
        model = TbSetmealfoodmapp
        fields = (
            'mealfoodmapid', 'temp_commonfoodid', 'temp_setmealinfoid', 'mealfoodmapremarks',
        )


class TbSleepinforecordscombineSerializer(serializers.ModelSerializer):
    """
    记录用户睡眠信息
    """
    sleepbegin = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    sleepover = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    sleeprecorduptime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    sleepdetailprocessrecords = TbSleepdetailprocessrecordsSerializer(many=True)

    class Meta:
        model = TbSleepinforecords
        fields = (
            'sleeprecordid', 'airhumidity', 'ambienttemperature', 'ambientnoise', 'sleepbegin',
            'sleepover', 'deepsleeptime', 'shallowsleeptime', 'sleepremarks', 'sleeprecorduptime',
            'temp_userid', 'temp_locationinfoid', 'waketimes', 'temp_intelligentdeviceid', 'intelligentdevicecode',
            'sleepuploadflag', 'awaketime', 'sleepdetailprocessrecords',
        )
    def create(self, validated_data):
        with transaction.atomic():
            temp_userid = validated_data['temp_userid'].userid
            sleepbegin = validated_data['sleepbegin']
            validator = TbSleepinforecords.objects.filter(temp_userid=temp_userid, sleepbegin=sleepbegin)
            sleepinforecords = None
            if validator:
                sleepinforecords = validator[0]
            else:
                detaildatas = validated_data.pop('sleepdetailprocessrecords')
                waketimes = 0
                deepsleeptime = 0
                shallowsleeptime = 0
                for detaildata1 in detaildatas:
                    if detaildata1['temp_sleepstatuscategoryid'].sleepstatuscategoryid == 4:
                        deepsleeptime += detaildata1['sleepstatusduration']
                    elif detaildata1['temp_sleepstatuscategoryid'].sleepstatuscategoryid == 3:
                        shallowsleeptime += detaildata1['sleepstatusduration']
                    elif detaildata1['temp_sleepstatuscategoryid'].sleepstatuscategoryid == 2:
                        waketimes += 1
                    else:
                        deepsleeptime += 0
                        shallowsleeptime += 0
                        waketimes += 0
                validated_data['deepsleeptime'] = round(deepsleeptime, 1)
                validated_data['shallowsleeptime'] = round(shallowsleeptime, 1)
                validated_data['waketimes'] = waketimes
                sleepinforecords = TbSleepinforecords.objects.create(**validated_data)
                for detaildata2 in detaildatas:
                    TbSleepdetailprocessrecords.objects.create(temp_sleeprecordid=sleepinforecords, **detaildata2)
            return sleepinforecords


class TbHealthsuggestionscombineSerializer(serializers.ModelSerializer):
    """
    健康建议表
    """
    temp_healthsuggtypeid = serializers.SlugRelatedField(queryset=TbHealthsuggtype.objects.all(), slug_field='healthsuggtypename')
    #temp_picturelocationid = serializers.SlugRelatedField(queryset=TbPicturelist.objects.all(), slug_field='originalpicturepath')
    temp_picturelocationid = TbPicturelistsimpleSerializer()
    class Meta:
        model = TbHealthsuggestions
        fields = (
            'healthsuggestid', 'healthsuggestcontent', 'healthsuggesttitle', 'healthsuggestremarks', 'temp_healthsuggtypeid',
            'healthsuggestflag', 'healthsuggestcode', 'temp_picturelocationid',
        )


class TbRecommendedconditionsmappcombineSerializer(serializers.ModelSerializer):
    """
    健康建议条件限定映射表
    """
    temp_healthsuggestlimitedid = serializers.SlugRelatedField(queryset=TbHealthsuggestlimited.objects.all(), slug_field='suggestlimitedvalue')
    temp_healthsuggestid = TbHealthsuggestionscombineSerializer()
    class Meta:
        model = TbRecommendedconditionsmapp

# class TbHealthsuggestlimitedCombineSerializer(serializers.ModelSerializer):
#     """
#     健康建议限定条件表
#     """
#     temp_healthsuggestid = TbHealthsuggestionsSerializer()
#     class Meta:
#         model = TbHealthsuggestlimited
#         fields = (
#             'healthsuggestlimitedid', 'suggestlimitedattrname', 'suggestlimitedstatus', 'suggestlimitedstatuslevel', 'temp_healthsuggestid',
#             'suggestlimitedexplain', 'suggestlimitedremarks', 'suggestlimitedvalue',
#         )

class TbCommondiseaseinfocombineSerializer(serializers.ModelSerializer):
    """
    常见疾病信息表
    """
    temp_commonditypeid = serializers.SlugRelatedField(queryset=TbCommondiseasetype.objects.all(), slug_field='commonditypename')
    class Meta:
        model = TbCommondiseaseinfo
        fields = (
            'commondiseaseid', 'temp_commonditypeid', 'commondiname', 'diseaseexplain',
        )
class TbIdentifydiseaserelcombineSerializer(serializers.ModelSerializer):
    """
    记录体质和疾病的关系
    """
    temp_commondiseaseid = TbCommondiseaseinfocombineSerializer()
    class Meta:
        model = TbIdentifydiseaserel
        fields = (
            'identifydirelid', 'temp_physiqueinfoid', 'temp_commondiseaseid', 'identifydirelexplain',
        )
class TbHealthwarningmesscombineSerializer(serializers.ModelSerializer):
    """
    健康预警信息表
    """
    temp_healthsuggestid = TbHealthsuggestionsSerializer()
    temp_healthwarningtypeid = serializers.SlugRelatedField(queryset=TbHealthwarningtype.objects.all(), slug_field='healthwarningname')
    class Meta:
        model = TbHealthwarningmess
        fields = (
            'healthwarningmessid', 'healthwarningtitle', 'healthwarningcontent', 'healthwarningremarks', 'temp_healthsuggestid',
            'temp_healthwarningtypeid',
        )
class TbUserhealthwarningmappcombineSerializer(serializers.ModelSerializer):
    """
    用户预警映射表
    """
    healthwarningtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_userid = serializers.SlugRelatedField(queryset=TbUser.objects.all(), slug_field='username')
    temp_healthwarningmessid = TbHealthwarningmesscombineSerializer()
    class Meta:
        model = TbUserhealthwarningmapp
        fields = (
            'userhealthwarningid', 'healthwarningcontent', 'healthwarningtime', 'healthwarningreason', 'temp_userid',
            'healthwarningremarks', 'temp_healthwarningmessid', 'checktosee',
        )

class TbUserCombineSerializer(serializers.ModelSerializer):
    """
    用户实体，记录用户基本信息
    """
    last_login = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbUser
        extra_kwargs = {
            'temp_picturelocationid': {'required': False},
        }
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            password = validated_data['password']
            if picture_data:

                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    user = TbUser.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    user = TbUser.objects.create(**validated_data)

            else:
                user = TbUser.objects.create(**validated_data)
            user.set_password(password)
            user.save()
        return user
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.username = validated_data.get('username', instance.username)
            instance.usersex = validated_data.get('usersex', instance.usersex)
            instance.userage = validated_data.get('userage', instance.userage)
            #instance.password = validated_data.get('password', instance.password)
            instance.userphonenumber = validated_data.get('userphonenumber', instance.userphonenumber)
            instance.email = validated_data.get('email', instance.email)
            instance.name = validated_data.get('name', instance.name)
            instance.last_login = validated_data.get('last_login', instance.last_login)
            instance.is_admin = validated_data.get('is_admin', instance.is_admin)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.userrank = validated_data.get('userrank', instance.userrank)
            instance.userwroktype = validated_data.get('userwroktype', instance.userwroktype)
            instance.userbmiindex = validated_data.get('userbmiindex', instance.userbmiindex)
            instance.temp_sleepfeatureid = validated_data.get('temp_sleepfeatureid', instance.temp_sleepfeatureid)
            instance.temp_exercisefeatureid = validated_data.get('temp_exercisefeatureid', instance.temp_exercisefeatureid)
            instance.temp_eatingfeatureid = validated_data.get('temp_eatingfeatureid', instance.temp_eatingfeatureid)
            instance.temp_adminisareaid = validated_data.get('temp_adminisareaid', instance.temp_adminisareaid)
            instance.save()
        return instance

class TbHealthsuggestionscomSerializer(serializers.ModelSerializer):
    """
    健康建议表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbHealthsuggestions
        fields = (
            'healthsuggestid', 'healthsuggestcontent', 'healthsuggesttitle', 'healthsuggestremarks', 'temp_healthsuggtypeid',
            'healthsuggestflag', 'healthsuggestcode', 'temp_picturelocationid',
        )
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:

                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    hs = TbHealthsuggestions.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    hs = TbHealthsuggestions.objects.create(**validated_data)

            else:
                hs = TbHealthsuggestions.objects.create(**validated_data)
        return hs
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.healthsuggestcontent = validated_data.get('healthsuggestcontent', instance.healthsuggestcontent)
            instance.healthsuggesttitle = validated_data.get('healthsuggesttitle', instance.healthsuggesttitle)
            instance.healthsuggestremarks = validated_data.get('healthsuggestremarks', instance.healthsuggestremarks)
            instance.temp_healthsuggtypeid = validated_data.get('temp_healthsuggtypeid', instance.temp_healthsuggtypeid)
            instance.healthsuggestflag = validated_data.get('healthsuggestflag', instance.healthsuggestflag)
            instance.healthsuggestcode = validated_data.get('healthsuggestcode', instance.healthsuggestcode)
            instance.save()
        return instance

class TbHospitalinfoComSerializer(serializers.ModelSerializer):
    """
    医院信息表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbHospitalinfo
        fields = (
            'hospitalid', 'hospitalname', 'hospitalexplain', 'temp_locationinfoid', 'hospitalrank',
            'temp_adminisareaid', 'temp_picturelocationid',
        )
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    hp = TbHospitalinfo.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    hp = TbHospitalinfo.objects.create(**validated_data)

            else:
                hp = TbHospitalinfo.objects.create(**validated_data)
        return hp
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.hospitalname = validated_data.get('hospitalname', instance.hospitalname)
            instance.hospitalexplain = validated_data.get('hospitalexplain', instance.hospitalexplain)
            instance.temp_locationinfoid = validated_data.get('temp_locationinfoid', instance.temp_locationinfoid)
            instance.hospitalrank = validated_data.get('hospitalrank', instance.hospitalrank)
            instance.temp_adminisareaid = validated_data.get('temp_adminisareaid', instance.temp_adminisareaid)
            instance.save()
        return instance
class TbIntelligentdeviceinfocombineSerializer(serializers.ModelSerializer):
    """
    智能设备基本信息表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbIntelligentdeviceinfo
        fields = (
            'intelligentdeviceid', 'intelligentdevicetype', 'intelligentdevicename', 'intelligentdeviceweight', 'intelligentdevicecolor',
            'intelligentdevicefunction', 'intelligentdevicecode', 'temp_picturelocationid',
        )
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    Id = TbIntelligentdeviceinfo.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    Id = TbIntelligentdeviceinfo.objects.create(**validated_data)

            else:
                Id = TbIntelligentdeviceinfo.objects.create(**validated_data)
        return Id
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.intelligentdevicename = validated_data.get('intelligentdevicename', instance.intelligentdevicename)
            instance.intelligentdevicetype = validated_data.get('intelligentdevicetype', instance.intelligentdevicetype)
            instance.intelligentdeviceweight = validated_data.get('intelligentdeviceweight', instance.intelligentdeviceweight)
            instance.intelligentdevicecolor = validated_data.get('intelligentdevicecolor', instance.intelligentdevicecolor)
            instance.intelligentdevicefunction = validated_data.get('intelligentdevicefunction', instance.intelligentdevicefunction)
            instance.intelligentdevicecode = validated_data.get('intelligentdevicecode', instance.intelligentdevicecode)
            instance.save()
        return instance
class TbMedicineinfoCombineSerializer(serializers.ModelSerializer):
    """
    中药信息表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbMedicineinfo
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    MI = TbMedicineinfo.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    MI = TbMedicineinfo.objects.create(**validated_data)
            else:
                MI = TbMedicineinfo.objects.create(**validated_data)
        return MI
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.medicinename = validated_data.get('medicinename', instance.medicinename)
            instance.medicinegeneraltype = validated_data.get('medicinegeneraltype', instance.medicinegeneraltype)
            instance.medicinesubtype = validated_data.get('medicinesubtype', instance.medicinesubtype)
            instance.medicinetoxicity = validated_data.get('medicinetoxicity', instance.medicinetoxicity)
            instance.medicineproperty = validated_data.get('medicineproperty', instance.medicineproperty)
            instance.medicinetaste = validated_data.get('medicinetaste', instance.medicinetaste)
            instance.indicationsfunction = validated_data.get('indicationsfunction', instance.indicationsfunction)
            instance.channeltropism = validated_data.get('channeltropism', instance.channeltropism)
            instance.clinicalapplication = validated_data.get('clinicalapplication', instance.clinicalapplication)
            instance.medicinegenera = validated_data.get('medicinegenera', instance.medicinegenera)
            instance.prescriptionname = validated_data.get('prescriptionname', instance.prescriptionname)
            instance.generaldosage = validated_data.get('generaldosage', instance.generaldosage)
            instance.generalusage = validated_data.get('generalusage', instance.generalusage)
            instance.withmedicine = validated_data.get('withmedicine', instance.withmedicine)
            instance.comment = validated_data.get('comment', instance.comment)
            instance.prescriptionsexample = validated_data.get('prescriptionsexample', instance.prescriptionsexample)
            instance.medicineremarks = validated_data.get('medicineremarks', instance.medicineremarks)
            instance.medicinecode = validated_data.get('medicinecode', instance.medicinecode)
            instance.save()
        return instance
class TbPhysiqueinfoCombineSerializer(serializers.ModelSerializer):
    """
    体质信息表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbPhysiqueinfo
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    Id = TbPhysiqueinfo.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    Id = TbPhysiqueinfo.objects.create(**validated_data)

            else:
                Id = TbPhysiqueinfo.objects.create(**validated_data)
        return Id
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.tablescoreheight = validated_data.get('tablescoreheight', instance.tablescoreheight)
            instance.tablescorelow = validated_data.get('tablescorelow', instance.tablescorelow)
            instance.switchscoreheight = validated_data.get('switchscoreheight', instance.switchscoreheight)
            instance.switchscorelow = validated_data.get('switchscorelow', instance.switchscorelow)
            instance.generacharacter = validated_data.get('generacharacter', instance.generacharacter)
            instance.shapefeature = validated_data.get('shapefeature', instance.shapefeature)
            instance.commonmanifest = validated_data.get('commonmanifest', instance.commonmanifest)
            instance.mentalcharacter = validated_data.get('mentalcharacter', instance.mentalcharacter)
            instance.incidencetendency = validated_data.get('incidencetendency', instance.incidencetendency)
            instance.adaptivecapacity = validated_data.get('adaptivecapacity', instance.adaptivecapacity)
            instance.physicaltypename = validated_data.get('physicaltypename', instance.physicaltypename)
            instance.physicaltypecode = validated_data.get('physicaltypecode', instance.physicaltypecode)
            instance.adjustmethod = validated_data.get('adjustmethod', instance.adjustmethod)
            instance.multiplepeople = validated_data.get('multiplepeople', instance.multiplepeople)
            instance.physicalinterpretation = validated_data.get('physicalinterpretation', instance.physicalinterpretation)
            instance.physicalreason = validated_data.get('physicalreason', instance.physicalreason)
            instance.physicaladjustmethod = validated_data.get('physicaladjustmethod', instance.physicaladjustmethod)
            instance.foodallowtaboo = validated_data.get('foodallowtaboo', instance.foodallowtaboo)
            instance.save()
        return instance
class TbTcmdcotorsinfoCombineSerializer(serializers.ModelSerializer):
    """
    中医专家信息表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbTcmdcotorsinfo
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    Id = TbTcmdcotorsinfo.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    Id = TbTcmdcotorsinfo.objects.create(**validated_data)

            else:
                Id = TbTcmdcotorsinfo.objects.create(**validated_data)
        return Id
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.doctorname = validated_data.get('doctorname', instance.doctorname)
            instance.doctorsex = validated_data.get('doctorsex', instance.doctorsex)
            instance.doctorage = validated_data.get('doctorage', instance.doctorage)
            instance.professionalrands = validated_data.get('professionalrands', instance.professionalrands)
            instance.doctorworktime = validated_data.get('doctorworktime', instance.doctorworktime)
            instance.doctorsynopsis = validated_data.get('doctorsynopsis', instance.doctorsynopsis)
            instance.researcharea = validated_data.get('researcharea', instance.researcharea)
            instance.researchfindings = validated_data.get('researchfindings', instance.researchfindings)
            instance.temp_adminisareaid = validated_data.get('temp_adminisareaid', instance.temp_adminisareaid)
            instance.temp_doctorexpertiseid = validated_data.get('temp_doctorexpertiseid', instance.temp_doctorexpertiseid)
            instance.doctorcode = validated_data.get('doctorcode', instance.doctorcode)
            instance.save()
        return instance
class TbTcmhealthknowledgeCombineSerializer(serializers.ModelSerializer):
    """
    记录中医养生知识发布细节
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    #temp_healthknowltypeid = TbHealthknowledgetypeSerializer()
    exersuggtime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TbTcmhealthknowledge
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    Id = TbTcmhealthknowledge.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    Id = TbTcmhealthknowledge.objects.create(**validated_data)

            else:
                Id = TbTcmhealthknowledge.objects.create(**validated_data)
        return Id
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.healthknowledgetitle = validated_data.get('healthknowledgetitle', instance.healthknowledgetitle)
            instance.healthknowledgecontent = validated_data.get('healthknowledgecontent', instance.healthknowledgecontent)
            instance.exersuggtime = validated_data.get('exersuggtime', instance.exersuggtime)
            instance.temp_managerid = validated_data.get('temp_managerid', instance.temp_managerid)
            instance.healthknowledgeremarks = validated_data.get('healthknowledgeremarks', instance.healthknowledgeremarks)
            instance.temp_healthknowltypeid = validated_data.get('temp_healthknowltypeid', instance.temp_healthknowltypeid)
            instance.healthknowledgecode = validated_data.get('healthknowledgecode', instance.healthknowledgecode)
            instance.healthknowledgeflag = validated_data.get('healthknowledgeflag', instance.healthknowledgeflag)
            instance.save()
        return instance
class TbCommonfoodinfoComSerializer(serializers.ModelSerializer):
    """
    常见食物信息表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True)
    class Meta:
        model = TbCommonfoodinfo
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    Id = TbCommonfoodinfo.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    Id = TbCommonfoodinfo.objects.create(**validated_data)

            else:
                Id = TbCommonfoodinfo.objects.create(**validated_data)
        return Id
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.commonfoodname = validated_data.get('commonfoodname', instance.commonfoodname)
            instance.temp_commonfoodtypeid = validated_data.get('temp_commonfoodtypeid', instance.temp_commonfoodtypeid)
            instance.commonfoodexplain = validated_data.get('commonfoodexplain', instance.commonfoodexplain)
            instance.temp_foodnutritionid = validated_data.get('temp_foodnutritionid', instance.temp_foodnutritionid)
            instance.save()
        return instance
class TbExerciseinfoCombineSerializer(serializers.ModelSerializer):
    """
    运动实体信息表
    """
    temp_picturelocationid = TbPicturelistSerializer(allow_null=True, required=False)
    class Meta:
        model = TbExerciseinfo
    def create(self, validated_data):
        with transaction.atomic():
            picture_data = validated_data.pop('temp_picturelocationid')
            if picture_data:
                if picture_data['originalpicturepath']:
                    pic = TbPicturelist.objects.create(**picture_data)
                    Id = TbExerciseinfo.objects.create(temp_picturelocationid=pic, **validated_data)
                else:
                    Id = TbExerciseinfo.objects.create(**validated_data)

            else:
                Id = TbExerciseinfo.objects.create(**validated_data)
        return Id
    def update(self, instance, validated_data):
        temp_picture_data = validated_data.pop('temp_picturelocationid')
        with transaction.atomic():
            if temp_picture_data:
                try:
                    temp_picturelocationid = instance.temp_picturelocationid
                    temp_picturelocationid.originalpicturepath = temp_picture_data.get('originalpicturepath', temp_picturelocationid.originalpicturepath)
                    temp_picturelocationid.smallpicturepath = temp_picture_data.get('smallpicturepath', temp_picturelocationid.smallpicturepath)
                    temp_picturelocationid.pictureclass = temp_picture_data.get('pictureclass', temp_picturelocationid.pictureclass)
                    temp_picturelocationid.picturename = temp_picture_data.get('picturename', temp_picturelocationid.picturename)
                    temp_picturelocationid.picturetitle = temp_picture_data.get('picturetitle', temp_picturelocationid.picturetitle)
                    temp_picturelocationid.pictureusecode = temp_picture_data.get('pictureusecode', temp_picturelocationid.pictureusecode)
                    temp_picturelocationid.pictureremarks = temp_picture_data.get('pictureremarks', temp_picturelocationid.pictureremarks)
                    temp_picturelocationid.save()
                except:
                    pic = TbPicturelist.objects.create(**temp_picture_data)
                    instance.temp_picturelocationid = pic
            instance.exercisename = validated_data.get('exercisename', instance.exercisename)
            instance.exercisetypename = validated_data.get('exercisetypename', instance.exercisetypename)
            instance.energywaste = validated_data.get('energywaste', instance.energywaste)
            instance.exercisetip = validated_data.get('exercisetip', instance.exercisetip)
            instance.exerciseaffect = validated_data.get('exerciseaffect', instance.exerciseaffect)
            instance.temp_exercisetypeid = validated_data.get('temp_exercisetypeid', instance.temp_exercisetypeid)
            instance.save()
        return instance
