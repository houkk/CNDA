
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import djoser
from CNDADATA import restful, views, LianbiaoView, specialdata
from rest_framework import routers
from CNDADATA import djosercustom



router = routers.DefaultRouter()
router.register(r'tbadminisarea', restful.TbAdminisareaViewSet, base_name='tbadminisarea')
router.register(r'tbaverageamountstd', restful.TbAverageamountstdViewSet)
router.register(r'tbcommondiseaseinfo', restful.TbCommondiseaseinfoViewSet)
router.register(r'tbcommondiseasetype', restful.TbCommondiseasetypeViewSet)
router.register(r'tbcommonfoodinfo', restful.TbCommonfoodinfoViewSet)
router.register(r'tbcommfoodtype', restful.TbCommonfoodtypeViewSet)
router.register(r'tbcommonnutrientintake', restful.TbCommonnutrientintakeViewSet)
router.register(r'tbconstituteidentifyresult', restful.TbConstituteidentifyresultViewSet)
router.register(r'tbctreatmentrecords', restful.TbCtreatmentrecordsViewSet)
router.register(r'tbdataacquiretype', restful.TbDataacquiretypeViewSet)
router.register(r'tbdataacquisition', restful.TbDataacquisitionViewSet)
router.register(r'tbdeviceacquiredatarecords', restful.TbDeviceacquiredatarecordsViewSet)
router.register(r'tbdeviceparacode', restful.TbDeviceparacodeViewSet)
router.register(r'tbdeviceparamapp', restful.TbDeviceparamappViewSet)
router.register(r'tbdiagnosistrendsrecords', restful.TbDiagnosistrendsrecordsViewSet)
router.register(r'tbdietaryrecords', restful.TbDietaryrecordsViewSet)
router.register(r'tbdoctorexpertiseinfo', restful.TbDoctorexpertiseinfoViewSet)
router.register(r'tbdoctorexpertisetype', restful.TbDoctorexpertisetypeViewSet)
router.register(r'tbeatinganalysis', restful.TbEatinganalysisViewSet)
router.register(r'tbeatingpreferrecords', restful.TbEatingpreferrecordsViewSet)
router.register(r'tbeatingsetmealinfo', restful.TbEatingsetmealinfoViewSet)
router.register(r'tbexercisetype', restful.TbExercisetypeViewSet)
router.register(r'tbexerciseinfo', restful.TbExerciseinfoViewSet)
router.register(r'tbexercisepreferrecords', restful.TbExercisepreferrecordsViewSet)
router.register(r'tbexpendedhealthproperties', restful.TbExpendedhealthpropertiesViewset)
router.register(r'tbexpertcollect', restful.TbExpertcollectViewset)
router.register(r'tbfoodfeature', restful.TbFoodfeatureViewSet)
router.register(r'tbfoodmedicinaleffecttype', restful.TbFoodmedicinaleffecttypeViewset)
router.register(r'tbfoodmedicinalprop', restful.TbFoodmedicinalpropViewset)
router.register(r'tbfoodmedicinalpropmapp', restful.TbFoodmedicinalpropmappViewset)
router.register(r'tbfoodnutritionelement', restful.TbFoodnutritionelementViewset)
router.register(r'tbfoodnutritioncontent', restful.TbFoodnutritioncontentViewSet)
router.register(r'tbfoodwidecategories', restful.TbFoodwidecategoriesViewset)
router.register(r'tbhealthindicatorinfo', restful.TbHealthindicatorinfoViewSet)
router.register(r'tbhealthknowledgecollection', restful.TbHealthknowledgecollectionViewset)
router.register(r'tbhealthknowledgetype', restful.TbHealthknowledgetypeViewSet)
router.register(r'tbhealthrecommendscollection', restful.TbHealthrecommendscollectionViewset)
router.register(r'tbhealthsuggestions', restful.TbHealthsuggestionsViewSet)
router.register(r'tbhealthsuggtype', restful.TbHealthsuggtypeViewSet)
router.register(r'tbhealthtrendrecords', restful.TbHealthtrendrecordsViewSet)
router.register(r'tbhospitaldoctorrel', restful.TbHospitaldoctorrelViewSet)
router.register(r'tbhospitalinfo', restful.TbHospitalinfoViewSet)
router.register(r'tbhospitalofficesinfo', restful.TbHospitalofficesinfoViewSet)
router.register(r'tbidentificationissuess', restful.TbIdentificationissuessViewSet)
router.register(r'tbidentifychoices', restful.TbIdentifychoicesViewSet)
router.register(r'tbidentifydiseaserel', restful.TbIdentifydiseaserelViewSet)
router.register(r'tbintelligentdeviceinfo', restful.TbIntelligentdeviceinfoViewSet)
router.register(r'tblocationinfo', restful.TbLocationinfoViewSet)
router.register(r'tbmanager', restful.TbManagerViewSet)
router.register(r'tbmeasurementunit', restful.TbMeasurementunitViewSet)
router.register(r'tbmedicalhistoryrecords', restful.TbMedicalhistoryrecordsViewSet)
router.register(r'tbmedicineinfo', restful.TbMedicineinfoViewSet)
router.register(r'tbmedicineuseinfo', restful.TbMedicineuseinfoViewSet)
router.register(r'tbmovementdetailrecords', restful.TbMovementdetailrecordsViewset)
router.register(r'tbmycollection', restful.TbMycollectionViewSet)
router.register(r'tbphoneappinfo', restful.TbPhoneappinfoViewSet)
router.register(r'tbphoneinfo', restful.TbPhoneinfoViewSet)
router.register(r'tbphonemonitorrecords', restful.TbPhonemonitorrecordsViewSet)
router.register(r'tbphonepreferuserecords', restful.TbPhonepreferuserecordsViewSet)
router.register(r'tbphysiqueinfo', restful.TbPhysiqueinfoViewSet)
router.register(r'tbpicturelist', restful.TbPicturelistViewSet)
router.register(r'tbrecommendedconditionsmapp', restful.TbRecommendedconditionsmappViewSet)
router.register(r'tbsetmealfoodmapp', restful.TbSetmealfoodmappViewSet)
router.register(r'tbsleepdetailprocessrecords', restful.TbSleepdetailprocessrecordsViewset)
router.register(r'tbsleepinforecords', restful.TbSleepinforecordsViewSet, base_name='sleepinforecords')
router.register(r'tbsleeppreferrecords', restful.TbSleeppreferrecordsViewSet)
router.register(r'tbsleepstatuscategory', restful.TbSleepstatuscategoryViewset)
router.register(r'tbsportinforecords', restful.TbSportinforecordsViewSet)
router.register(r'tbstatisticofclick', restful.TbStatisticofclickViewSet)
router.register(r'tbsupervisorylevel', restful.TbSupervisorylevelViewSet)
router.register(r'tbtcmdcotorsinfo', restful.TbTcmdcotorsinfoViewSet)
router.register(r'tbtcmdiagnosisobj', restful.TbTcmdiagnosisobjViewSet)
router.register(r'tbtcmdiagnosistype', restful.TbTcmdiagnosistypeViewSet)
router.register(r'tbtcmhealthknowledge', restful.TbTcmhealthknowledgeViewSet)
router.register(r'tbuser', restful.TbUserViewSet)
router.register(r'tbuseranswerrecords', restful.TbUseranswerrecordsViewSet)
router.register(r'tbuserexercisefeature', restful.TbUserexercisefeatureViewSet)
router.register(r'tbuserreviewstat', restful.TbUserreviewstatViewSet)
router.register(r'tbusersleepfeature', restful.TbUsersleepfeatureViewSet)
router.register(r'tbwesmedicineexamitem', restful.TbWesmedicineexamitemViewSet)
router.register(r'tbwtreatmentrecords', restful.TbWtreatmentrecordsViewSet)
router.register(r'tbvariousindicatorstandard', restful.TbVariousindicatorstandardViewSet)
router.register(r'tbvariousindicatorlimited', restful.TbVariousindicatorlimitedViewSet)
router.register(r'tbindicatorusermapp', restful.TbIndicatorusermappViewSet)
router.register(r'tbhealthsuggestlimited', restful.TbHealthsuggestlimitedViewset)
router.register(r'tbhealthknowledgelimited', restful.TbHealthknowledgelimitedViewSet)
router.register(r'tbmedicineprescription', restful.TbMedicineprescriptionViewSet)
router.register(r'tbmedicineprescriptionmapp', restful.TbMedicineprescriptionmappViewSet)
router.register(r'tbhealthwarningtype', restful.TbHealthwarningtypeViewSet)
router.register(r'tbhealthwarningmess', restful.TbHealthwarningmessViewSet)
router.register(r'tbuserhealthattrmapp', restful.TbUserhealthattrmappViewset)
router.register(r'tbuserhealthwarningmapp', restful.TbUserhealthwarningmappViewSet)
router.register(r'tbuserknowledgemapp', restful.TbUserknowledgemappViewSet)
router.register(r'tbhealthsuggestionsmapp', restful.TbHealthsuggestionsmappViewSet)


