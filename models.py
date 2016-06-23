# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class CndadataRegister(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    aboutyou = models.CharField(db_column='aboutYou', max_length=100)  # Field name made lowercase.
    mailinglist = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CNDADATA_register'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('TbUser', unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CorsheadersCorsmodel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cors = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'corsheaders_corsmodel'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey('TbUser')

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctorview(models.Model):
    doctorid = models.IntegerField(blank=True, null=True)
    doctorname = models.CharField(max_length=20, blank=True)
    doctorsex = models.CharField(max_length=5, blank=True)
    doctorage = models.IntegerField(blank=True, null=True)
    professionalrands = models.CharField(max_length=100, blank=True)
    doctorworktime = models.IntegerField(blank=True, null=True)
    doctorsynopsis = models.CharField(max_length=1024, blank=True)
    researcharea = models.CharField(max_length=1024, blank=True)
    researchfindings = models.CharField(max_length=1024, blank=True)
    adminisareaprovince = models.CharField(max_length=50, blank=True)
    adminisareacity = models.CharField(max_length=50, blank=True)
    adminisareacounty = models.CharField(max_length=50, blank=True)
    doctorexptypename = models.CharField(max_length=50, blank=True)
    doctorexpertisetitle = models.CharField(max_length=100, blank=True)
    hospitalname = models.CharField(max_length=100, blank=True)
    hospitalofficename = models.CharField(max_length=50, blank=True)
    workduty = models.CharField(max_length=200, blank=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctorview'


class RestFrameworkToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    user = models.ForeignKey('TbUser', unique=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rest_framework_token'


class TbAdminisarea(models.Model):
    adminisareaid = models.IntegerField(primary_key=True)
    adminisareacode = models.CharField(max_length=50, blank=True)
    adminisareaprovince = models.CharField(max_length=50, blank=True)
    adminisareacity = models.CharField(max_length=50, blank=True)
    adminisareacounty = models.CharField(max_length=50, blank=True)
    adminisarearemarks = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_adminisarea'


class TbAverageamountstd(models.Model):
    amountstdid = models.IntegerField(primary_key=True)
    amountnumofdays = models.BigIntegerField(blank=True, null=True)
    averageamountremarks = models.CharField(max_length=100, blank=True)
    amountbegintime = models.TimeField(blank=True, null=True)
    amountstoptime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_averageamountstd'


class TbCommondiseaseinfo(models.Model):
    commondiseaseid = models.IntegerField(primary_key=True)
    temp_commonditypeid_id = models.IntegerField(blank=True, null=True)
    commondiname = models.CharField(max_length=50, blank=True)
    diseaseexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_commondiseaseinfo'


class TbCommondiseasetype(models.Model):
    commonditypeid = models.IntegerField(primary_key=True)
    commonditypename = models.CharField(max_length=50, blank=True)
    commonditypecode = models.IntegerField(blank=True, null=True)
    diclassifyexplain = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_commondiseasetype'


class TbCommonfoodinfo(models.Model):
    commonfoodid = models.IntegerField(primary_key=True)
    commonfoodname = models.CharField(max_length=50, blank=True)
    temp_commonfoodtypeid_id = models.IntegerField(blank=True, null=True)
    commonfoodexplain = models.CharField(max_length=1024, blank=True)
    temp_foodnutritionid_id = models.IntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_commonfoodinfo'


class TbCommonfoodtype(models.Model):
    commonfoodtypeid = models.IntegerField(primary_key=True)
    commonfoodtypename = models.CharField(max_length=50, blank=True)
    commonfoodtypecode = models.IntegerField(blank=True, null=True)
    foodtypeexplain = models.CharField(max_length=1024, blank=True)
    temp_foodwidecategoryid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_commonfoodtype'


class TbCommonnutrientintake(models.Model):
    nutrientid = models.IntegerField(primary_key=True)
    nutrientname = models.CharField(max_length=30, blank=True)
    nutrientintakemax = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nutrientintakemin = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    maxagefor = models.IntegerField(blank=True, null=True)
    minagefor = models.IntegerField(blank=True, null=True)
    nutrientintakeremarks = models.CharField(max_length=200, blank=True)
    temp_unitattributeid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_commonnutrientintake'


class TbConstituteidentifyresult(models.Model):
    identifyresultid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_physiqueinfoid_id = models.IntegerField(blank=True, null=True)
    constituteidentifytime = models.DateTimeField(blank=True, null=True)
    constituteidentifyremarks = models.CharField(max_length=500, blank=True)
    constituteidentifyresult = models.CharField(max_length=30, blank=True)
    constituteldentifyflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_constituteidentifyresult'


class TbCtreatmentrecords(models.Model):
    tcmexaminationid = models.IntegerField(primary_key=True)
    integral_spirit = models.CharField(max_length=1024, blank=True)
    integral_look = models.CharField(max_length=1024, blank=True)
    integral_shape = models.CharField(max_length=1024, blank=True)
    part_head = models.CharField(max_length=1024, blank=True)
    part_organs = models.CharField(max_length=1024, blank=True)
    part_chest = models.CharField(max_length=1024, blank=True)
    part_tonguenature = models.CharField(max_length=1024, blank=True)
    part_fur = models.CharField(max_length=1024, blank=True)
    pulsecondition = models.CharField(max_length=1024, blank=True)
    inquiry_feel = models.CharField(max_length=1024, blank=True)
    inquiry_eating = models.CharField(max_length=1024, blank=True)
    inquiry_habit = models.CharField(max_length=1024, blank=True)
    healthcareguid = models.CharField(max_length=1024, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_doctorid_id = models.IntegerField(blank=True, null=True)
    examinationtime = models.DateTimeField(blank=True, null=True)
    examinationlocation = models.CharField(max_length=100, blank=True)
    examinationresult = models.CharField(max_length=1024, blank=True)
    examinationremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_ctreatmentrecords'


class TbDataacquiretype(models.Model):
    acqdatatypeid = models.IntegerField(primary_key=True)
    acqdatatypename = models.CharField(max_length=50, blank=True)
    acqdatatypeexplain = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_dataacquiretype'


class TbDataacquisition(models.Model):
    acquiredataid = models.IntegerField(primary_key=True)
    acquiredataname = models.CharField(max_length=20, blank=True)
    acquiredataexplain = models.CharField(max_length=200, blank=True)
    temp_acqdatatypeid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dataacquisition'


class TbDeviceacquiredatarecords(models.Model):
    deviceacqrecordid = models.IntegerField(primary_key=True)
    temp_intelligentdeviceid_id = models.IntegerField(blank=True, null=True)
    temp_acquiredataid_id = models.IntegerField(blank=True, null=True)
    deviceacqdatavalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    temp_unitattributeid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_deviceacquiredatarecords'


class TbDeviceparacode(models.Model):
    deviceparacodeid = models.IntegerField(primary_key=True)
    parametercode = models.IntegerField(blank=True, null=True)
    parametername = models.CharField(max_length=30, blank=True)
    parametermean = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_deviceparacode'


class TbDeviceparamapp(models.Model):
    deviceparamappid = models.IntegerField(primary_key=True)
    temp_intelligentdeviceid_id = models.IntegerField(blank=True, null=True)
    temp_deviceparacodeid_id = models.IntegerField(blank=True, null=True)
    deviceparavalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_deviceparamapp'


class TbDiagnosistrendsrecords(models.Model):
    diatrendid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_diagnosisobjid_id = models.IntegerField(blank=True, null=True)
    temp_doctorid_id = models.IntegerField(blank=True, null=True)
    diatrendres = models.CharField(max_length=100, blank=True)
    diatrendresexplain = models.CharField(max_length=200, blank=True)
    diatrendtime = models.DateField(blank=True, null=True)
    diatrendplace = models.CharField(max_length=100, blank=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_diagnosistrendsrecords'


class TbDietaryrecords(models.Model):
    eatingrecordid = models.IntegerField(primary_key=True)
    foodtypename = models.CharField(max_length=50, blank=True)
    foodname = models.CharField(max_length=50, blank=True)
    eatingamount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    unitname = models.CharField(max_length=20, blank=True)
    eatingtime = models.DateTimeField(blank=True, null=True)
    eatingrecordsuptime = models.DateTimeField(blank=True, null=True)
    eatinginforemarks = models.CharField(max_length=150, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    eatingstateback = models.CharField(max_length=200, blank=True)
    temp_foodnutritionid_id = models.IntegerField(blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    temp_intelligentdeviceid_id = models.IntegerField(blank=True, null=True)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    eatingupflag = models.BigIntegerField(blank=True, null=True)
    setmealcode = models.BigIntegerField(blank=True, null=True)
    eatingovertime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dietaryrecords'


class TbDoctorexpertiseinfo(models.Model):
    doctorexpertiseid = models.IntegerField(primary_key=True)
    doctorexpertisetitle = models.CharField(max_length=100, blank=True)
    doctorexpertiseexplain = models.CharField(max_length=1024, blank=True)
    temp_doctorexptypeid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_doctorexpertiseinfo'


class TbDoctorexpertisetype(models.Model):
    doctorexptypeid = models.IntegerField(primary_key=True)
    doctorexptypename = models.CharField(max_length=50, blank=True)
    doctorexptypecode = models.IntegerField(blank=True, null=True)
    doctorexptypeexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_doctorexpertisetype'


class TbEatinganalysis(models.Model):
    eatinganalysisid = models.IntegerField(primary_key=True)
    energyintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    energyunit = models.CharField(max_length=10, blank=True)
    moistureintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    moistureunit = models.CharField(max_length=10, blank=True)
    proteinintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    proteinunit = models.CharField(max_length=10, blank=True)
    fatintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fatunit = models.CharField(max_length=10, blank=True)
    fiberintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fiberunit = models.CharField(max_length=10, blank=True)
    carbohydrateintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    carbohydrateunit = models.CharField(max_length=10, blank=True)
    vitaminaintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminaunit = models.CharField(max_length=10, blank=True)
    vitaminb1intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb1unit = models.CharField(max_length=10, blank=True)
    vitaminb2intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb2unit = models.CharField(max_length=10, blank=True)
    vitaminb6intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb6unit = models.CharField(max_length=10, blank=True)
    vitaminb12intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb12unit = models.CharField(max_length=10, blank=True)
    vitamincintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamincunit = models.CharField(max_length=10, blank=True)
    vitamindintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamindunit = models.CharField(max_length=10, blank=True)
    vitamineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamineunit = models.CharField(max_length=10, blank=True)
    vitaminkintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminkunit = models.CharField(max_length=10, blank=True)
    nicotinicacidintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nicotinicacidunit = models.CharField(max_length=10, blank=True)
    folateintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    folateunit = models.CharField(max_length=10, blank=True)
    sodiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sodiumunit = models.CharField(max_length=10, blank=True)
    calciumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    calciumunit = models.CharField(max_length=10, blank=True)
    ironintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ironunit = models.CharField(max_length=10, blank=True)
    potassiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    potassiumunit = models.CharField(max_length=10, blank=True)
    zincintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    zincunit = models.CharField(max_length=10, blank=True)
    magnesiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    magnesiumunit = models.CharField(max_length=10, blank=True)
    copperintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    copperunit = models.CharField(max_length=10, blank=True)
    chomuimintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    chomuimunit = models.CharField(max_length=10, blank=True)
    mangaesiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mangaesiumunit = models.CharField(max_length=10, blank=True)
    molybdenumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    molybdenumunit = models.CharField(max_length=10, blank=True)
    iodineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    iodineunit = models.CharField(max_length=10, blank=True)
    phosphrusintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    phosphrusunit = models.CharField(max_length=10, blank=True)
    seleniumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    seleniumunit = models.CharField(max_length=10, blank=True)
    fluorineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fluorineunit = models.CharField(max_length=10, blank=True)
    cholesterolintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cholesterolunit = models.CharField(max_length=10, blank=True)
    saturatedintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    saturatedunit = models.CharField(max_length=10, blank=True)
    acidregurgitationintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    acidregurgitationunit = models.CharField(max_length=10, blank=True)
    biotinintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    biotinunit = models.CharField(max_length=10, blank=True)
    cholineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cholineunit = models.CharField(max_length=10, blank=True)
    temp_eatingrecordid_id = models.BigIntegerField(blank=True, null=True)
    caroteneintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    caroteneunit = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_eatinganalysis'


class TbEatingpreferrecords(models.Model):
    eatingpreferid = models.IntegerField(primary_key=True)
    foodtypename = models.CharField(max_length=50, blank=True)
    foodname = models.CharField(max_length=50, blank=True)
    preference = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    averageintake = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    temp_foodnutritionid_id = models.IntegerField(blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    eatingoftenstarttime = models.TimeField(blank=True, null=True)
    eatingoftenovertime = models.TimeField(blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    additemtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_eatingpreferrecords'


class TbEatingsetmealinfo(models.Model):
    setmealinfoid = models.IntegerField(primary_key=True)
    foodtypecontent = models.IntegerField(blank=True, null=True)
    setmealname = models.CharField(max_length=50, blank=True)
    setmealexplain = models.CharField(max_length=1024, blank=True)
    setmealremarks = models.CharField(max_length=100, blank=True)
    setmealcode = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_eatingsetmealinfo'


class TbExerciseinfo(models.Model):
    exerciseid = models.IntegerField(primary_key=True)
    exercisename = models.CharField(max_length=20, blank=True)
    exercisetypename = models.CharField(max_length=20, blank=True)
    energywaste = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    exercisetip = models.CharField(max_length=1024, blank=True)
    exerciseaffect = models.CharField(max_length=1024, blank=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)
    temp_exercisetypeid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_exerciseinfo'


class TbExercisepreferrecords(models.Model):
    exercisepreferenceid = models.IntegerField(primary_key=True)
    exercisetype = models.CharField(max_length=20, blank=True)
    exercisename = models.CharField(max_length=20, blank=True)
    exercisedescribe = models.CharField(max_length=200, blank=True)
    temp_exerciseid_id = models.IntegerField(blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    additemtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_exercisepreferrecords'


class TbExercisetype(models.Model):
    exercisetypeid = models.IntegerField(primary_key=True)
    exercisetypename = models.CharField(max_length=100, blank=True)
    exercisetypeexplain = models.CharField(max_length=1024, blank=True)
    exercisetypecode = models.IntegerField(blank=True, null=True)
    exercisetyperemarks = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_exercisetype'


class TbExpendedhealthproperties(models.Model):
    exphealthpropertyid = models.IntegerField(primary_key=True)
    healthpropertyname = models.CharField(max_length=20, blank=True)
    healthpropertyexplain = models.CharField(max_length=500, blank=True)
    healthpropertycode = models.IntegerField(blank=True, null=True)
    healthpropertyremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_expendedhealthproperties'


class TbExpertcollect(models.Model):
    expertcollectid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_doctorid_id = models.BigIntegerField(blank=True, null=True)
    collectiontime = models.DateTimeField(blank=True, null=True)
    collectionremarks = models.CharField(max_length=1024, blank=True)
    collectionstatusflag = models.SmallIntegerField(blank=True, null=True)
    collectioncontentsnapshot = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_expertcollect'


class TbFoodfeature(models.Model):
    eatingfeatureid = models.IntegerField(primary_key=True)
    eatinghabitsdetermine = models.CharField(max_length=10, blank=True)
    eatinghabitanalysis = models.CharField(max_length=500, blank=True)
    averageenergyintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    energyintakeunit = models.CharField(max_length=10, blank=True)
    averagemoistureintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    moistureintakeunit = models.CharField(max_length=10, blank=True)
    averageproteinintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    proteinintakeunit = models.CharField(max_length=10, blank=True)
    averagefatintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fatintakeunit = models.CharField(max_length=10, blank=True)
    averagefiberintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fiberintakeunit = models.CharField(max_length=10, blank=True)
    averagecarbohydrateintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    carbohydrateintakeunit = models.CharField(max_length=10, blank=True)
    averagevitaminaintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminaintakeunit = models.CharField(max_length=10, blank=True)
    averagevitaminb1intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb1intakeunit = models.CharField(max_length=10, blank=True)
    averagevitaminb2intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb2intakeunit = models.CharField(max_length=10, blank=True)
    averagevitaminb6intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb6intakeunit = models.CharField(max_length=10, blank=True)
    averagevitaminb12intake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb12intakeunit = models.CharField(max_length=10, blank=True)
    averagevitamincintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamincintakeunit = models.CharField(max_length=10, blank=True)
    averagevitamindintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamindintakeunit = models.CharField(max_length=10, blank=True)
    averagevitamineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamineintakeunit = models.CharField(max_length=10, blank=True)
    averagevitaminkintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminkintakeunit = models.CharField(max_length=10, blank=True)
    averagenicotinicacidintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nicotinicacidintakeunit = models.CharField(max_length=10, blank=True)
    averagefolateintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    folateintakeunit = models.CharField(max_length=10, blank=True)
    averagesodiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sodiumintakeunit = models.CharField(max_length=10, blank=True)
    averagecalciumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    calciumintakeunit = models.CharField(max_length=10, blank=True)
    averageironintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ironintakeunit = models.CharField(max_length=10, blank=True)
    averagepotassiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    potassiumintakeunit = models.CharField(max_length=10, blank=True)
    averagezincintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    zincintakeunit = models.CharField(max_length=10, blank=True)
    averagemagnesiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    magnesiumintakeunit = models.CharField(max_length=10, blank=True)
    averagecopperintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    copperintakeunit = models.CharField(max_length=10, blank=True)
    averagechomuimintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    chomuimintakeunit = models.CharField(max_length=10, blank=True)
    averagemangaesiumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mangaesiumintakeunit = models.CharField(max_length=10, blank=True)
    averagemolybdenumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    molybdenumintakeunit = models.CharField(max_length=10, blank=True)
    averageiodineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    iodineintakeunit = models.CharField(max_length=10, blank=True)
    averagephosphrusintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    phosphrusintakeunit = models.CharField(max_length=10, blank=True)
    averageseleniumintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    seleniumintakeunit = models.CharField(max_length=10, blank=True)
    averagefluorineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fluorineintakeunit = models.CharField(max_length=10, blank=True)
    averagecholesterolintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cholesterolintakeunit = models.CharField(max_length=10, blank=True)
    averagesaturatedintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    saturatedintakeunit = models.CharField(max_length=10, blank=True)
    averageacidregurgitationintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    acidregurgitationintakeunit = models.CharField(max_length=10, blank=True)
    averagebiotinintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    biotinintakeunit = models.CharField(max_length=10, blank=True)
    averagecholineintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cholineintakeunit = models.CharField(max_length=10, blank=True)
    temp_amountstdid_id = models.IntegerField(blank=True, null=True)
    latelymaintentime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_foodfeature'


class TbFoodmedicinaleffecttype(models.Model):
    medicinaleffecttypeid = models.IntegerField(primary_key=True)
    medicinaleffecttypename = models.CharField(max_length=100, blank=True)
    medicinaleffecttypecode = models.IntegerField(blank=True, null=True)
    medicinaleffecttypeexp = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodmedicinaleffecttype'


class TbFoodmedicinalprop(models.Model):
    foodmedicinalpropid = models.IntegerField(primary_key=True)
    medicineproperty = models.CharField(max_length=50, blank=True)
    medicineflavor = models.CharField(max_length=50, blank=True)
    medicineeffect = models.CharField(max_length=1024, blank=True)
    medicinepropremarks = models.CharField(max_length=1024, blank=True)
    temp_medicinaleffecttypeid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_foodmedicinalprop'


class TbFoodmedicinalpropmapp(models.Model):
    foodmedicinalpropmappid = models.IntegerField(primary_key=True)
    temp_commonfoodid_id = models.IntegerField(blank=True, null=True)
    temp_foodmedicinalpropid_id = models.IntegerField(blank=True, null=True)
    foodmedicinalpropmappexp = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodmedicinalpropmapp'


class TbFoodnutritioncontent(models.Model):
    foodnutritionid = models.IntegerField(primary_key=True)
    foodenergy = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    energyunit = models.CharField(max_length=10, blank=True)
    foodmoisture = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    moistureyunit = models.CharField(max_length=10, blank=True)
    proteincontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    proteinyunit = models.CharField(max_length=10, blank=True)
    fatcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fatyunit = models.CharField(max_length=10, blank=True)
    fibercontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fiberyunit = models.CharField(max_length=10, blank=True)
    carbohydratecontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    carbohydrateyunit = models.CharField(max_length=10, blank=True)
    vitaminacontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminaunit = models.CharField(max_length=10, blank=True)
    vitaminb1content = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb1unit = models.CharField(max_length=10, blank=True)
    vitaminb2content = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb2unit = models.CharField(max_length=10, blank=True)
    vitaminb6content = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb6unit = models.CharField(max_length=10, blank=True)
    vitaminb12content = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminb12unit = models.CharField(max_length=10, blank=True)
    vitaminccontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamincunit = models.CharField(max_length=10, blank=True)
    vitamindcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamindunit = models.CharField(max_length=10, blank=True)
    vitaminecontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitamineunit = models.CharField(max_length=10, blank=True)
    vitaminkcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vitaminkunit = models.CharField(max_length=10, blank=True)
    nicotinicacidcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nicotinicacidunit = models.CharField(max_length=10, blank=True)
    folatecontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    folateunit = models.CharField(max_length=10, blank=True)
    sodiumcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sodiumunit = models.CharField(max_length=10, blank=True)
    calciumcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    calciumunit = models.CharField(max_length=10, blank=True)
    ironcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ironunit = models.CharField(max_length=10, blank=True)
    potassiumcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    potassiumunit = models.CharField(max_length=10, blank=True)
    zinccontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    zincunit = models.CharField(max_length=10, blank=True)
    magnesiumcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    magnesiumunit = models.CharField(max_length=10, blank=True)
    coppercontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    copperunit = models.CharField(max_length=10, blank=True)
    chromiumcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    chromiumunit = models.CharField(max_length=10, blank=True)
    mangaesscontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    mangaessunit = models.CharField(max_length=10, blank=True)
    molybdenumcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    molybdenumunit = models.CharField(max_length=10, blank=True)
    iodinecontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    iodineunit = models.CharField(max_length=10, blank=True)
    phosphruscontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    phosphrusunit = models.CharField(max_length=10, blank=True)
    seleniumcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    seleniumunit = models.CharField(max_length=10, blank=True)
    fluorinecontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fluorineunit = models.CharField(max_length=10, blank=True)
    cholesterolcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cholesterounit = models.CharField(max_length=10, blank=True)
    saturatedfattyacidcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    saturatedfattyacidunit = models.CharField(max_length=10, blank=True)
    acidregurgitationcontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    acidregurgitationunit = models.CharField(max_length=10, blank=True)
    biotincontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    biotinunit = models.CharField(max_length=10, blank=True)
    cholinecontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cholineunit = models.CharField(max_length=10, blank=True)
    carotenecontent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    caroteneunit = models.CharField(max_length=10, blank=True)
    edibleparts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_foodnutritioncontent'


class TbFoodnutritionelement(models.Model):
    elementid = models.IntegerField(primary_key=True)
    elementzh = models.CharField(max_length=20, blank=True)
    elementen = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodnutritionelement'


class TbFoodwidecategories(models.Model):
    foodwidecategoryid = models.IntegerField(primary_key=True)
    foodwidecatename = models.CharField(max_length=50, blank=True)
    foodwidecatecode = models.IntegerField(blank=True, null=True)
    foodwidecateexplain = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodwidecategories'


class TbHealthindicatorinfo(models.Model):
    healthindicatorid = models.IntegerField(primary_key=True)
    healthindicatorname = models.CharField(max_length=50, blank=True)
    healthindicatorvalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    healthindicatorchange = models.CharField(max_length=100, blank=True)
    indicatorchangeexplain = models.CharField(max_length=200, blank=True)
    temp_healthtrendid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_healthindicatorinfo'


class TbHealthknowledgecollection(models.Model):
    healthknowledgecollid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_healthknowledgeid_id = models.BigIntegerField(blank=True, null=True)
    collectiontime = models.DateTimeField(blank=True, null=True)
    collectionremarks = models.CharField(max_length=1024, blank=True)
    collectionstatusflag = models.SmallIntegerField(blank=True, null=True)
    collectioncontentsnapshot = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthknowledgecollection'


class TbHealthknowledgelimited(models.Model):
    healthknowllimitedid = models.IntegerField(primary_key=True)
    healthknowllimitedattname = models.CharField(max_length=50, blank=True)
    healthknowllimitedstatus = models.SmallIntegerField(blank=True, null=True)
    healthknowllimitedstatuslevel = models.SmallIntegerField(blank=True, null=True)
    temp_healthknowledgeid_id = models.BigIntegerField(blank=True, null=True)
    healthknowllimitedexp = models.CharField(max_length=200, blank=True)
    healthknowllimitedremarks = models.CharField(max_length=200, blank=True)
    healthknowllimitedvalue = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthknowledgelimited'


class TbHealthknowledgetype(models.Model):
    healthknowltypeid = models.IntegerField(primary_key=True)
    healthknowltypename = models.CharField(max_length=50, blank=True)
    healthknowltypecode = models.IntegerField(blank=True, null=True)
    healthknowltypeexp = models.CharField(max_length=200, blank=True)
    healthknowltyperemarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthknowledgetype'


class TbHealthrecommendscollection(models.Model):
    healthrecommendscolid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_healthsuggestid_id = models.BigIntegerField(blank=True, null=True)
    collectiontime = models.DateTimeField(blank=True, null=True)
    collectionremarks = models.CharField(max_length=1024, blank=True)
    collectionstatusflag = models.SmallIntegerField(blank=True, null=True)
    collectioncontentsnapshot = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthrecommendscollection'


class TbHealthsuggestions(models.Model):
    healthsuggestid = models.BigIntegerField(primary_key=True)
    healthsuggestcontent = models.CharField(max_length=1024, blank=True)
    healthsuggesttitle = models.CharField(max_length=100, blank=True)
    healthsuggestremarks = models.CharField(max_length=1024, blank=True)
    temp_healthsuggtypeid_id = models.IntegerField(blank=True, null=True)
    healthsuggestflag = models.IntegerField(blank=True, null=True)
    healthsuggestcode = models.BigIntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggestions'


class TbHealthsuggestionsmapp(models.Model):
    healthsuggestmappid = models.IntegerField(primary_key=True)
    healthsuggcontent = models.CharField(max_length=1024, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_healthsuggestid_id = models.BigIntegerField(blank=True, null=True)
    healthsuggestreason = models.CharField(max_length=500, blank=True)
    healthsuggesttime = models.DateTimeField(blank=True, null=True)
    healthsuggestremarks = models.CharField(max_length=500, blank=True)
    checktosee = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggestionsmapp'


class TbHealthsuggestlimited(models.Model):
    healthsuggestlimitedid = models.IntegerField(primary_key=True)
    suggestlimitedattrname = models.CharField(max_length=50, blank=True)
    suggestlimitedstatus = models.SmallIntegerField(blank=True, null=True)
    suggestlimitedstatuslevel = models.SmallIntegerField(blank=True, null=True)
    suggestlimitedexplain = models.CharField(max_length=200, blank=True)
    suggestlimitedremarks = models.CharField(max_length=200, blank=True)
    suggestlimitedvalue = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggestlimited'


class TbHealthsuggtype(models.Model):
    healthsuggtypeid = models.IntegerField(primary_key=True)
    healthsuggtypename = models.CharField(max_length=50, blank=True)
    healthsuggtypecode = models.IntegerField(blank=True, null=True)
    suggclassifyexpla = models.CharField(max_length=200, blank=True)
    healthsuggtyperemarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggtype'


class TbHealthtrendrecords(models.Model):
    healthtrendid = models.IntegerField(primary_key=True)
    heaanalysistitle = models.CharField(max_length=200, blank=True)
    healthanalysistime = models.DateTimeField(blank=True, null=True)
    healthtrendanalysiresult = models.CharField(max_length=1024, blank=True)
    temp_healthknowledgeid_id = models.BigIntegerField(blank=True, null=True)
    healthtrendanalysisremarks = models.CharField(max_length=1024, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_healthtrendrecords'


class TbHealthwarningmess(models.Model):
    healthwarningmessid = models.IntegerField(primary_key=True)
    healthwarningtitle = models.CharField(max_length=100, blank=True)
    healthwarningcontent = models.CharField(max_length=1024, blank=True)
    healthwarningremarks = models.CharField(max_length=200, blank=True)
    temp_healthsuggestid_id = models.BigIntegerField(blank=True, null=True)
    temp_healthwarningtypeid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_healthwarningmess'


class TbHealthwarningtype(models.Model):
    healthwarningtypeid = models.IntegerField(primary_key=True)
    healthwarningname = models.CharField(max_length=100, blank=True)
    healthwarningtypecode = models.IntegerField(blank=True, null=True)
    healthwarningtypeexp = models.CharField(max_length=200, blank=True)
    healthwarningtyperemarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthwarningtype'


class TbHospitaldoctorrel(models.Model):
    hospitaldocrelid = models.IntegerField(primary_key=True)
    temp_hospitalid_id = models.IntegerField(blank=True, null=True)
    temp_doctorid_id = models.IntegerField(unique=True, blank=True, null=True)
    temp_hospitalofficeid_id = models.IntegerField(blank=True, null=True)
    workduty = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_hospitaldoctorrel'


class TbHospitalinfo(models.Model):
    hospitalid = models.IntegerField(primary_key=True)
    hospitalname = models.CharField(max_length=100, blank=True)
    hospitalexplain = models.CharField(max_length=1024, blank=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    hospitalrank = models.CharField(max_length=100, blank=True)
    temp_adminisareaid_id = models.IntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_hospitalinfo'


class TbHospitalofficesinfo(models.Model):
    hospitalofficeid = models.IntegerField(primary_key=True)
    hospitalofficename = models.CharField(max_length=50, blank=True)
    hospitalofficeexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_hospitalofficesinfo'


class TbIdentificationissuess(models.Model):
    identifyissueid = models.IntegerField(primary_key=True)
    temp_physiqueinfoid_id = models.IntegerField(blank=True, null=True)
    identifyissuecontent = models.CharField(max_length=200, blank=True)
    identifyissueremarks = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_identificationissuess'


class TbIdentifychoices(models.Model):
    identifychoiceid = models.IntegerField(primary_key=True)
    identifychoicevalue = models.IntegerField(blank=True, null=True)
    scriptdescribe = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_identifychoices'


class TbIdentifydiseaserel(models.Model):
    identifydirelid = models.IntegerField(primary_key=True)
    temp_physiqueinfoid_id = models.IntegerField(blank=True, null=True)
    temp_commondiseaseid_id = models.IntegerField(blank=True, null=True)
    identifydirelexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_identifydiseaserel'


class TbIndicatorusermapp(models.Model):
    indicatorusermappid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_indicatorstandardid_id = models.IntegerField(blank=True, null=True)
    userindicatorvalue = models.CharField(max_length=50, blank=True)
    userindicatorexp = models.CharField(max_length=200, blank=True)
    userindicatorremarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_indicatorusermapp'


class TbIntelligentdeviceinfo(models.Model):
    intelligentdeviceid = models.IntegerField(primary_key=True)
    intelligentdevicetype = models.CharField(max_length=50, blank=True)
    intelligentdevicename = models.CharField(max_length=50, blank=True)
    intelligentdeviceweight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    intelligentdevicecolor = models.CharField(max_length=10, blank=True)
    intelligentdevicefunction = models.CharField(max_length=200, blank=True)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_intelligentdeviceinfo'


class TbLocationinfo(models.Model):
    locationinfoid = models.IntegerField(primary_key=True)
    locationlongitude = models.CharField(max_length=50, blank=True)
    locationlatitude = models.CharField(max_length=50, blank=True)
    reallocation = models.CharField(max_length=200, blank=True)
    locationremarks = models.CharField(max_length=200, blank=True)
    locationprovince = models.CharField(max_length=50, blank=True)
    locationcity = models.CharField(max_length=50, blank=True)
    locationclassify = models.CharField(max_length=50, blank=True)
    locationcounty = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_locationinfo'


class TbManager(models.Model):
    managerid = models.IntegerField(primary_key=True)
    managername = models.CharField(max_length=30, blank=True)
    managerpassword = models.CharField(max_length=50, blank=True)
    managerunit = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_manager'


class TbMeasurementunit(models.Model):
    unitattributeid = models.IntegerField(primary_key=True)
    unitattributename = models.CharField(max_length=20, blank=True)
    unitlevel = models.IntegerField(blank=True, null=True)
    unitname = models.CharField(max_length=20, blank=True)
    hexadecimal = models.IntegerField(blank=True, null=True)
    unitremarks = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_measurementunit'


class TbMedicalhistoryrecords(models.Model):
    medicalhistoryrecordid = models.IntegerField(primary_key=True)
    diseasetype = models.CharField(max_length=100, blank=True)
    diseasename = models.CharField(max_length=100, blank=True)
    diseaseseverity = models.CharField(max_length=100, blank=True)
    treatmentinfo = models.CharField(max_length=1024, blank=True)
    treatmentdoctor = models.CharField(max_length=50, blank=True)
    treatmentunit = models.CharField(max_length=100, blank=True)
    treatmentlocation = models.CharField(max_length=100, blank=True)
    treatmentresult = models.CharField(max_length=1024, blank=True)
    recoverydegree = models.CharField(max_length=1024, blank=True)
    treatmenttime = models.DateTimeField(blank=True, null=True)
    treatmentremarks = models.CharField(max_length=1024, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_doctorid_id = models.IntegerField(blank=True, null=True)
    temp_medicineuseinfoid_id = models.BigIntegerField(blank=True, null=True)
    temp_commondiseaseid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_medicalhistoryrecords'


class TbMedicineinfo(models.Model):
    chinesemedicineid = models.IntegerField(primary_key=True)
    medicinename = models.CharField(max_length=50, blank=True)
    medicinegeneraltype = models.CharField(max_length=50, blank=True)
    medicinesubtype = models.CharField(max_length=50, blank=True)
    medicinetoxicity = models.CharField(max_length=50, blank=True)
    medicineproperty = models.CharField(max_length=100, blank=True)
    medicinetaste = models.CharField(max_length=50, blank=True)
    indicationsfunction = models.CharField(max_length=1024, blank=True)
    channeltropism = models.CharField(max_length=1024, blank=True)
    clinicalapplication = models.CharField(max_length=1024, blank=True)
    medicinegenera = models.CharField(max_length=1024, blank=True)
    prescriptionname = models.CharField(max_length=1024, blank=True)
    generaldosage = models.CharField(max_length=1024, blank=True)
    generalusage = models.CharField(max_length=1024, blank=True)
    withmedicine = models.CharField(max_length=1024, blank=True)
    comment = models.CharField(max_length=1024, blank=True)
    prescriptionsexample = models.CharField(max_length=1024, blank=True)
    medicineremarks = models.CharField(max_length=1024, blank=True)
    medicinecode = models.BigIntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_medicineinfo'


class TbMedicineprescription(models.Model):
    medicineprescriptionid = models.IntegerField(primary_key=True)
    medicineprescriptionname = models.CharField(max_length=50, blank=True)
    prescriptionindications = models.CharField(max_length=200, blank=True)
    prescriptionusage = models.CharField(max_length=100, blank=True)
    prescriptionmethod = models.CharField(max_length=100, blank=True)
    prescriptioncharacters = models.CharField(max_length=100, blank=True)
    prescriptionspecification = models.CharField(max_length=100, blank=True)
    prescriptionstore = models.CharField(max_length=50, blank=True)
    prescriptioncontraindicat = models.CharField(max_length=200, blank=True)
    prescriptiontheories = models.CharField(max_length=500, blank=True)
    prescriptionextract = models.CharField(max_length=500, blank=True)
    prescriptionremarks = models.CharField(max_length=500, blank=True)
    prescriptiontag = models.CharField(max_length=50, blank=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_medicineprescription'


class TbMedicineprescriptionmapp(models.Model):
    medprescriptmappid = models.IntegerField(primary_key=True)
    temp_chinesemedicineid_id = models.IntegerField(blank=True, null=True)
    temp_medicineprescriptionid_id = models.BigIntegerField(blank=True, null=True)
    medicineamount = models.CharField(max_length=30, blank=True)
    medprescriptmappremarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_medicineprescriptionmapp'


class TbMedicineuseinfo(models.Model):
    medicineuseinfoid = models.IntegerField(primary_key=True)
    medicineusetype = models.CharField(max_length=100, blank=True)
    medicineusename = models.CharField(max_length=50, blank=True)
    medicineusedose = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    medicineuseremarks = models.CharField(max_length=1024, blank=True)
    temp_tcmexaminationid_id = models.BigIntegerField(blank=True, null=True)
    temp_unitattributeid_id = models.IntegerField(blank=True, null=True)
    prescriptiontag = models.CharField(max_length=50, blank=True)
    temp_chinesemedicineid_id = models.IntegerField(blank=True, null=True)
    temp_medicineprescriptionid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_medicineuseinfo'


class TbMovementdetailrecords(models.Model):
    movementdetailid = models.IntegerField(primary_key=True)
    movementstarttime = models.DateTimeField(blank=True, null=True)
    movementstoptime = models.DateTimeField(blank=True, null=True)
    temp_exerciseid_id = models.IntegerField(blank=True, null=True)
    temp_sportrecordid_id = models.BigIntegerField(blank=True, null=True)
    movementdetailremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_movementdetailrecords'


class TbMycollection(models.Model):
    mycollectionid = models.IntegerField(primary_key=True)
    collectionclass = models.CharField(max_length=50, blank=True)
    collectioncode = models.BigIntegerField(blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_mycollection'


class TbPhoneappinfo(models.Model):
    appinfoid = models.IntegerField(primary_key=True)
    apptype = models.CharField(max_length=20, blank=True)
    appname = models.CharField(max_length=30, blank=True)
    apptag = models.CharField(max_length=50, blank=True)
    appotherinfo = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_phoneappinfo'


class TbPhoneinfo(models.Model):
    phoneinfoid = models.IntegerField(primary_key=True)
    phoneuniqunum = models.CharField(max_length=100, blank=True)
    phonenum = models.CharField(max_length=30, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_phoneinfo'


class TbPhonemonitorrecords(models.Model):
    phoneappmonitorrecordid = models.IntegerField(primary_key=True)
    temp_appinfoid_id = models.IntegerField(blank=True, null=True)
    appopentime = models.DateTimeField(blank=True, null=True)
    appclosetime = models.DateTimeField(blank=True, null=True)
    appusetime = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    temp_phoneinfoid_id = models.IntegerField(blank=True, null=True)
    recordproducttime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_phonemonitorrecords'


class TbPhonepreferuserecords(models.Model):
    phonepreferuseid = models.IntegerField(primary_key=True)
    oftenusebeginat = models.TimeField(blank=True, null=True)
    oftenuseovertime = models.TimeField(blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    temp_appinfoid_id = models.IntegerField(blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_amountstdid_id = models.IntegerField(blank=True, null=True)
    additemtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_phonepreferuserecords'


class TbPhysiqueinfo(models.Model):
    physiqueinfoid = models.IntegerField(primary_key=True)
    tablescoreheight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    tablescorelow = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    switchscoreheight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    switchscorelow = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    generacharacter = models.CharField(max_length=1024, blank=True)
    shapefeature = models.CharField(max_length=1024, blank=True)
    commonmanifest = models.CharField(max_length=1024, blank=True)
    mentalcharacter = models.CharField(max_length=1024, blank=True)
    incidencetendency = models.CharField(max_length=1024, blank=True)
    adaptivecapacity = models.CharField(max_length=1024, blank=True)
    physicaltypename = models.CharField(max_length=20, blank=True)
    physicaltypecode = models.IntegerField(blank=True, null=True)
    adjustmethod = models.CharField(max_length=1024, blank=True)
    multiplepeople = models.CharField(max_length=1024, blank=True)
    physicalinterpretation = models.CharField(max_length=1024, blank=True)
    physicalreason = models.CharField(max_length=1024, blank=True)
    physicaladjustmethod = models.CharField(max_length=1024, blank=True)
    foodallowtaboo = models.CharField(max_length=1024, blank=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_physiqueinfo'


class TbPicturelist(models.Model):
    picturelocationid = models.IntegerField(primary_key=True)
    originalpicturepath = models.CharField(max_length=1024, blank=True)
    smallpicturepath = models.CharField(max_length=1024, blank=True)
    pictureclass = models.CharField(max_length=100, blank=True)
    picturename = models.CharField(max_length=100, blank=True)
    picturetitle = models.CharField(max_length=100, blank=True)
    pictureusecode = models.BigIntegerField(blank=True, null=True)
    pictureremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_picturelist'


class TbRecommendedconditionsmapp(models.Model):
    recommendedconditionsmappid = models.IntegerField(primary_key=True)
    temp_healthsuggestlimitedid_id = models.IntegerField(blank=True, null=True)
    temp_healthsuggestid_id = models.BigIntegerField(blank=True, null=True)
    recommendmappremarks = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_recommendedconditionsmapp'


class TbSetmealfoodmapp(models.Model):
    mealfoodmapid = models.IntegerField(primary_key=True)
    temp_commonfoodid_id = models.IntegerField(blank=True, null=True)
    temp_setmealinfoid_id = models.BigIntegerField(blank=True, null=True)
    mealfoodmapremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_setmealfoodmapp'


class TbSleepdetailprocessrecords(models.Model):
    sleepdetailrecordsid = models.IntegerField(primary_key=True)
    temp_sleeprecordid_id = models.BigIntegerField(blank=True, null=True)
    temp_sleepstatuscategoryid_id = models.SmallIntegerField(blank=True, null=True)
    sleepstatusbegintime = models.DateTimeField(blank=True, null=True)
    sleepstatusovertime = models.DateTimeField(blank=True, null=True)
    sleepstatusduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sleepstatusremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_sleepdetailprocessrecords'


class TbSleepinforecords(models.Model):
    sleeprecordid = models.IntegerField(primary_key=True)
    airhumidity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ambienttemperature = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ambientnoise = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sleepbegin = models.DateTimeField(blank=True, null=True)
    sleepover = models.DateTimeField(blank=True, null=True)
    deepsleeptime = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    shallowsleeptime = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sleepremarks = models.CharField(max_length=150, blank=True)
    sleeprecorduptime = models.DateTimeField(blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    waketimes = models.IntegerField(blank=True, null=True)
    temp_intelligentdeviceid_id = models.IntegerField(blank=True, null=True)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    sleepuploadflag = models.BigIntegerField(blank=True, null=True)
    awaketime = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_sleepinforecords'


class TbSleeppreferrecords(models.Model):
    sleeppreferid = models.IntegerField(primary_key=True)
    prefersleepbeginat = models.TimeField(blank=True, null=True)
    prefersleepoverat = models.TimeField(blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    sleepfeatureaddtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sleeppreferrecords'


class TbSleepstatuscategory(models.Model):
    sleepstatuscategoryid = models.IntegerField(primary_key=True)
    sleepstatusname = models.CharField(max_length=20, blank=True)
    sleepstatuscode = models.SmallIntegerField(blank=True, null=True)
    sleepstatusexplain = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_sleepstatuscategory'


class TbSportinforecords(models.Model):
    sportrecordid = models.IntegerField(primary_key=True)
    walkstepnumber = models.BigIntegerField(blank=True, null=True)
    runstepnumber = models.BigIntegerField(blank=True, null=True)
    walkdistance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    rundistance = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    calorieconsumption = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sportbegintime = models.DateTimeField(blank=True, null=True)
    sportovertime = models.DateTimeField(blank=True, null=True)
    sportrecorduptime = models.DateTimeField(blank=True, null=True)
    sportinforemarks = models.CharField(max_length=150, blank=True)
    sportanalysis = models.CharField(max_length=1024, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    sport_mode = models.CharField(max_length=100, blank=True)
    temp_intelligentdeviceid_id = models.IntegerField(blank=True, null=True)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    uploadflag = models.BigIntegerField(blank=True, null=True)
    restingcalorieconsume = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    movecalorieconsume = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    crawledfloor = models.IntegerField(blank=True, null=True)
    fallitems = models.SmallIntegerField(blank=True, null=True)
    activeduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    longestactiveduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    longestidleduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    temp_exerciseid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sportinforecords'


class TbStatisticofclick(models.Model):
    statisticclickid = models.IntegerField(primary_key=True)
    clickclass = models.CharField(max_length=50, blank=True)
    clickitem = models.BigIntegerField(blank=True, null=True)
    praiseyn = models.SmallIntegerField(blank=True, null=True)
    statisticclickremarks = models.CharField(max_length=100, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_statisticofclick'


class TbSupervisorylevel(models.Model):
    superlevelid = models.IntegerField(primary_key=True)
    temp_managerid_id = models.IntegerField(blank=True, null=True)
    temp_adminisareaid_id = models.IntegerField(blank=True, null=True)
    managerrank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_supervisorylevel'


class TbTcmdcotorsinfo(models.Model):
    doctorid = models.IntegerField(primary_key=True)
    doctorname = models.CharField(max_length=20, blank=True)
    doctorsex = models.CharField(max_length=5, blank=True)
    doctorage = models.IntegerField(blank=True, null=True)
    professionalrands = models.CharField(max_length=100, blank=True)
    doctorworktime = models.IntegerField(blank=True, null=True)
    doctorsynopsis = models.CharField(max_length=1024, blank=True)
    researcharea = models.CharField(max_length=1024, blank=True)
    researchfindings = models.CharField(max_length=1024, blank=True)
    temp_adminisareaid_id = models.IntegerField(blank=True, null=True)
    temp_doctorexpertiseid_id = models.IntegerField(blank=True, null=True)
    doctorcode = models.BigIntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tcmdcotorsinfo'


class TbTcmdiagnosisobj(models.Model):
    diagnosisobjid = models.IntegerField(primary_key=True)
    diagnosisobjname = models.CharField(max_length=50, blank=True)
    diagnosisobjexplain = models.CharField(max_length=1024, blank=True)
    temp_diagnosistypeid_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tcmdiagnosisobj'


class TbTcmdiagnosistype(models.Model):
    diagnosistypeid = models.IntegerField(primary_key=True)
    diagnosistypename = models.CharField(max_length=50, blank=True)
    diagnosistypecode = models.IntegerField(blank=True, null=True)
    diagnosistypeexplain = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_tcmdiagnosistype'


class TbTcmhealthknowledge(models.Model):
    healthknowledgeid = models.IntegerField(primary_key=True)
    healthknowledgetitle = models.CharField(max_length=200, blank=True)
    healthknowledgecontent = models.CharField(max_length=1024, blank=True)
    exersuggtime = models.DateTimeField(blank=True, null=True)
    temp_managerid_id = models.IntegerField(blank=True, null=True)
    healthknowledgeremarks = models.CharField(max_length=1024, blank=True)
    temp_healthknowltypeid_id = models.IntegerField(blank=True, null=True)
    healthknowledgecode = models.BigIntegerField(blank=True, null=True)
    healthknowledgeflag = models.IntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_tcmhealthknowledge'


class TbUser(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, blank=True)
    usersex = models.CharField(max_length=5, blank=True)
    userage = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True)
    userphonenumber = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50, blank=True)
    userrank = models.CharField(max_length=5, blank=True)
    userwroktype = models.CharField(max_length=100, blank=True)
    userbmiindex = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    temp_sleepfeatureid = models.IntegerField(blank=True, null=True)
    temp_exercisefeatureid = models.IntegerField(blank=True, null=True)
    temp_eatingfeatureid = models.IntegerField(blank=True, null=True)
    temp_adminisareaid_id = models.IntegerField(blank=True, null=True)
    temp_picturelocationid_id = models.BigIntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.NullBooleanField()
    is_admin = models.NullBooleanField()
    name = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_user'


class TbUseranswerrecords(models.Model):
    issuescoremappid = models.BigIntegerField(primary_key=True)
    temp_identifyissueid_id = models.IntegerField(blank=True, null=True)
    temp_identifychoiceid_id = models.IntegerField(blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    getscore = models.IntegerField(blank=True, null=True)
    answerflag = models.BigIntegerField(blank=True, null=True)
    answertime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_useranswerrecords'


class TbUserexercisefeature(models.Model):
    exercisefeatureid = models.IntegerField(primary_key=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    steplength = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    runsteplength = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    standardweight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    datauptime = models.DateTimeField(blank=True, null=True)
    exercisefeatureremarks = models.CharField(max_length=150, blank=True)
    motilityindex = models.CharField(max_length=20, blank=True)
    exercisehabitsdetermine = models.CharField(max_length=500, blank=True)
    exercisehabitanalysis = models.CharField(max_length=500, blank=True)
    averageexcitetime = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    exercisetypeprefer = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_userexercisefeature'


class TbUserhealthattrmapp(models.Model):
    userhealthattrmappid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    temp_exphealthpropertyid_id = models.IntegerField(blank=True, null=True)
    expendhealthattrvalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    temp_unitattributeid_id = models.IntegerField(blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    currentuseflag = models.SmallIntegerField(blank=True, null=True)
    userattrmappingexplain = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_userhealthattrmapp'


class TbUserhealthwarningmapp(models.Model):
    userhealthwarningid = models.IntegerField(primary_key=True)
    healthwarningcontent = models.CharField(max_length=1024, blank=True)
    healthwarningtime = models.DateTimeField(blank=True, null=True)
    healthwarningreason = models.CharField(max_length=500, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    healthwarningremarks = models.CharField(max_length=500, blank=True)
    temp_healthwarningmessid_id = models.BigIntegerField(blank=True, null=True)
    checktosee = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_userhealthwarningmapp'


class TbUserknowledgemapp(models.Model):
    userknowledgemappid = models.IntegerField(primary_key=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)
    healthknowledgecontent = models.CharField(max_length=1024, blank=True)
    temp_healthknowledgeid_id = models.BigIntegerField(blank=True, null=True)
    healthknowledgereason = models.CharField(max_length=500, blank=True)
    healthknowledgetime = models.DateTimeField(blank=True, null=True)
    healthknowledgeremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_userknowledgemapp'


class TbUserreviewstat(models.Model):
    userreviewstatid = models.IntegerField(primary_key=True)
    userreviewclass = models.CharField(max_length=50, blank=True)
    userreviewitem = models.BigIntegerField(blank=True, null=True)
    userreviewcontent = models.CharField(max_length=1024, blank=True)
    userreviewremarks = models.CharField(max_length=500, blank=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_userreviewstat'


class TbUsersleepfeature(models.Model):
    sleepfeatureid = models.IntegerField(primary_key=True)
    airhumidity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ambienttemperature = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ambientnoise = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    bedtimehabits = models.CharField(max_length=100, blank=True)
    goodbedtimehabits = models.CharField(max_length=5, blank=True)
    siestahabit = models.CharField(max_length=5, blank=True)
    averagesleeptime = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sleephabitdetermination = models.CharField(max_length=10, blank=True)
    sleepindex = models.CharField(max_length=20, blank=True)
    sleephabitanalysis = models.CharField(max_length=500, blank=True)
    temp_locationinfoid_id = models.BigIntegerField(blank=True, null=True)
    latelymaintentime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_usersleepfeature'


class TbVariousindicatorlimited(models.Model):
    indicatorlimitedid = models.IntegerField(primary_key=True)
    temp_indicatorstandardid_id = models.IntegerField(blank=True, null=True)
    indicatorstandardname = models.CharField(max_length=50, blank=True)
    indicatorstandardstatus = models.SmallIntegerField(blank=True, null=True)
    indicatorstandardcode = models.IntegerField(blank=True, null=True)
    indicatorstandardvalue = models.CharField(max_length=50, blank=True)
    indicatorstandardstatuslevel = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_variousindicatorlimited'


class TbVariousindicatorstandard(models.Model):
    indicatorstandardid = models.IntegerField(primary_key=True)
    indicatorname = models.CharField(max_length=50, blank=True)
    indicatorcode = models.IntegerField(blank=True, null=True)
    indicatorstatus = models.SmallIntegerField(blank=True, null=True)
    indicatorvalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    indicatorremarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_variousindicatorstandard'


class TbWesmedicineexamitem(models.Model):
    westmedicineexamid = models.IntegerField(primary_key=True)
    westmedicineitemname = models.CharField(max_length=50, blank=True)
    wesmedicineitemexpl = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_wesmedicineexamitem'


class TbWtreatmentrecords(models.Model):
    wtreatmentrecordid = models.IntegerField(primary_key=True)
    temp_westmedicineexamid_id = models.IntegerField(blank=True, null=True)
    wesexamresultval = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    temp_userid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtreatmentrecords'


class Userhealthknowledge(models.Model):
    userknowledgemappid = models.IntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=30, blank=True)
    healthknowltypeid = models.IntegerField(blank=True, null=True)
    healthknowltypename = models.CharField(max_length=50, blank=True)
    healthknowledgetitle = models.CharField(max_length=200, blank=True)
    healthknowledgecontent = models.CharField(max_length=1024, blank=True)
    healthknowledgetime = models.DateTimeField(blank=True, null=True)
    healthknowledgecode = models.BigIntegerField(blank=True, null=True)
    temp_picturelistid_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userhealthknowledge'
