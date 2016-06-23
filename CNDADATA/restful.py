# -*- coding: utf-8 -*-
from django.db.models import Q, Avg
from rest_framework.decorators import list_route
from serializers import *
from LianBiaoSerializer import *
from models import *
from filter import *
from rest_framework import viewsets, permissions, pagination
from rest_framework_bulk import BulkCreateModelMixin, BulkUpdateModelMixin


class TbAdminisareaViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    行政区划代码表
    """
    queryset = TbAdminisarea.objects.all()
    serializer_class = TbAdminisareaSerializer
    filter_class = TbAdminisareaFilter


class TbAverageamountstdViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    平均量计算标准
    """
    queryset = TbAverageamountstd.objects.all()
    serializer_class = TbAverageamountstdSerializer

class TbCommondiseaseinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    常见疾病信息表
    """
    queryset = TbCommondiseaseinfo.objects.all()
    serializer_class = TbCommondiseaseinfoSerializer
    filter_class = TbCommondiseaseinfoFilter

class TbCommondiseasetypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    常见疾病类别表
    """
    queryset = TbCommondiseasetype.objects.all()
    serializer_class = TbCommondiseasetypeSerializer
    filter_class = TbCommondiseasetypeFilter

class TbCommonfoodinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    常见食物信息表
    """
    paginate_by = 4
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    queryset = TbCommonfoodinfo.objects.all()
    #serializer_class = TbCommonfoodinfoSerializer
    filter_class = TbCommonfoodinfoFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbCommonfoodinfoComSerializer
        if self.action == 'update':
            return TbCommonfoodinfoComSerializer
        if self.action == 'partial_update':
            return TbCommonfoodinfoComSerializer
        return TbCommonfoodinfoSerializer

class TbFoodwidecategoriesViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    食物大类表
    """
    queryset = TbFoodwidecategories.objects.all()
    serializer_class = TbFoodwidecategoriesSerializer
    filter_class = TbFoodwidecategoriesFilter

class TbCommonfoodtypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    常见食物类别表
    """
    queryset = TbCommonfoodtype.objects.all()
    serializer_class = TbCommonfoodtypeSerializer
    filter_class = TbCommonfoodtypeFilter

class TbCommonnutrientintakeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    营养素每日摄入量
    """
    queryset = TbCommonnutrientintake.objects.all()
    serializer_class = TbCommonnutrientintakeSerializer
    filter_class = TbCommonnutrientintakeFilter

class TbConstituteidentifyresultViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    体质辨识结果记录表
    """
    queryset = TbConstituteidentifyresult.objects.all()
    serializer_class = TbConstituteidentifyresultSerializer
    filter_class = TbConstituteidentifyresultFilter
    def get_queryset(self):
        if self.request._request.GET:
            global inputbool
            try:
                inputbool = self.request._request.GET['nine']
                inputbool = True
            except:
                inputbool = False
            print inputbool
            if inputbool:
                userid = self.request._request.GET['userid']
                result = TbConstituteidentifyresult.objects.filter(temp_userid=userid).order_by('-identifyresultid')[:9]
                return result
            else:
                return TbConstituteidentifyresult.objects.all()
        return TbConstituteidentifyresult.objects.all()
    # def get_serializer_class(self):
    #     if self.action == "create":
    #         return TbConstituteidentifyresultSerializer
    #     if self.action == "update":
    #         return TbConstituteidentifyresultSerializer
    #     return TbConstituteidentifyresultCombineSerializer

class TbCtreatmentrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录用户中医诊疗信息
    """
    queryset = TbCtreatmentrecords.objects.all()
    serializer_class = TbCtreatmentrecordsSerializer
    filter_class = TbCtreatmentrecordsFilter

class TbDataacquiretypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    采集数据分类表
    """
    queryset = TbDataacquiretype.objects.all()
    serializer_class = TbDataacquiretypeSerializer
    filter_class = TbDataacquiretypeFilter

class TbDataacquisitionViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    设备数据采集代码表
    """
    queryset = TbDataacquisition.objects.all()
    serializer_class = TbDataacquisitionSerializer
    filter_class = TbDataacquisitionFilter

class TbDeviceacquiredatarecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    智能设备采集数据记录表
    """
    queryset = TbDeviceacquiredatarecords.objects.all()
    serializer_class = TbDeviceacquiredatarecordsSerializer
    filter_class = TbDeviceacquiredatarecordsFilter

class TbDeviceparacodeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    设备参数代码表
    """
    queryset = TbDeviceparacode.objects.all()
    serializer_class = TbDeviceparacodeSerializer
    filter_class = TbDeviceparacodeFilter
class TbDeviceparamappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    针对不同设备有不同参数
    """
    queryset = TbDeviceparamapp.objects.all()
    serializer_class = TbDeviceparamappSerializer
    filter_class = TbDeviceparamappFilter

class TbDiagnosistrendsrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    诊断动态记录表
    """
    queryset = TbDiagnosistrendsrecords.objects.all()
    serializer_class = TbDiagnosistrendsrecordsSerializer
    filter_class = TbDiagnosistrendsrecordsFilter

class TbDietaryrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    饮食信息记录表
    """
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    queryset = TbDietaryrecords.objects.all()
    serializer_class = TbDietaryrecordsSerializer
    filter_class = TbDietaryrecordsFilter

class TbDoctorexpertiseinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    医生专长信息表
    """
    queryset = TbDoctorexpertiseinfo.objects.all()
    serializer_class = TbDoctorexpertiseinfoSerializer
    filter_class = TbDoctorexpertiseinfoFilter

class TbDoctorexpertisetypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    医生专长分类代码表
    """
    queryset = TbDoctorexpertisetype.objects.all()
    serializer_class = TbDoctorexpertisetypeSerializer
    filter_class = TbDoctorexpertisetypeFilter

class TbEatinganalysisViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    饮食状况分析表
    """
    queryset = TbEatinganalysis.objects.all()
    serializer_class = TbEatinganalysisSerializer
    filter_class = TbEatinganalysisFilter

class TbEatingpreferrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    饮食偏好记录表
    """
    queryset = TbEatingpreferrecords.objects.all()
    serializer_class = TbEatingpreferrecordsSerializer
    filter_class = TbEatingpreferrecordsFilter

class TbEatingsetmealinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    饮食套餐信息表
    """
    queryset = TbEatingsetmealinfo.objects.all()
    serializer_class = TbEatingsetmealinfoSerializer
    filter_class = TbEatingsetmealinfoFilter


class TbExercisetypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    运动类型名
    """
    queryset = TbExercisetype.objects.all()
    serializer_class = TbExercisetypeSerializer
    filter_class = TbExercisetypeFilter


class TbExerciseinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    运动实体信息表
    """
    queryset = TbExerciseinfo.objects.all()
    #serializer_class = TbExerciseinfoSerializer
    filter_class = TbExerciseinfoFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbExerciseinfoCombineSerializer
        if self.action == 'update':
            return TbExerciseinfoCombineSerializer
        if self.action == 'partial_update':
            return TbExerciseinfoCombineSerializer
        return TbExerciseinfoSerializer


class TbExercisepreferrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    运动偏好记录表
    """
    queryset = TbExercisepreferrecords.objects.all()
    serializer_class = TbExercisepreferrecordsSerializer
    filter_class = TbExercisepreferrecordsFilter

class TbExpendedhealthpropertiesViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    扩张健康属性表
    """
    queryset = TbExpendedhealthproperties.objects.all()
    serializer_class = TbExpendedhealthpropertiesSerializer
    filter_class = TbExpendedhealthpropertiesFilter


class TbFoodfeatureViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    饮食特征信息表
    """
    queryset = TbFoodfeature.objects.all()
    serializer_class = TbFoodfeatureSerializer
    filter_class = TbFoodfeatureFilter

class TbFoodnutritionelementViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    常见食物营养成分元素表
    """
    queryset = TbFoodnutritionelement.objects.all()
    serializer_class = TbFoodnutritionelementSerializer
    filter_class = TbFoodnutritionelementFilter

class TbFoodnutritioncontentViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    食物营养含量信息表
    """
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    queryset = TbFoodnutritioncontent.objects.all()
    serializer_class = TbFoodnutritioncontentSerializer
    filter_class = TbFoodnutritioncontentFilter

class TbHealthindicatorinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康指标信息表
    """
    queryset = TbHealthindicatorinfo.objects.all()
    serializer_class = TbHealthindicatorinfoSerializer
    filter_class = TbHealthindicatorinfoFilter

class TbHealthknowledgetypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    养生知识类别表
    """
    queryset = TbHealthknowledgetype.objects.all()
    serializer_class = TbHealthknowledgetypeSerializer
    filter_class = TbHealthknowledgetypeFilter


class TbHealthknowledgelimitedViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    养生知识限定条件表
    """
    queryset = TbHealthknowledgelimited.objects.all()
    serializer_class = TbHealthknowledgelimitedSerializer
    filter_class = TbHealthknowledgelimitedFilter


class TbHealthsuggestionsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康建议表
    """
    queryset = TbHealthsuggestions.objects.all()
    #serializer_class = TbHealthsuggestionsSerializer
    filter_class = TbHealthsuggestionsFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbHealthsuggestionscomSerializer
        if self.action == 'update':
            return TbHealthsuggestionscomSerializer
        if self.action == 'partial_update':
            return TbHealthsuggestionscomSerializer
        return TbHealthsuggestionsSerializer

class TbHealthsuggestionsmappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户健康建议映射表
    """

    queryset = TbHealthsuggestionsmapp.objects.all()
    #serializer_class = TbHealthsuggestionsmappSerializer
    filter_class = TbHealthsuggestionsmappFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbHealthsuggestionsmappSerializer
        if self.action == 'update':
            return TbHealthsuggestionsmappSerializer
        return TbHealthsuggestionsmappcombineSerializer


class TbHealthsuggestlimitedViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康建议限定条件表
    """
    queryset = TbHealthsuggestlimited.objects.all()
    serializer_class = TbHealthsuggestlimitedSerializer
    filter_class = TbHealthsuggestlimitedFilter


class TbHealthsuggtypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康建议类别表
    """
    queryset = TbHealthsuggtype.objects.all()
    serializer_class = TbHealthsuggtypeSerializer
    filter_class = TbHealthsuggtypeFilter

class TbHealthtrendrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录用户健康趋势
    """
    queryset = TbHealthtrendrecords.objects.all()
    serializer_class = TbHealthtrendrecordsSerializer
    filter_class = TbHealthtrendrecordsFilter
    # def get_serializer_class(self):
    #     if self.action == "create":
    #         return TbHealthtrendrecordsSerializer
    #     if self.action == "update":
    #         return TbHealthtrendrecordsSerializer
    #     return TbHealthtrendrecordsLianbiaoSerializer


class TbHealthwarningtypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康预警类别表
    """
    queryset = TbHealthwarningtype.objects.all()
    serializer_class = TbHealthwarningtypeSerializer
    filter_class = TbHealthwarningtypeFilter





class TbHealthwarningmessViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康预警信息表
    """

    queryset = TbHealthwarningmess.objects.all()
    serializer_class = TbHealthwarningmessSerializer
    filter_class = TbHealthwarningmessFilter


class TbUserhealthattrmappViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户健康属性映射表
    """
    queryset = TbUserhealthattrmapp.objects.all()
    serializer_class = TbUserhealthattrmappSerializer
    filter_class = TbUserhealthattrmappFilter


class TbUserhealthwarningmappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户预警映射表
    """
    queryset = TbUserhealthwarningmapp.objects.all()
    #serializer_class = TbUserhealthwarningmappSerializer
    filter_class = TbUserhealthwarningmappFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbUserhealthwarningmappSerializer
        if self.action == 'update':
            return TbUserhealthwarningmappSerializer
        return TbUserhealthwarningmappcombineSerializer






class TbHospitaldoctorrelViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    医院医生关系表
    """
    queryset = TbHospitaldoctorrel.objects.all()
    serializer_class = TbHospitaldoctorrelSerializer
    filter_class = TbHospitaldoctorrelFilter

class TbHospitalinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    医院信息表
    """
    queryset = TbHospitalinfo.objects.all()
    #serializer_class = TbHospitalinfoSerializer
    filter_class = TbHospitalinfoFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbHospitalinfoComSerializer
        if self.action == 'update':
            return TbHospitalinfoComSerializer
        if self.action == 'partial_update':
            return TbHospitalinfoComSerializer
        return TbHospitalinfoSerializer

class TbHospitalofficesinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    医院科室信息表
    """
    queryset = TbHospitalofficesinfo.objects.all()
    serializer_class = TbHospitalofficesinfoSerializer
    filter_class = TbHospitalofficesinfoFilter

class TbIdentificationissuessViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    体质辨识问卷项目表
    """
    queryset = TbIdentificationissuess.objects.all()
    serializer_class = TbIdentificationissuessSerializer
    filter_class = TbIdentificationissuessFilter

class TbIdentifychoicesViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    体质辨识选项表
    """
    queryset = TbIdentifychoices.objects.all()
    serializer_class = TbIdentifychoicesSerializer
    filter_class = TbIdentifychoicesFilter

class TbIdentifydiseaserelViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录体质和疾病的关系
    """
    queryset = TbIdentifydiseaserel.objects.all()
    #serializer_class = TbIdentifydiseaserelSerializer
    filter_class = TbIdentifydiseaserelFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbIdentifydiseaserelSerializer
        if self.action == 'update':
            return TbIdentifydiseaserelSerializer
        return TbIdentifydiseaserelcombineSerializer

class TbIntelligentdeviceinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    智能设备基本信息表
    """
    queryset = TbIntelligentdeviceinfo.objects.all()
    #serializer_class = TbIntelligentdeviceinfoSerializer
    filter_class = TbIntelligentdeviceinfoFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbIntelligentdeviceinfocombineSerializer
        if self.action == 'update':
            return TbIntelligentdeviceinfocombineSerializer
        if self.action == 'partial_update':
            return TbIntelligentdeviceinfocombineSerializer
        return TbIntelligentdeviceinfoSerializer

class TbLocationinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    地理位置相关信息
    """
    queryset = TbLocationinfo.objects.all()
    serializer_class = TbLocationinfoSerializer
    filter_class = TbLocationinfoFilter

class TbManagerViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    管理员实体，记录管理员基本信息
    """
    queryset = TbManager.objects.all()
    serializer_class = TbManagerSerializer
    filter_class = TbManagerFilter

class TbMeasurementunitViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    项目中用到的计量单位在此记录
    """
    queryset = TbMeasurementunit.objects.all()
    serializer_class = TbMeasurementunitSerializer
    filter_class = TbMeasurementunitFilter

class TbMedicalhistoryrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录用户病史
    """
    queryset = TbMedicalhistoryrecords.objects.all()
    serializer_class = TbMedicalhistoryrecordsSerializer
    filter_class = TbMedicalhistoryrecordsFilter

class TbMedicineinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    中药信息表
    """
    queryset = TbMedicineinfo.objects.all()
    #serializer_class = TbMedicineinfoSerializer
    filter_class = TbMedicineinfoFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbMedicineinfoCombineSerializer
        if self.action == 'update':
            return TbMedicineinfoCombineSerializer
        if self.action == 'partial_update':
            return TbMedicineinfoCombineSerializer
        return TbMedicineinfoSerializer

class TbMedicineprescriptionViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    中药方剂表
    """
    queryset = TbMedicineprescription.objects.all()
    serializer_class = TbMedicineprescriptionSerializer
    filter_class = TbMedicineprescriptionFilter


class TbMedicineprescriptionmappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    药品方剂映射表
    """
    queryset = TbMedicineprescriptionmapp.objects.all()
    serializer_class = TbMedicineprescriptionmappSerializer
    filter_class = TbMedicineprescriptionmappFilter


class TbMedicineuseinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录用户诊疗过程中的用药信息
    """
    queryset = TbMedicineuseinfo.objects.all()
    serializer_class = TbMedicineuseinfoSerializer
    filter_class = TbMedicineuseinfoFilter


class TbMovementdetailrecordsViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    运动详细过程记录表
    """
    queryset = TbMovementdetailrecords.objects.all()
    serializer_class = TbMovementdetailrecordsSerializer
    filter_class = TbMovementdetailrecordsFilter


class TbMycollectionViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    我的收藏
    """
    queryset = TbMycollection.objects.all()
    serializer_class = TbMycollectionSeria
    filter_class = TbMycollectionFilter




class TbPhoneappinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    手机应用实体部分信息
    """
    queryset = TbPhoneappinfo.objects.all()
    serializer_class = TbPhoneappinfoSerializer
    filter_class = TbPhoneappinfoFilter

class TbPhoneinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    手机监控特征信息表
    """
    queryset = TbPhoneinfo.objects.all()
    serializer_class = TbPhoneinfoSerializer
    filter_class = TbPhoneinfoFilter

class TbPhonemonitorrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    手机监控记录表
    """
    queryset = TbPhonemonitorrecords.objects.all()
    serializer_class = TbPhonemonitorrecordsSerializer
    filter_class = TbPhonemonitorrecordsFilter

class TbPhonepreferuserecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    手机使用偏好记录
    """
    queryset = TbPhonepreferuserecords.objects.all()
    serializer_class = TbPhonepreferuserecordsSerializer
    filter_class = TbPhonepreferuserecordsFilter

class TbPhysiqueinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    体质信息表
    """
    queryset = TbPhysiqueinfo.objects.all()
    #serializer_class = TbPhysiqueinfoSerializer
    filter_class = TbPhysiqueinfoFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbPhysiqueinfoCombineSerializer
        if self.action == 'update':
            return TbPhysiqueinfoCombineSerializer
        if self.action == 'partial_update':
            return TbPhysiqueinfoCombineSerializer
        return TbPhysiqueinfoSerializer

class TbPicturelistViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    图片列表
    """
    queryset = TbPicturelist.objects.all()
    serializer_class = TbPicturelistSerializer
    filter_class = TbPicturelistFilter

class TbRecommendedconditionsmappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    健康建议条件限定映射表
    """
    queryset = TbRecommendedconditionsmapp.objects.all()
    serializer_class = TbRecommendedconditionsmappSerializer
    filter_class = TbRecommendedconditionsmappFilter


class TbSetmealfoodmappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    套餐食物映射表
    """
    queryset = TbSetmealfoodmapp.objects.all()
    serializer_class = TbSetmealfoodmappSerializer
    filter_class = TbSetmealfoodmappFiler

class TbSleepdetailprocessrecordsViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    睡眠详细过程记录表
    """
    queryset = TbSleepdetailprocessrecords.objects.all()
    serializer_class = TbSleepdetailprocessrecordsSerializer
    filter_class = TbSleepdetailprocessrecordsFilter


class TbSleepinforecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录用户睡眠信息
    """
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    queryset = TbSleepinforecords.objects.all()
    serializer_class = TbSleepinforecordsSerializer
    filter_class = TbSleepinforecordsFilter


class TbSleeppreferrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录用户睡眠偏好，如：睡眠时间，可向用户推送相关信息
    """
    queryset = TbSleeppreferrecords.objects.all()
    serializer_class = TbSleeppreferrecordsSerializer
    filter_class = TbSleeppreferrecordsFilter

class TbSleepstatuscategoryViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    睡眠状态类别表
    """
    queryset = TbSleepstatuscategory.objects.all()
    serializer_class = TbSleepstatuscategorySerializer
    filter_class = TbSleepstatuscategoryFilter


class TbSportinforecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录用户运动数据
    """
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    queryset = TbSportinforecords.objects.all()
    serializer_class = TbSportinforecordsSerializer
    filter_class = TbSportinforecordsFilter
class TbStatisticofclickViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    点击量统计表
    """
    queryset = TbStatisticofclick.objects.all()
    serializer_class = TbStatisticofclickSerializer
    filter_class = TbStatisticofclickFilter

class TbSupervisorylevelViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    管理员管理权限、范围
    """
    queryset = TbSupervisorylevel.objects.all()
    serializer_class = TbSupervisorylevelSerializer
    filter_class = TbSupervisorylevelFilter

class TbTcmdcotorsinfoViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    中医专家信息表
    """
    queryset = TbTcmdcotorsinfo.objects.all()
    #serializer_class = TbTcmdcotorsinfoSerializer
    filter_class = TbTcmdcotorsinfoFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbTcmdcotorsinfoCombineSerializer
        if self.action == 'update':
            return TbTcmdcotorsinfoCombineSerializer
        if self.action == 'partial_update':
            return TbTcmdcotorsinfoCombineSerializer
        return TbTcmdcotorsinfoSerializer

class TbTcmdiagnosisobjViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    诊断对象表
    """
    queryset = TbTcmdiagnosisobj.objects.all()
    serializer_class = TbTcmdiagnosisobjSerializer
    filter_class = TbTcmdiagnosisobjFilter

class TbTcmdiagnosistypeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    中医诊断分类表
    """
    queryset = TbTcmdiagnosistype.objects.all()
    serializer_class = TbTcmdiagnosistypeSerializer
    filter_class = TbTcmdiagnosistypeFilter

class TbTcmhealthknowledgeViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    记录中医养生知识发布细节
    """
    paginate_by = 20
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    queryset = TbTcmhealthknowledge.objects.all()
    #serializer_class = TbTcmhealthknowledgeSerializer
    filter_class = TbTcmhealthknowledgeFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbTcmhealthknowledgeCombineSerializer
        if self.action == 'update':
            return TbTcmhealthknowledgeCombineSerializer
        if self.action == 'partial_update':
            return TbTcmhealthknowledgeCombineSerializer
        return TbTcmhealthknowledgeSerializer

class TbUserViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户实体，记录用户基本信息
    """
    queryset = TbUser.objects.all()
    #serializer_class = TbUserSerializer
    filter_class = TbUserFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbUserCombineSerializer
        if self.action == 'update':
            return TbUserCombineSerializer
        if self.action == 'partial_update':
            return TbUserCombineSerializer
        return TbUserSerializer


class TbUseranswerrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户答题记录表
    """
    queryset = TbUseranswerrecords.objects.all()
    serializer_class = TbUseranswerrecordsSerializer
    filter_class = TbUseranswerrecordsFilter

class TbUserexercisefeatureViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户运动的特征信息，如：身高等
    """
    queryset = TbUserexercisefeature.objects.all()
    serializer_class = TbUserexercisefeatureSerializer
    filter_class = TbUserexercisefeatureFilter


class TbUserknowledgemappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户养生知识映射表
    """
    queryset = TbUserknowledgemapp.objects.all()
    serializer_class = TbUserknowledgemappSerializer
    filter_class = TbUserknowledgemappFilter


class TbUserreviewstatViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户评论统计
    """
    queryset = TbUserreviewstat.objects.all()
    serializer_class = TbUserreviewstatSerializer
    filter_class = TbUserreviewstatFilter


class TbUsersleepfeatureViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    用户睡眠特征信息（包括睡眠环境：温度、湿度、噪声情况等）
    """
    queryset = TbUsersleepfeature.objects.all()
    serializer_class = TbUsersleepfeatureSerializer
    filter_class = TbUsersleepfeatureFilter



class TbVariousindicatorstandardViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    各类指标标准表
    """
    queryset = TbVariousindicatorstandard.objects.all()
    serializer_class = TbVariousindicatorstandardSerializer
    filter_class = TbVariousindicatorstandardFilter



class TbVariousindicatorlimitedViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    各类标准限定表
    """
    queryset = TbVariousindicatorlimited.objects.all()
    serializer_class = TbVariousindicatorlimitedSerializer
    filter_class = TbVariousindicatorlimitedFilter


class TbIndicatorusermappViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    指标用户映射表
    """
    queryset = TbIndicatorusermapp.objects.all()
    serializer_class = TbIndicatorusermappSerializer
    filter_class = TbIndicatorusermappFilter



class TbWesmedicineexamitemViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    西医体检项目表
    """
    queryset = TbWesmedicineexamitem.objects.all()
    serializer_class = TbWesmedicineexamitemSerializer
    filter_class = TbWesmedicineexamitemFilter

class TbWtreatmentrecordsViewSet(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    西医诊疗记录表
    """
    queryset = TbWtreatmentrecords.objects.all()
    serializer_class = TbWtreatmentrecordsSerializer
    filter_class = TbWtreatmentrecordsFilter


class TbExpertcollectViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    专家收藏表
    """
    queryset = TbExpertcollect.objects.all()
    serializer_class = TbExpertcollectSerilizer
    filter_class = TbExpertcollectFilter
class TbHealthrecommendscollectionViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    养生建议收藏表
    """
    queryset = TbHealthrecommendscollection.objects.all()
    serializer_class = TbHealthrecommendscollectionSerializer
    filter_class = TbHealthrecommendscollectionFilter

class TbHealthknowledgecollectionViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    养生知识收藏表
    """
    queryset = TbHealthknowledgecollection.objects.all()
    serializer_class = TbHealthknowledgecollectionSerializer
    filter_class = TbHealthknowledgecollectionFilter

class TbFoodmedicinaleffecttypeViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    食物药用功效类别
    """
    queryset = TbFoodmedicinaleffecttype.objects.all()
    serializer_class = TbFoodmedicinaleffecttypeSerializer
    filter_class = TbFoodmedicinaleffecttypeFilter

class TbFoodmedicinalpropViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    食物药用属性表
    """
    queryset = TbFoodmedicinalprop.objects.all()
    serializer_class = TbFoodmedicinalpropSerializer
    filter_class = TbFoodmedicinalpropFilter

class TbFoodmedicinalpropmappViewset(BulkCreateModelMixin, BulkUpdateModelMixin, viewsets.ModelViewSet):
    """
    食物药用属性映射表
    """
    queryset = TbFoodmedicinalpropmapp.objects.all()
    serializer_class = TbFoodmedicinalpropmappSerializer
    filter_class = TbFoodmedicinalpropmappFilter