router.register(r'test', LianbiaoView.TbHospitaldoctorrelliaobiaoViewSet)
router.register(r'doctorview', LianbiaoView.DoctorviewViewset, base_name='doctorview')
router.register(r'userhealthknowledgeview', LianbiaoView.UserhealthknowledgeViewset)
router.register(r'tbsportinforecordsseven', LianbiaoView.TbSportinforecordsSeven, base_name='tbsportinforecordsseven')
router.register(r'tbhealthtrendrecordscombine', LianbiaoView.TbHealthtrendrecordsLianbiaoViewSet)
router.register(r'tbconstituteidentifyresultcombine', LianbiaoView.TbConstituteidentifyresultCombineViewSet)
router.register(r'tbhospitalinfocombine', LianbiaoView.TbHospitalinfoCombineViewSet)
router.register(r'personaltuijian', LianbiaoView.personaltuijian, base_name='personaltuijian')
router.register(r'tbsetmealfoodmappcombine', LianbiaoView.TbSetmealfoodmappcombineViewset)
router.register(r'tbsleepinforecordscombine', LianbiaoView.TbSleepinforecordscombineViewSet)
router.register(r'tbrecommendedconditionsmappcombineid', LianbiaoView.TbRecommendedconditionsmappCombineidViewSet, base_name='tbhealthsuggestlimitedcombine')
router.register(r'tbrecommendedconditionsmappcombine', LianbiaoView.TbRecommendedconditionsmappCombineViewSet, base_name='tbhealthsuggestlimitedcombine')
urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^front/', include('Front.urls')),
    url(r'^login/', include('login.urls')),
    url(r'userhealthknowledgeview/(?P<healthknowltypename>.+)/$', LianbiaoView.userhealthknowledge.as_view()),
    url(r'tbtcmhealthknowledge/(?P<down>.+)/(?P<up>.+)/$', LianbiaoView.TbTcmhealthknowledgedate.as_view()),
    #url(r'sportinforecords/(?P<userid>.+)/$', LianbiaoView.TbSportinforecordsSeven.as_view()),
    url(r'^index/', views.index),
    url(r'^index1/', views.index1),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^update/', views.update),
    url(r'^tbsports/', specialdata.TbSportspecial),
    url(r'^tbsleep/', specialdata.TbSleepspecial),
    url(r'^sportall/', specialdata.sportall),
    url(r'^sportallmon/', specialdata.sportallmon),
    url(r'^sleepallmon/', specialdata.sleepallmon),
    url(r'^sportsingle/', specialdata.sportsingle),
    url(r'^sleepall/', specialdata.sleepall),
    url(r'^sleepsingle/', specialdata.sleepsingle),
    url(r'^eatingelement/', specialdata.eatingelement),
    url(r'^eatingallmon/', specialdata.eatingallmon),
    url(r'^eatingtype/', specialdata.eatingtype),
    url(r'^sleepenv/', specialdata.sleepenv),
    url(r'^page/', specialdata.pagetest),
    url(r'^index/$', views.index),
    url(r'^sport/$', specialdata.sport),
    url(r'^sleep/$', specialdata.sleep),
    url(r'^eating/$', specialdata.eating),
    url(r'^me/$', djosercustom.customuserview.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update', 'post': 'create'})),
    url(r'^changepassword/$', djosercustom.changepassword.as_view()),
    url(r'^passwordreset/$', djosercustom.Passwordresert.as_view()),
    url(r'^ceshi/(?P<datekey>.+)/$', specialdata.ceshi),
    url(r'^validate/$', djosercustom.validate),
    url(r'^logintest/$', djosercustom.customlogin.as_view()),
    url(r'^tokentest/$', specialdata.tokentest),
    url(r'^sleeparea/$', specialdata.sleeparea),
    url(r'^sleepadmin/$', specialdata.sleepadmin),
    url(r'^sportadmin/$', specialdata.sportadmin),
    url(r'^eatingelementadmin/$', specialdata.eatingelementadmin),
    url(r'^eatingtypeadmin/$', specialdata.eatingtypeadmin),
    #url(r'^timesplit/$', specialdata.timesplit),
)


