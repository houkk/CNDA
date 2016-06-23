#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
from django.db import models
from PIL import Image
# Create your models here.

class RestFrameworkToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    user = models.ForeignKey('TbUser', unique=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rest_framework_token'

class Register(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    aboutYou = models.CharField(max_length=100)
    mailinglist = models.BooleanField(default=False)
    class Meta:
        managed = False
    def __unicode__(self):

        return self.name

def get_image(instance, filename):
    if instance.pictureremarks:
        return unicode('static/pictures/'+instance.pictureremarks+'/'+filename)
    else:
        return 'static/pictures/'+filename


class TbPicturelist(models.Model):
    """
    图片列表
    """
    picturelocationid = models.AutoField(primary_key=True)
    originalpicturepath = models.ImageField(upload_to=get_image, blank=True, null=True)
    #originalpicturepath = models.CharField(max_length=1024, blank=True)
    smallpicturepath = models.CharField(max_length=1024, blank=True)
    pictureclass = models.CharField(max_length=100, blank=True)
    picturename = models.CharField(max_length=100, blank=True)
    picturetitle = models.CharField(max_length=100, blank=True)
    pictureusecode = models.IntegerField(blank=True, null=True)
    pictureremarks = models.CharField(max_length=500, blank=True, null=True,
                                      choices=(
                                                ('test', 'test'),
                                                ('head', 'head'),
                                                ('healthknowledge', 'healthknowledge'),
                                                ('physicalinformation', 'physicalinformation'),
                                                ('other', 'other')
                                              )
                                     )

    class Meta:
        managed = False
        db_table = 'tb_picturelist'
        ordering = ['picturelocationid']
    def __unicode__(self):
        return '%d:%s' % (self.picturelocationid, self.picturename)


class TbManager(models.Model):
    """
    管理员实体，记录管理员基本信息
    """
    managerid = models.AutoField(primary_key=True)
    managername = models.CharField(max_length=30, blank=True)
    managerpassword = models.CharField(max_length=50, blank=True)
    managerunit = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_manager'
        ordering = ['managerid']
    def __unicode__(self):
        return '%d:%s' % (self.managerid, self.managername)



class TbAdminisarea(models.Model):
    """
    行政区划代码表
    """
    adminisareaid = models.AutoField(primary_key=True)
    adminisareacode = models.CharField(max_length=15, blank=True)
    adminisareaprovince = models.CharField(max_length=50, blank=True)
    adminisareacity = models.CharField(max_length=50, blank=True)
    adminisareacounty = models.CharField(max_length=50, blank=True)
    adminisarearemarks = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_adminisarea'
        ordering = ['adminisareaid']
    def __unicode__(self):
        return '%d:%s%s%s' % (self.adminisareaid, self.adminisareaprovince, self.adminisareacity, self.adminisareacounty)


class TbAverageamountstd(models.Model):
    """
    平均量计算标准
    """
    amountstdid = models.AutoField(primary_key=True)
    amountnumofdays = models.BigIntegerField(blank=True, null=True)
    averageamountremarks = models.CharField(max_length=100, blank=True)
    amountbegintime = models.TimeField(blank=True, null=True)
    amountstoptime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_averageamountstd'
    def __unicode__(self):
        return '%d:%d' % (self.amountstdid, self.amountnumofdays)


class TbCommondiseasetype(models.Model):
    """
    常见疾病类别表
    """
    commonditypeid = models.AutoField(primary_key=True)
    commonditypename = models.CharField(max_length=50, blank=True)
    commonditypecode = models.IntegerField(blank=True, null=True)
    diclassifyexplain = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_commondiseasetype'
        ordering = ['commonditypeid']
    def __unicode__(self):
        return '%d:%s' % (self.commonditypeid, self.commonditypename)
class TbCommondiseaseinfo(models.Model):
    """
    常见疾病信息表
    """
    commondiseaseid = models.AutoField(primary_key=True)
    #temp_commonditypeid = models.IntegerField(blank=True, null=True)
    temp_commonditypeid = models.ForeignKey(TbCommondiseasetype, related_name='commondiseaseinfo', blank=True, null=True, on_delete=models.SET_NULL)
    commondiname = models.CharField(max_length=50, blank=True)
    diseaseexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_commondiseaseinfo'
        ordering = ['commondiseaseid']
    def __unicode__(self):
        return '%d:%s' % (self.commondiseaseid, self.commondiname)



class TbFoodwidecategories(models.Model):
    """
    食物大类表
    """
    foodwidecategoryid = models.IntegerField(primary_key=True)
    foodwidecatename = models.CharField(max_length=50, blank=True)
    foodwidecatecode = models.IntegerField(blank=True, null=True)
    foodwidecateexplain = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodwidecategories'
        ordering = ['foodwidecategoryid']
    def __unicode__(self):
        return '%d:%s' % (self.foodwidecategoryid, self.foodwidecatename)


class TbCommonfoodtype(models.Model):
    """
    常见食物类别表
    """
    commonfoodtypeid = models.AutoField(primary_key=True)
    commonfoodtypename = models.CharField(max_length=50, blank=True)
    commonfoodtypecode = models.IntegerField(blank=True, null=True)
    foodtypeexplain = models.CharField(max_length=1024, blank=True)
    temp_foodwidecategoryid = models.ForeignKey(TbFoodwidecategories, related_name='tbcommonfoodtype', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_commonfoodtype'
        ordering = ['commonfoodtypeid']
    def __unicode__(self):
        return '%d:%s' % (self.commonfoodtypecode, self.commonfoodtypename)
class TbMeasurementunit(models.Model):
    """
    项目中用到的计量单位在此记录
    """
    unitattributeid = models.AutoField(primary_key=True)
    unitattributename = models.CharField(max_length=20, blank=True)
    unitlevel = models.IntegerField(blank=True, null=True)
    unitname = models.CharField(max_length=20, blank=True)
    hexadecimal = models.IntegerField(blank=True, null=True)
    unitremarks = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_measurementunit'
        ordering = ['unitattributeid']
    def __unicode__(self):
        return '%d:%s' % (self.unitattributeid, self.unitname)


class TbFoodnutritionelement(models.Model):
    """
    常见食物营养成分元素表
    """
    elementid = models.AutoField(primary_key=True)
    elementzh = models.CharField(max_length=20, blank=True)
    elementen = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodnutritionelement'
        ordering = ['elementid']
    def __unicode__(self):
        return '%d:%s' % (self.elementid, self.elementzh)


class TbFoodnutritioncontent(models.Model):
    """
    食物营养含量信息表
    """
    foodnutritionid = models.AutoField(primary_key=True)
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
        ordering = ['foodnutritionid']
    def __unicode__(self):
        return '%d:%s' % (self.foodnutritionid, self.foodenergy)
class TbEatingsetmealinfo(models.Model):
    """
    饮食套餐信息表
    """
    setmealinfoid = models.AutoField(primary_key=True)
    foodtypecontent = models.IntegerField(blank=True, null=True)
    setmealname = models.CharField(max_length=50, blank=True)
    setmealexplain = models.CharField(max_length=1024, blank=True)
    setmealremarks = models.CharField(max_length=100, blank=True)
    setmealcode = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_eatingsetmealinfo'
        ordering = ['setmealinfoid']
    def __unicode__(self):
        return '%d:%s' % (self.setmealinfoid, self.setmealname)


class TbCommonfoodinfo(models.Model):
    """
    常见食物信息表
    """
    commonfoodid = models.AutoField(primary_key=True)
    commonfoodname = models.CharField(max_length=50, blank=True)
    #temp_commonfoodtypeid = models.IntegerField(blank=True, null=True)
    temp_commonfoodtypeid = models.ForeignKey(TbCommonfoodtype, related_name='commonfoodinfo', blank=True, null=True, on_delete=models.SET_NULL)
    commonfoodexplain = models.CharField(max_length=1024, blank=True)
    #temp_foodnutritionid = models.IntegerField(blank=True, null=True)
    temp_foodnutritionid = models.ForeignKey(TbFoodnutritioncontent, related_name='commonfoodinfo', blank=True, null=True, on_delete=models.SET_NULL)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='commonfoodinfo', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_commonfoodinfo'
        ordering = ['commonfoodid']
    def __unicode__(self):
        return "%d:%s" % (self.commonfoodid, self.commonfoodname)

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=UserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None):

        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class TbUser(AbstractBaseUser):
    """
    用户实体，记录用户基本信息
    """
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=True, unique=True)
    name = models.CharField(max_length=30, blank=True,)
    usersex = models.CharField(max_length=5, blank=True)
    userage = models.IntegerField(blank=True, null=True)
    #userpassword = models.CharField(max_length=50, blank=True)
    userphonenumber = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50, blank=True, unique=True)
    userrank = models.CharField(max_length=5, blank=True)
    userwroktype = models.CharField(max_length=100, blank=True)
    userbmiindex = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    temp_sleepfeatureid = models.IntegerField(blank=True, null=True)
    temp_exercisefeatureid = models.IntegerField(blank=True, null=True)
    temp_eatingfeatureid = models.IntegerField(blank=True, null=True)
    #temp_adminisareaid = models.IntegerField(blank=True, null=True)
    #temp_adminisareaid_id =models.IntegerField(blank=True, null=True)
    temp_adminisareaid = models.ForeignKey(TbAdminisarea, related_name='user', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_picturelocationid_id = models.IntegerField(blank=True, null=True)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='user', blank=True, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
    def __unicode__(self):
        return '%d:%s' % (self.userid, self.username)
    class Meta:
        managed = False
        db_table = 'tb_user'
        ordering = ['userid']

    def get_full_name(self):

        return self.email
    def get_short_name(self):
        return self.name
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# class TbUser(models.Model):
#     """
#     用户实体，记录用户基本信息
#     """
#     userid = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=30, blank=True)
#     usersex = models.CharField(max_length=5, blank=True)
#     userage = models.IntegerField(blank=True, null=True)
#     userpassword = models.CharField(max_length=50, blank=True)
#     userphonenumber = models.CharField(max_length=15, blank=True)
#     usermail = models.CharField(max_length=50, blank=True, unique=True)
#     userrank = models.CharField(max_length=5, blank=True)
#     userwroktype = models.CharField(max_length=100, blank=True)
#     userbmiindex = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
#     temp_sleepfeatureid = models.IntegerField(blank=True, null=True)
#     temp_exercisefeatureid = models.IntegerField(blank=True, null=True)
#     temp_eatingfeatureid = models.IntegerField(blank=True, null=True)
#     #temp_adminisareaid = models.IntegerField(blank=True, null=True)
#     temp_adminisareaid = models.ForeignKey(TbAdminisarea, related_name='user', blank=True, null=True, on_delete=models.SET_NULL)
#     temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='user', blank=True, null=True, on_delete=models.SET_NULL)
#
#     def __unicode__(self):
#         return '%d:%s' % (self.userid, self.username)
#     class Meta:
#         managed = False
#         db_table = 'tb_user'
#         ordering = ['userid']







class TbCommonnutrientintake(models.Model):
    """
    营养素每日摄入量
    """
    nutrientid = models.AutoField(primary_key=True)
    nutrientname = models.CharField(max_length=30, blank=True)
    nutrientintakemax = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    nutrientintakemin = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    maxagefor = models.IntegerField(blank=True, null=True)
    minagefor = models.IntegerField(blank=True, null=True)
    nutrientintakeremarks = models.CharField(max_length=200, blank=True)
    #temp_unitattributeid = models.IntegerField(blank=True, null=True)
    temp_unitattributeid = models.ForeignKey(TbMeasurementunit, related_name='commonnutrientintake', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_commonnutrientintake'
        ordering = ['nutrientid']
    def __unicode__(self):
        return '%d:%s' % (self.nutrientid, self.nutrientname)






class TbPhysiqueinfo(models.Model):
    """
    体质信息表
    """
    physiqueinfoid = models.AutoField(primary_key=True)
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
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='tbphysiqueinfo', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_physiqueinfo'
        ordering = ['physiqueinfoid']
    def __unicode__(self):
        return '%d:%s' % (self.physiqueinfoid, self.physicaltypename)







class TbConstituteidentifyresult(models.Model):
    """
    体质辨识结果记录表
    """
    identifyresultid = models.AutoField(primary_key=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='constituteidentifyresult', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_physiqueinfoid = models.IntegerField(blank=True, null=True)
    temp_physiqueinfoid = models.ForeignKey(TbPhysiqueinfo, related_name='constituteidentifyresult', blank=True, null=True, on_delete=models.SET_NULL)
    constituteidentifytime = models.DateTimeField(blank=True, null=True)
    constituteidentifyremarks = models.CharField(max_length=500, blank=True)
    constituteidentifyresult = models.CharField(max_length=30, blank=True)
    constituteldentifyflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_constituteidentifyresult'
        ordering = ['identifyresultid']
    def __unicode__(self):
        return '%d:%s' % (self.identifyresultid, self.constituteidentifyresult)






class TbDoctorexpertisetype(models.Model):
    """
    医生专长分类代码表
    """
    doctorexptypeid = models.AutoField(primary_key=True)
    doctorexptypename = models.CharField(max_length=50, blank=True)
    doctorexptypecode = models.IntegerField(blank=True, null=True)
    doctorexptypeexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_doctorexpertisetype'
        ordering = ['doctorexptypeid']
    def __unicode__(self):
        return '%d:%s' % (self.doctorexptypecode, self.doctorexptypename)

class TbDoctorexpertiseinfo(models.Model):
    """
    医生专长信息表
    """
    doctorexpertiseid = models.AutoField(primary_key=True)
    doctorexpertisetitle = models.CharField(max_length=100, blank=True)
    doctorexpertiseexplain = models.CharField(max_length=1024, blank=True)
    #temp_doctorexptypeid = models.IntegerField(blank=True, null=True)
    temp_doctorexptypeid = models.ForeignKey(TbDoctorexpertisetype, related_name='doctorexpertiserinfo', blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        managed = False
        db_table = 'tb_doctorexpertiseinfo'
        ordering = ['doctorexpertiseid']
    def __unicode__(self):
        return '%d:%s' % (self.doctorexpertiseid, self.doctorexpertisetitle)

class TbTcmdcotorsinfo(models.Model):
    """
    中医专家信息表
    """
    doctorid = models.AutoField(primary_key=True)
    doctorname = models.CharField(max_length=20, blank=True)
    doctorsex = models.CharField(max_length=5, blank=True)
    doctorage = models.IntegerField(blank=True, null=True)
    professionalrands = models.CharField(max_length=100, blank=True)
    doctorworktime = models.IntegerField(blank=True, null=True)
    doctorsynopsis = models.CharField(max_length=1024, blank=True)
    researcharea = models.CharField(max_length=1024, blank=True)
    researchfindings = models.CharField(max_length=1024, blank=True)
    #temp_adminisareaid = models.IntegerField(blank=True, null=True)
    temp_adminisareaid = models.ForeignKey(TbAdminisarea, related_name='tcmdcotorsinfo', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_doctorexpertiseid = models.IntegerField(blank=True, null=True)
    temp_doctorexpertiseid = models.ForeignKey(TbDoctorexpertiseinfo, related_name='tcmdcotorsinfo', blank=True, null=True, on_delete=models.SET_NULL)
    doctorcode = models.BigIntegerField(blank=True, null=True)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='tbtcmdcotorsinfo', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_tcmdcotorsinfo'
        ordering = ['-doctorid']
    def __unicode__(self):
        return '%d:%s' % (self.doctorid, self.doctorname)

class TbMedicineinfo(models.Model):
    """
    中药信息表
    """
    chinesemedicineid = models.AutoField(primary_key=True)
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
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='tbmedicineinfo', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_medicineinfo'
        ordering = ['chinesemedicineid']
    def __unicode__(self):
        return '%d:%s' % (self.chinesemedicineid, self.medicinename)




class TbMedicineprescription(models.Model):
    """
    中药方剂表
    """
    medicineprescriptionid = models.AutoField(primary_key=True)
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
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='tbmedicineprescription', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_medicineprescription'
        ordering = ['medicineprescriptionid']
    def __unicode__(self):
        return '%d:%s' % (self.medicineprescriptionid, self.medicineprescriptionname)



class TbMedicineprescriptionmapp(models.Model):
    """
    药品方剂映射表
    """
    medprescriptmappid = models.AutoField(primary_key=True)
    temp_chinesemedicineid = models.ForeignKey(TbMedicineinfo, related_name='medicineprescriptionmapp', blank=True, null=True, on_delete=models.SET_NULL)
    temp_medicineprescriptionid = models.ForeignKey(TbMedicineprescription, related_name='medicineprescriptionmapp', blank=True, null=True, on_delete=models.SET_NULL)
    medicineamount = models.CharField(max_length=30, blank=True)
    medprescriptmappremarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_medicineprescriptionmapp'
        ordering = ['medprescriptmappid']
    def __unicode__(self):
        return '%d:%s' % (self.medprescriptmappid, self.medicineamount)




class TbCtreatmentrecords(models.Model):
    """
    记录用户中医诊疗信息
    """
    tcmexaminationid = models.AutoField(primary_key=True)
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
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='ctreatmentrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_doctorid = models.IntegerField(blank=True, null=True)
    temp_doctorid = models.ForeignKey(TbTcmdcotorsinfo, related_name='ctreatmentrecords', blank=True, null=True, on_delete=models.SET_NULL)
    examinationtime = models.DateTimeField(blank=True, null=True)
    examinationlocation = models.CharField(max_length=100, blank=True)
    examinationresult = models.CharField(max_length=1024, blank=True)
    examinationremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_ctreatmentrecords'
        ordering = ['tcmexaminationid']

class TbMedicineuseinfo(models.Model):
    """
    记录用户诊疗过程中的用药信息
    """
    medicineuseinfoid = models.AutoField(primary_key=True)
    medicineusetype = models.CharField(max_length=100, blank=True)
    medicineusename = models.CharField(max_length=50, blank=True)
    medicineusedose = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    medicineuseremarks = models.CharField(max_length=1024, blank=True)
    #temp_tcmexaminationid = models.BigIntegerField(blank=True, null=True)
    temp_tcmexaminationid = models.ForeignKey(TbCtreatmentrecords, related_name='tcmexamination', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_unitattributeid = models.IntegerField(blank=True, null=True)
    temp_unitattributeid = models.ForeignKey(TbMeasurementunit, related_name='medicineuseinfo', blank=True, null=True, on_delete=models.SET_NULL)
    prescriptiontag = models.CharField(max_length=50, blank=True)
    #temp_chinesemedicineid = models.IntegerField(blank=True, null=True)
    temp_chinesemedicineid = models.ForeignKey(TbMedicineinfo, related_name='medicineuseinfo', blank=True, null=True, on_delete=models.SET_NULL)
    temp_medicineprescriptionid = models.ForeignKey(TbMedicineprescription, related_name='medicineuseinfo', blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        managed = False
        db_table = 'tb_medicineuseinfo'
        ordering = ['medicineuseinfoid']
    def __unicode__(self):
        return '%d:%s' % (self.medicineuseinfoid, self.medicineusename)
















class TbDataacquiretype(models.Model):
    """
    采集数据分类表
    """
    acqdatatypeid = models.AutoField(primary_key=True)
    acqdatatypename = models.CharField(max_length=50, blank=True)
    acqdatatypeexplain = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_dataacquiretype'
        ordering = ['acqdatatypeid']
    def __unicode__(self):
        return '%d:%s' % (self.acqdatatypeid, self.acqdatatypename)

class TbDataacquisition(models.Model):
    """
    设备数据采集代码表
    """
    acquiredataid = models.AutoField(primary_key=True)
    acquiredataname = models.CharField(max_length=20, blank=True)
    acquiredataexplain = models.CharField(max_length=200, blank=True)
    #temp_acqdatatypeid = models.IntegerField(blank=True, null=True)
    temp_acqdatatypeid = models.ForeignKey(TbDataacquiretype, related_name='dataacquisition', blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        managed = False
        db_table = 'tb_dataacquisition'
        ordering = ['acquiredataid']
    def __unicode__(self):
        return '%d:%s' % (self.acquiredataid, self.acquiredataname)




class TbIntelligentdeviceinfo(models.Model):
    """
    智能设备基本信息表
    """
    intelligentdeviceid = models.AutoField(primary_key=True)
    intelligentdevicetype = models.CharField(max_length=50, blank=True)
    intelligentdevicename = models.CharField(max_length=50, blank=True)
    intelligentdeviceweight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    intelligentdevicecolor = models.CharField(max_length=10, blank=True)
    intelligentdevicefunction = models.CharField(max_length=200, blank=True)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='deviceacquiredatarecords', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_intelligentdeviceinfo'
        ordering = ['intelligentdeviceid']
    def __unicode__(self):
        return '%d:%s' % (self.intelligentdeviceid, self.intelligentdevicename)
class TbDeviceacquiredatarecords(models.Model):
    """
    智能设备采集数据记录表
    """
    deviceacqrecordid = models.AutoField(primary_key=True)
    #temp_intelligentdeviceid = models.IntegerField(blank=True, null=True)
    temp_intelligentdeviceid = models.ForeignKey(TbIntelligentdeviceinfo, related_name='deviceacquiredatarecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_acquiredataid = models.IntegerField(blank=True, null=True)
    temp_acquiredataid = models.ForeignKey(TbDataacquisition, related_name='deviceacquiredatarecords', blank=True, null=True, on_delete=models.SET_NULL)
    deviceacqdatavalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    #temp_unitattributeid = models.IntegerField(blank=True, null=True)
    temp_unitattributeid = models.ForeignKey(TbMeasurementunit, related_name='deviceacquiredatarecords', blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        managed = False
        db_table = 'tb_deviceacquiredatarecords'
        ordering = ['deviceacqrecordid']







class TbDeviceparacode(models.Model):
    """
    设备参数代码表
    """
    deviceparacodeid = models.AutoField(primary_key=True)
    parametercode = models.IntegerField(blank=True, null=True)
    parametername = models.CharField(max_length=30, blank=True)
    parametermean = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_deviceparacode'
        ordering = ['deviceparacodeid']
    def __unicode__(self):
        return '%d:%s' % (self.deviceparacodeid, self.parametername)

class TbDeviceparamapp(models.Model):
    """
    针对不同设备有不同参数
    """
    deviceparamappid = models.AutoField(primary_key=True)
    #temp_intelligentdeviceid = models.IntegerField(blank=True, null=True)
    temp_intelligentdeviceid = models.ForeignKey(
        TbIntelligentdeviceinfo, related_name='deviceparamapp', blank=True, null=True, on_delete=models.SET_NULL
    )
    #temp_deviceparacodeid = models.IntegerField(blank=True, null=True)
    temp_deviceparacodeid = models.ForeignKey(TbDeviceparacode, related_name='deviceparamapp', blank=True, null=True, on_delete=models.SET_NULL)
    deviceparavalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_deviceparamapp'
        ordering = ['deviceparamappid']







class TbTcmdiagnosistype(models.Model):
    """
    中医诊断分类表
    """
    diagnosistypeid = models.AutoField(primary_key=True)
    diagnosistypename = models.CharField(max_length=50, blank=True)
    diagnosistypecode = models.IntegerField(blank=True, null=True)
    diagnosistypeexplain = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_tcmdiagnosistype'
        ordering = ['diagnosistypeid']
    def __unicode__(self):
        return '%d:%s' % (self.diagnosistypecode, self.diagnosistypename)
class TbTcmdiagnosisobj(models.Model):
    """
    诊断对象表
    """
    diagnosisobjid = models.AutoField(primary_key=True)
    diagnosisobjname = models.CharField(max_length=50, blank=True)
    diagnosisobjexplain = models.CharField(max_length=1024, blank=True)
    #temp_diagnosistypeid = models.IntegerField(blank=True, null=True)
    temp_diagnosistypeid = models.ForeignKey(TbTcmdiagnosistype, related_name='tcmdiagnosisobj', blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        managed = False
        db_table = 'tb_tcmdiagnosisobj'
        ordering = ['diagnosisobjid']
    def __unicode__(self):
        return '%d:%s' % (self.diagnosisobjid, self.diagnosisobjname)

class TbLocationinfo(models.Model):
    """
    地理位置相关信息
    """
    locationinfoid = models.AutoField(primary_key=True)
    locationlongitude = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    locationlatitude = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    reallocation = models.CharField(max_length=200, blank=True)
    locationremarks = models.CharField(max_length=200, blank=True)
    locationprovince = models.CharField(max_length=50, blank=True)
    locationcity = models.CharField(max_length=50, blank=True)
    locationclassify = models.CharField(max_length=50, blank=True)
    locationcounty = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_locationinfo'
        ordering = ['locationinfoid']
    def __unicode__(self):
        return '%d:%s' % (self.locationinfoid, self.reallocation)
class TbDiagnosistrendsrecords(models.Model):
    """
    诊断动态记录表
    """
    diatrendid = models.AutoField(primary_key=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='diagnosistrendsrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_diagnosisobjid = models.IntegerField(blank=True, null=True)
    temp_diagnosisobjid = models.ForeignKey(TbTcmdiagnosisobj, related_name='diagnosistrendsrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_doctorid = models.IntegerField(blank=True, null=True)
    temp_doctorid = models.ForeignKey(TbTcmdcotorsinfo, related_name='diagnosistrendsrecords', blank=True, null=True, on_delete=models.SET_NULL)
    diatrendres = models.CharField(max_length=100, blank=True)
    diatrendresexplain = models.CharField(max_length=200, blank=True)
    diatrendtime = models.DateField(blank=True, null=True)
    diatrendplace = models.CharField(max_length=100, blank=True)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='diagnosistrendsrecords', blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        managed = False
        db_table = 'tb_diagnosistrendsrecords'
        ordering = ['diatrendid']












class TbDietaryrecords(models.Model):
    """
    饮食信息记录表
    """
    eatingrecordid = models.AutoField(primary_key=True)
    foodtypename = models.CharField(max_length=50, blank=True)
    foodname = models.CharField(max_length=50, blank=True)
    eatingamount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    unitname = models.CharField(max_length=20, blank=True)
    eatingtime = models.DateTimeField(blank=True, null=True)
    eatingrecordsuptime = models.DateTimeField(blank=True, null=True)
    eatinginforemarks = models.CharField(max_length=150, blank=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='dietaryrecords', blank=True, null=True, on_delete=models.SET_NULL)
    eatingstateback = models.CharField(max_length=200, blank=True)
    #temp_foodnutritionid = models.IntegerField(blank=True, null=True)
    temp_foodnutritionid = models.ForeignKey(TbFoodnutritioncontent, related_name='dietaryrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='dietaryrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_intelligentdeviceid = models.IntegerField(blank=True, null=True)
    temp_intelligentdeviceid = models.ForeignKey(TbIntelligentdeviceinfo, related_name='dietaryrecords', blank=True, null=True, on_delete=models.SET_NULL)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    eatingupflag = models.BigIntegerField(blank=True, null=True)
    setmealcode = models.BigIntegerField(blank=True, null=True)
    eatingovertime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_dietaryrecords'
        ordering = ['eatingrecordid']
    def __unicode__(self):
        return '%d:%s' % (self.eatingrecordid, self.foodname)



class TbEatinganalysis(models.Model):
    """
    饮食状况分析表
    """
    eatinganalysisid = models.AutoField(primary_key=True)
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
    #temp_eatingrecordid = models.BigIntegerField(blank=True, null=True)
    temp_eatingrecordid = models.ForeignKey(TbDietaryrecords, related_name='eatingrecord', blank=True, null=True)
    caroteneintake = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    caroteneunit = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_eatinganalysis'
        ordering = ['eatinganalysisid']
    def __unicode__(self):
        return '%d' % (self.eatinganalysisid)















class TbEatingpreferrecords(models.Model):
    """
    饮食偏好记录表
    """
    eatingpreferid = models.AutoField(primary_key=True)
    foodtypename = models.CharField(max_length=50, blank=True)
    foodname = models.CharField(max_length=50, blank=True)
    preference = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    averageintake = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    #temp_foodnutritionid = models.IntegerField(blank=True, null=True)
    temp_foodnutritionid = models.ForeignKey(TbFoodnutritioncontent, related_name='eatingpreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='eatingpreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    eatingoftenstarttime = models.TimeField(blank=True, null=True)
    eatingoftenovertime = models.TimeField(blank=True, null=True)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='eatingpreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    additemtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_eatingpreferrecords'
        ordering = ['eatingpreferid']
    def __unicode__(self):
        return '%d:%s' % (self.eatingpreferid, self.foodname)

class TbExercisetype(models.Model):
    """
    运动类型名
    """
    exercisetypeid = models.AutoField(primary_key=True)
    exercisetypename = models.CharField(max_length=100, blank=True)
    exercisetypeexplain = models.CharField(max_length=1024, blank=True)
    exercisetypecode = models.IntegerField(blank=True, null=True)
    exercisetyperemarks = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_exercisetype'
        ordering = ['exercisetypeid']
    def __unicode__(self):
        return '%d:%s' % (self.exercisetypeid, self.exercisetypename)


class TbExerciseinfo(models.Model):
    """
    运动实体信息表
    """
    exerciseid = models.AutoField(primary_key=True)
    exercisename = models.CharField(max_length=20, blank=True)
    exercisetypename = models.CharField(max_length=20, blank=True)
    energywaste = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    exercisetip = models.CharField(max_length=1024, blank=True)
    exerciseaffect = models.CharField(max_length=1024, blank=True)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='exercisepreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    temp_exercisetypeid = models.ForeignKey(TbExercisetype, related_name='exercisepreferrecords', blank=True, null=True, on_delete=models.SET_NULL)


    class Meta:
        managed = False
        db_table = 'tb_exerciseinfo'
        ordering = ['exerciseid']
    def __unicode__(self):
        return '%d:%s' % (self.exerciseid, self.exercisename)

class TbExercisepreferrecords(models.Model):
    """
    运动偏好记录表
    """
    exercisepreferenceid = models.AutoField(primary_key=True)
    exercisetype = models.CharField(max_length=20, blank=True)
    exercisename = models.CharField(max_length=20, blank=True)
    exercisedescribe = models.CharField(max_length=200, blank=True)
    #temp_exerciseid = models.IntegerField(blank=True, null=True)
    temp_exerciseid = models.ForeignKey(TbExerciseinfo, related_name='exercisepreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='exercisepreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='exercisepreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    additemtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_exercisepreferrecords'
        ordering = ['exercisepreferenceid']
    def __unicode__(self):
        return '%d:%s' % (self.exercisepreferenceid, self.exercisename)


class TbExpendedhealthproperties(models.Model):
    """
    扩张健康属性表
    """
    exphealthpropertyid = models.AutoField(primary_key=True)
    healthpropertyname = models.CharField(max_length=20, blank=True)
    healthpropertyexplain = models.CharField(max_length=500, blank=True)
    healthpropertycode = models.IntegerField(blank=True, null=True)
    healthpropertyremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_expendedhealthproperties'
        ordering = ['exphealthpropertyid']
    def __unicode__(self):
        return '%d:%s' % (self.exphealthpropertyid, self.healthpropertyname)




class TbFoodfeature(models.Model):
    """
    饮食特征信息表
    """
    eatingfeatureid = models.AutoField(primary_key=True)
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
    temp_amountstdid = models.ForeignKey(TbAverageamountstd, related_name='foodfeature', blank=True, null=True, on_delete=models.SET_NULL)
    latelymaintentime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_foodfeature'
        ordering = ['eatingfeatureid']








class TbHealthknowledgetype(models.Model):
    """
    养生知识类别表
    """
    healthknowltypeid = models.AutoField(primary_key=True)
    healthknowltypename = models.CharField(max_length=50, blank=True)
    healthknowltypecode = models.IntegerField(blank=True, null=True)
    healthknowltypeexp = models.CharField(max_length=200, blank=True)
    healthknowltyperemarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthknowledgetype'
        ordering = ['healthknowltypeid']
    def __unicode__(self):
        return '%d:%s' % (self.healthknowltypeid, self.healthknowltypename)




class TbTcmhealthknowledge(models.Model):
    """
    记录中医养生知识发布细节
    """
    healthknowledgeid = models.AutoField(primary_key=True)
    healthknowledgetitle = models.CharField(max_length=200, blank=True)
    healthknowledgecontent = models.CharField(max_length=1024, blank=True)
    exersuggtime = models.DateTimeField(blank=True, null=True)
    #temp_managerid = models.IntegerField(blank=True, null=True)
    temp_managerid = models.ForeignKey(TbManager, related_name='tcmhealthknowledge', blank=True, null=True, on_delete=models.SET_NULL)
    healthknowledgeremarks = models.CharField(max_length=1024, blank=True)
    #temp_healthknowltypeid = models.IntegerField(blank=True, null=True)
    temp_healthknowltypeid = models.ForeignKey(TbHealthknowledgetype, related_name='tcmhealthknowledge', blank=True, null=True, on_delete=models.SET_NULL)
    healthknowledgecode = models.BigIntegerField(blank=True, null=True)
    healthknowledgeflag = models.IntegerField(blank=True, null=True)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='healthknowledge', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_tcmhealthknowledge'
        ordering = ['healthknowledgeid']
    def __unicode__(self):
        return "%d:%s" % (self.healthknowledgeid, self.healthknowledgetitle)



class TbUserknowledgemapp(models.Model):
    """
    用户养生知识映射表
    """
    userknowledgemappid = models.AutoField(primary_key=True)
    temp_userid = models.ForeignKey(TbUser, related_name='userknowledgemapp', blank=True, null=True, on_delete=models.SET_NULL)
    healthknowledgecontent = models.CharField(max_length=1024, blank=True)
    temp_healthknowledgeid = models.ForeignKey(TbTcmhealthknowledge, related_name='userknowledgemapp', blank=True, null=True, on_delete=models.SET_NULL)
    healthknowledgereason = models.CharField(max_length=500, blank=True)
    healthknowledgetime = models.DateTimeField(blank=True, null=True)
    healthknowledgeremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_userknowledgemapp'
        ordering = ['userknowledgemappid']



class TbHealthknowledgelimited(models.Model):
    """
    养生知识限定条件表
    """
    healthknowllimitedid = models.AutoField(primary_key=True)
    healthknowllimitedattname = models.CharField(max_length=50, blank=True)
    healthknowllimitedstatus = models.SmallIntegerField(blank=True, null=True)
    healthknowllimitedstatuslevel = models.SmallIntegerField(blank=True, null=True)
    temp_healthknowledgeid = models.ForeignKey(TbTcmhealthknowledge, related_name='healthknowledgelimited', blank=True, null=True, on_delete=models.SET_NULL)
    healthknowllimitedexp = models.CharField(max_length=200, blank=True)
    healthknowllimitedremarks = models.CharField(max_length=200, blank=True)
    healthknowllimitedvalue = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthknowledgelimited'
        ordering = ['healthknowllimitedid']
    def __unicode__(self):
        return '%d:%s' % (self.healthknowllimitedid, self.healthknowllimitedattname)



class TbHealthtrendrecords(models.Model):
    """
    记录用户健康趋势
    """
    healthtrendid = models.AutoField(primary_key=True)
    heaanalysistitle = models.CharField(max_length=200, blank=True)
    healthanalysistime = models.DateTimeField(blank=True, null=True)
    healthtrendanalysiresult = models.CharField(max_length=1024, blank=True)
    #temp_personalizedhealthid = models.BigIntegerField(blank=True, null=True)
    temp_healthknowledgeid = models.ForeignKey(TbTcmhealthknowledge, related_name='healthtrendrecords', blank=True, null=True, on_delete=models.SET_NULL)
    healthtrendanalysisremarks = models.CharField(max_length=1024, blank=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='healthtrendrecords', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_healthtrendrecords'
        ordering = ['healthtrendid']
    def __unicode__(self):
        return '%d:%s' % (self.healthtrendid, self.heaanalysistitle)

class TbHealthindicatorinfo(models.Model):
    """
    健康指标信息表
    """
    healthindicatorid = models.AutoField(primary_key=True)
    healthindicatorname = models.CharField(max_length=50, blank=True)
    healthindicatorvalue = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    healthindicatorchange = models.CharField(max_length=100, blank=True)
    indicatorchangeexplain = models.CharField(max_length=200, blank=True)
    #temp_healthtrendid = models.BigIntegerField(blank=True, null=True)
    temp_healthtrendid = models.ForeignKey(TbHealthtrendrecords, related_name='healthindicatorinfo', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_healthindicatorinfo'
        ordering = ['healthindicatorid']








class TbHealthsuggtype(models.Model):
    """
    健康建议类别表
    """
    healthsuggtypeid = models.AutoField(primary_key=True)
    healthsuggtypename = models.CharField(max_length=50, blank=True)
    healthsuggtypecode = models.IntegerField(blank=True, null=True)
    suggclassifyexpla = models.CharField(max_length=200, blank=True)
    healthsuggtyperemarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggtype'
        ordering = ['healthsuggtypeid']
    def __unicode__(self):
        return '%d:%s' % (self.healthsuggtypeid, self.healthsuggtypename)


class TbHealthsuggestions(models.Model):
    """
    健康建议表
    """
    healthsuggestid = models.AutoField(primary_key=True)
    healthsuggestcontent = models.CharField(max_length=1024, blank=True)
    healthsuggesttitle = models.CharField(max_length=100, blank=True)
    healthsuggestremarks = models.CharField(max_length=1024, blank=True)
    #temp_healthsuggtypeid = models.IntegerField(blank=True, null=True)
    temp_healthsuggtypeid = models.ForeignKey(TbHealthsuggtype, related_name='healthsuggestions', blank=True, null=True, on_delete=models.SET_NULL)
    healthsuggestflag = models.IntegerField(blank=True, null=True)
    healthsuggestcode = models.BigIntegerField(blank=True, null=True)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='healthsuggestions', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggestions'
        ordering = ['healthsuggestid']
    def __unicode__(self):
        return '%d:%s' % (self.healthsuggestid, self.healthsuggesttitle)



class TbHealthsuggestionsmapp(models.Model):
    """
    用户健康建议映射表
    """
    healthsuggestmappid = models.AutoField(primary_key=True)
    healthsuggcontent = models.CharField(max_length=1024, blank=True)
    temp_userid = models.ForeignKey(TbUser, related_name='healthsuggestionsmapp', blank=True, null=True, on_delete=models.SET_NULL)
    temp_healthsuggestid = models.ForeignKey(TbHealthsuggestions, related_name='healthsuggestionsmapp', blank=True, null=True, on_delete=models.SET_NULL)
    healthsuggestreason = models.CharField(max_length=500, blank=True)
    healthsuggesttime = models.DateTimeField(blank=True, null=True)
    healthsuggestremarks = models.CharField(max_length=500, blank=True)
    checktosee = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggestionsmapp'
        ordering = ['-healthsuggesttime']



class TbHealthsuggestlimited(models.Model):
    """
    健康建议限定条件表
    """
    healthsuggestlimitedid = models.AutoField(primary_key=True)
    suggestlimitedattrname = models.CharField(max_length=50, blank=True)
    suggestlimitedstatus = models.SmallIntegerField(blank=True, null=True)
    suggestlimitedstatuslevel = models.SmallIntegerField(blank=True, null=True)
    suggestlimitedexplain = models.CharField(max_length=200, blank=True)
    suggestlimitedremarks = models.CharField(max_length=200, blank=True)
    suggestlimitedvalue = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthsuggestlimited'
        ordering = ['healthsuggestlimitedid']
    def __unicode__(self):
        return '%d:%s' % (self.healthsuggestlimitedid, self.suggestlimitedvalue)



class TbUserhealthattrmapp(models.Model):
    """
    用户健康属性映射表
    """
    userhealthattrmappid = models.AutoField(primary_key=True)
    temp_userid = models.ForeignKey(TbUser, related_name='userhealthattrmapp', blank=True, null=True, on_delete=models.SET_NULL)
    temp_exphealthpropertyid = models.ForeignKey(TbExpendedhealthproperties, related_name='userhealthattrmapp', blank=True, null=True, on_delete=models.SET_NULL)
    expendhealthattrvalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    temp_unitattributeid = models.ForeignKey(TbMeasurementunit, related_name='userhealthattrmapp', blank=True, null=True, on_delete=models.SET_NULL)
    updatetime = models.DateTimeField(blank=True, null=True)
    currentuseflag = models.SmallIntegerField(blank=True, null=True)
    userattrmappingexplain = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_userhealthattrmapp'
        ordering = ['userhealthattrmappid']




class TbHealthwarningtype(models.Model):
    """
    健康预警类别表
    """
    healthwarningtypeid = models.AutoField(primary_key=True)
    healthwarningname = models.CharField(max_length=100, blank=True)
    healthwarningtypecode = models.IntegerField(blank=True, null=True)
    healthwarningtypeexp = models.CharField(max_length=200, blank=True)
    healthwarningtyperemarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthwarningtype'
        ordering = ['healthwarningtypeid']
    def __unicode__(self):
        return '%d:%s' % (self.healthwarningtypeid, self.healthwarningname)


class TbHealthwarningmess(models.Model):
    """
    健康预警信息表
    """
    healthwarningmessid = models.AutoField(primary_key=True)
    healthwarningtitle = models.CharField(max_length=100, blank=True)
    healthwarningcontent = models.CharField(max_length=1024, blank=True)
    healthwarningremarks = models.CharField(max_length=200, blank=True)
    temp_healthsuggestid = models.ForeignKey(TbHealthsuggestions, related_name='healthwarningmess', blank=True, null=True, on_delete=models.SET_NULL)
    temp_healthwarningtypeid = models.ForeignKey(TbHealthwarningtype, related_name='healthwarningmess', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_healthwarningmess'
        ordering = ['healthwarningmessid']
    def __unicode__(self):
        return '%d:%s' % (self.healthwarningmessid, self.healthwarningtitle)




class TbUserhealthwarningmapp(models.Model):
    """
    用户预警映射表
    """
    userhealthwarningid = models.AutoField(primary_key=True)
    healthwarningcontent = models.CharField(max_length=1024, blank=True)
    healthwarningtime = models.DateTimeField(blank=True, null=True)
    healthwarningreason = models.CharField(max_length=500, blank=True)
    temp_userid = models.ForeignKey(TbUser, related_name='userhealthwarningmapp', blank=True, null=True, on_delete=models.SET_NULL)
    healthwarningremarks = models.CharField(max_length=500, blank=True)
    temp_healthwarningmessid = models.ForeignKey(TbHealthwarningmess, related_name='userhealthwarningmapp', blank=True, null=True, on_delete=models.SET_NULL)
    checktosee = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_userhealthwarningmapp'
        ordering = ['-healthwarningtime']












class TbHospitalinfo(models.Model):
    """
    医院信息表
    """
    hospitalid = models.AutoField(primary_key=True)
    hospitalname = models.CharField(max_length=100, blank=True)
    hospitalexplain = models.CharField(max_length=1024, blank=True)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='hospitalinfo', blank=True, null=True, on_delete=models.SET_NULL)
    hospitalrank = models.CharField(max_length=100, blank=True)
    #temp_adminisareaid = models.IntegerField(blank=True, null=True)
    temp_adminisareaid = models.ForeignKey(TbAdminisarea, related_name='hospitalinfo', blank=True, null=True, on_delete=models.SET_NULL)
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='hospitalinfo', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_hospitalinfo'
        ordering = ['hospitalid']
    def __unicode__(self):
        return '%d:%s' % (self.hospitalid, self.hospitalname)

class TbHospitalofficesinfo(models.Model):
    """
    医院科室信息表
    """
    hospitalofficeid = models.AutoField(primary_key=True)
    hospitalofficename = models.CharField(max_length=50, blank=True)
    hospitalofficeexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_hospitalofficesinfo'
        ordering = ['hospitalofficeid']
    def __unicode__(self):
        return '%d:%s' % (self.hospitalofficeid, self.hospitalofficename)

class TbHospitaldoctorrel(models.Model):
    """
    医院医生关系表
    """
    hospitaldocrelid = models.AutoField(primary_key=True)
    #temp_hospitalid = models.IntegerField(blank=True, null=True)
    temp_hospitalid = models.ForeignKey(TbHospitalinfo, related_name='hospitaldoctorrel', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_doctorid = models.IntegerField(blank=True, null=True)
    temp_doctorid = models.ForeignKey(TbTcmdcotorsinfo, related_name='hospitaldoctorrel', unique=True, blank=True, null=True, on_delete=models.SET_NULL)
    #temp_hospitalofficeid = models.IntegerField(blank=True, null=True)
    temp_hospitalofficeid = models.ForeignKey(TbHospitalofficesinfo, related_name='hospitaldoctorrel', blank=True, null=True, on_delete=models.SET_NULL)
    workduty = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_hospitaldoctorrel'
        ordering = ['hospitaldocrelid']
        unique_together = ("temp_hospitalid", "temp_doctorid")











class TbIdentificationissuess(models.Model):
    """
    体质辨识问卷项目表
    """
    identifyissueid = models.AutoField(primary_key=True)
    #temp_physiqueinfoid = models.IntegerField(blank=True, null=True)
    temp_physiqueinfoid = models.ForeignKey(TbPhysiqueinfo, related_name='identificationissuess', blank=True, null=True, on_delete=models.SET_NULL)
    identifyissuecontent = models.CharField(max_length=200, blank=True)
    identifyissueremarks = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_identificationissuess'
        ordering = ['identifyissueid']
    def __unicode__(self):
        return '%d:%s' % (self.temp_physiqueinfoid, self.identifyissuecontent)






class TbIdentifychoices(models.Model):
    """
    体质辨识选项表
    """
    identifychoiceid = models.AutoField(primary_key=True)
    identifychoicevalue = models.IntegerField(blank=True, null=True)
    scriptdescribe = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_identifychoices'
        ordering = ['identifychoiceid']
    def __unicode__(self):
        return '%d' % (self.identifychoicevalue)



class TbIdentifydiseaserel(models.Model):
    """
    记录体质和疾病的关系
    """
    identifydirelid = models.AutoField(primary_key=True)
    #temp_physiqueinfoid = models.IntegerField(blank=True, null=True)
    temp_physiqueinfoid = models.ForeignKey(TbPhysiqueinfo, related_name='identifydiseaserel', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_commondiseaseid = models.IntegerField(blank=True, null=True)
    temp_commondiseaseid = models.ForeignKey(TbCommondiseaseinfo, related_name='identifydiseaserel', blank=True, null=True, on_delete=models.SET_NULL)
    identifydirelexplain = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_identifydiseaserel'
        ordering = ['identifydirelid']














class TbMedicalhistoryrecords(models.Model):
    """
    记录用户病史
    """
    medicalhistoryrecordid = models.AutoField(primary_key=True)
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
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='medicalhistoryrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_doctorid = models.IntegerField(blank=True, null=True)
    temp_doctorid = models.ForeignKey(TbTcmdcotorsinfo, related_name='medicalhistoryrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_medicineuseinfoid = models.BigIntegerField(blank=True, null=True)
    temp_medicineuseinfoid = models.ForeignKey(TbMedicineuseinfo, related_name='medicalhistoryrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_commondiseaseid = models.IntegerField(blank=True, null=True)
    temp_commondiseaseid = models.ForeignKey(TbCommondiseaseinfo, related_name='commondisease', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_medicalhistoryrecords'
        ordering = ['medicalhistoryrecordid']











class TbPhoneappinfo(models.Model):
    """
    手机应用实体部分信息
    """
    appinfoid = models.AutoField(primary_key=True)
    apptype = models.CharField(max_length=20, blank=True)
    appname = models.CharField(max_length=30, blank=True)
    apptag = models.CharField(max_length=50, blank=True)
    appotherinfo = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_phoneappinfo'
        ordering = ['appinfoid']


class TbPhoneinfo(models.Model):
    """
    手机监控特征信息表
    """
    phoneinfoid = models.AutoField(primary_key=True)
    phoneuniqunum = models.CharField(max_length=100, blank=True)
    phonenum = models.CharField(max_length=30, blank=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='phoneinfo', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_phoneinfo'
        ordering = ['phoneinfoid']
    def __unicode__(self):
        return '%s' % (self.phonenum)



class TbPhonemonitorrecords(models.Model):
    """
    手机监控记录表
    """
    phoneappmonitorrecordid = models.AutoField(primary_key=True)
    #temp_appinfoid = models.IntegerField(blank=True, null=True)
    temp_appinfoid = models.ForeignKey(TbPhoneappinfo, related_name='phonemonitorrecords', blank=True, null=True, on_delete=models.SET_NULL)
    appopentime = models.DateTimeField(blank=True, null=True)
    appclosetime = models.DateTimeField(blank=True, null=True)
    appusetime = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='phonemonitorrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_phoneinfoid = models.IntegerField(blank=True, null=True)
    temp_phoneinfoid = models.ForeignKey(TbPhoneinfo, related_name='phonemonitorrecords', blank=True, null=True, on_delete=models.SET_NULL)
    recordproducttime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_phonemonitorrecords'
        ordering = ['phoneappmonitorrecordid']


class TbPhonepreferuserecords(models.Model):
    """
    手机使用偏好记录
    """
    phonepreferuseid = models.AutoField(primary_key=True)
    oftenusebeginat = models.TimeField(blank=True, null=True)
    oftenuseovertime = models.TimeField(blank=True, null=True)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='phonepreferuserecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_appinfoid = models.IntegerField(blank=True, null=True)
    temp_appinfoid = models.ForeignKey(TbPhoneappinfo, related_name='phonepreferuserecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='phonepreferuserecords', blank=True, null=True, on_delete=models.SET_NULL)
    temp_amountstdid = models.ForeignKey(TbAverageamountstd, related_name='phonepreferuserecords', blank=True, null=True, on_delete=models.SET_NULL)
    additemtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_phonepreferuserecords'
        ordering = ['phonepreferuseid']



class TbRecommendedconditionsmapp(models.Model):
    """
    健康建议条件限定映射表
    """
    recommendedconditionsmappid = models.AutoField(primary_key=True)
    temp_healthsuggestlimitedid = models.ForeignKey(TbHealthsuggestlimited, related_name='tbrecommendedconditionsmapp', blank=True, null=True, on_delete=models.SET_NULL)
    temp_healthsuggestid = models.ForeignKey(TbHealthsuggestions, related_name='tbrecommendedconditionsmapp', blank=True, null=True, on_delete=models.SET_NULL)
    recommendmappremarks = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_recommendedconditionsmapp'
        ordering = ['recommendedconditionsmappid']



class TbSleepinforecords(models.Model):
    """
    记录用户睡眠信息
    """
    sleeprecordid = models.AutoField(primary_key=True)
    airhumidity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ambienttemperature = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ambientnoise = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    sleepbegin = models.DateTimeField(blank=True, null=True)
    sleepover = models.DateTimeField(blank=True, null=True)
    deepsleeptime = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    shallowsleeptime = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sleepremarks = models.CharField(max_length=150, blank=True)
    sleeprecorduptime = models.DateTimeField(blank=True, null=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='sleepinforecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='sleepinforecords', blank=True, null=True, on_delete=models.SET_NULL)
    waketimes = models.IntegerField(blank=True, null=True)
    #temp_intelligentdeviceid = models.IntegerField(blank=True, null=True)
    temp_intelligentdeviceid = models.ForeignKey(TbIntelligentdeviceinfo, related_name='sleepinforecords', blank=True, null=True, on_delete=models.SET_NULL)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    sleepuploadflag = models.BigIntegerField(blank=True, null=True)
    awaketime = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_sleepinforecords'
        ordering = ['sleeprecordid']
    def __unicode__(self):
        return '%d' % (self.sleeprecordid)




class TbSleepstatuscategory(models.Model):
    """
    睡眠状态类别表
    """
    sleepstatuscategoryid = models.AutoField(primary_key=True)
    sleepstatusname = models.CharField(max_length=20, blank=True)
    sleepstatuscode = models.SmallIntegerField(blank=True, null=True)
    sleepstatusexplain = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_sleepstatuscategory'
        ordering = ['sleepstatuscategoryid']
    def __unicode__(self):
        return "%d:%s" % (self.sleepstatuscategoryid, self.sleepstatusname)




class TbSleepdetailprocessrecords(models.Model):
    """
    睡眠详细过程记录表
    """
    sleepdetailrecordsid = models.AutoField(primary_key=True)
    temp_sleeprecordid = models.ForeignKey(TbSleepinforecords, related_name='sleepdetailprocessrecords', blank=True, null=True)
    temp_sleepstatuscategoryid = models.ForeignKey(TbSleepstatuscategory, related_name='sleepdetailprocessrecords', blank=True, null=True, on_delete=models.SET_NULL)
    sleepstatusbegintime = models.DateTimeField(blank=True, null=True)
    sleepstatusovertime = models.DateTimeField(blank=True, null=True)
    sleepstatusduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    sleepstatusremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_sleepdetailprocessrecords'
        ordering = ['sleepdetailrecordsid']
    def __unicode__(self):
        return "%d" % (self.sleepdetailrecordsid)





class TbSleeppreferrecords(models.Model):
    """
    记录用户睡眠偏好，如：睡眠时间，可向用户推送相关信息
    """
    sleeppreferid = models.AutoField(primary_key=True)
    prefersleepbeginat = models.TimeField(blank=True, null=True)
    prefersleepoverat = models.TimeField(blank=True, null=True)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='sleeppreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='sleeppreferrecords', blank=True, null=True, on_delete=models.SET_NULL)
    sleepfeatureaddtime = models.DateTimeField(blank=True, null=True)
    currentlypreferflag = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_sleeppreferrecords'
        ordering = ['sleeppreferid']






class TbSportinforecords(models.Model):
    """
    记录用户运动数据
    """
    sportrecordid = models.AutoField(primary_key=True)
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
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='sportinforecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='sportinforecords', blank=True, null=True, on_delete=models.SET_NULL)
    sport_mode = models.CharField(max_length=100, blank=True)
    #temp_intelligentdeviceid = models.IntegerField(blank=True, null=True)
    temp_intelligentdeviceid = models.ForeignKey(TbIntelligentdeviceinfo, related_name='sportinforecords', blank=True, null=True, on_delete=models.SET_NULL)
    intelligentdevicecode = models.IntegerField(blank=True, null=True)
    uploadflag = models.BigIntegerField(blank=True, null=True)
    restingcalorieconsume = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    movecalorieconsume = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    crawledfloor = models.IntegerField(blank=True, null=True)
    fallitems = models.SmallIntegerField(blank=True, null=True)
    activeduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    longestactiveduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    longestidleduration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    temp_exerciseid = models.ForeignKey(TbExerciseinfo, related_name='sportinforecords', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_sportinforecords'
        ordering = ['sportrecordid']





class TbSupervisorylevel(models.Model):
    """
    管理员管理权限、范围
    """
    superlevelid = models.AutoField(primary_key=True)
    #temp_managerid = models.IntegerField(blank=True, null=True)
    temp_managerid = models.ForeignKey(TbManager, related_name='supervisorylevel', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_adminisareaid = models.IntegerField(blank=True, null=True)
    temp_adminisareaid = models.ForeignKey(TbAdminisarea, related_name='supervisorylevel', blank=True, null=True, on_delete=models.SET_NULL)
    managerrank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_supervisorylevel'
        ordering = ['superlevelid']
















class TbUseranswerrecords(models.Model):
    """
    用户答题记录表
    """
    issuescoremappid = models.AutoField(primary_key=True)
    #temp_identifyissueid = models.IntegerField(blank=True, null=True)
    temp_identifyissueid = models.ForeignKey(TbIdentificationissuess, related_name='useranswerrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_identifychoiceid = models.IntegerField(blank=True, null=True)
    temp_identifychoiceid = models.ForeignKey(TbIdentifychoices, related_name='useranswerrecords', blank=True, null=True, on_delete=models.SET_NULL)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='useranswerrecords', blank=True, null=True, on_delete=models.SET_NULL)
    getscore = models.IntegerField(blank=True, null=True)
    answerflag = models.BigIntegerField(blank=True, null=True)
    answertime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_useranswerrecords'
        ordering = ['issuescoremappid']


class TbUserexercisefeature(models.Model):
    """
    用户运动的特征信息，如：身高等
    """
    exercisefeatureid = models.AutoField(primary_key=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    steplength = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    runsteplength = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    standardweight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    datauptime = models.DateField(blank=True, null=True)
    exercisefeatureremarks = models.CharField(max_length=150, blank=True)
    motilityindex = models.CharField(max_length=20, blank=True)
    exercisehabitsdetermine = models.CharField(max_length=500, blank=True)
    exercisehabitanalysis = models.CharField(max_length=500, blank=True)
    averageexcitetime = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    exercisetypeprefer = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_userexercisefeature'
        ordering = ['exercisefeatureid']


class TbUsersleepfeature(models.Model):
    """
    用户睡眠特征信息（包括睡眠环境：温度、湿度、噪声情况等）
    """
    sleepfeatureid = models.AutoField(primary_key=True)
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
    #temp_locationinfoid = models.BigIntegerField(blank=True, null=True)
    temp_locationinfoid = models.ForeignKey(TbLocationinfo, related_name='usersleepfeature', blank=True, null=True, on_delete=models.SET_NULL)
    latelymaintentime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_usersleepfeature'
        ordering = ['sleepfeatureid']


class TbWesmedicineexamitem(models.Model):
    """
    西医体检项目表
    """
    westmedicineexamid = models.AutoField(primary_key=True)
    westmedicineitemname = models.CharField(max_length=50, blank=True)
    wesmedicineitemexpl = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_wesmedicineexamitem'
        ordering = ['westmedicineexamid']
    def __unicode__(self):
        return '%s' % (self.westmedicineitemname, )

class TbWtreatmentrecords(models.Model):
    """
    西医诊疗记录表
    """
    wtreatmentrecordid = models.AutoField(primary_key=True)
    #temp_westmedicineexamid = models.IntegerField(blank=True, null=True)
    temp_westmedicineexamid = models.ForeignKey(TbWesmedicineexamitem, related_name='wtreatmentrecords', blank=True, null=True, on_delete=models.SET_NULL)
    wesexamresultval = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='wtreatmentrecords', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_wtreatmentrecords'
        ordering = ['wtreatmentrecordid']


class TbMovementdetailrecords(models.Model):
    """
    运动详细过程记录表
    """
    movementdetailid = models.AutoField(primary_key=True)
    movementstarttime = models.DateTimeField(blank=True, null=True)
    movementstoptime = models.DateTimeField(blank=True, null=True)
    temp_exerciseid = models.ForeignKey(TbExerciseinfo, related_name='movementdetailrecords', blank=True, null=True, on_delete=models.SET_NULL)
    temp_sportrecordid = models.ForeignKey(TbSportinforecords, related_name='movementdetailrecords', blank=True, null=True, on_delete=models.SET_NULL)
    movementdetailremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_movementdetailrecords'
        ordering = ['movementdetailid']




class TbMycollection(models.Model):
    """
    我的收藏
    """
    mycollectionid = models.AutoField(primary_key=True)
    collectionclass = models.CharField(max_length=50, blank=True)
    collectioncode = models.BigIntegerField(blank=True, null=True)
    #temp_userid = models.BigIntegerField(blank=True, null=True)
    temp_userid = models.ForeignKey(TbUser, related_name='mycollection', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_mycollection'
        ordering = ['mycollectionid']




class TbStatisticofclick(models.Model):
    """
    点击量统计表
    """
    statisticclickid = models.AutoField(primary_key=True)
    clickclass = models.CharField(max_length=50, blank=True)
    clickitem = models.BigIntegerField(blank=True, null=True)
    praiseyn = models.SmallIntegerField(blank=True, null=True)
    statisticclickremarks = models.CharField(max_length=100, blank=True)
    temp_userid = models.ForeignKey(TbUser, related_name='statisticofclick', blank=True, null=True, on_delete=models.SET_NULL)
    ipaddress = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_statisticofclick'
        ordering = ['statisticclickid']



class TbUserreviewstat(models.Model):
    """
    用户评论统计
    """
    userreviewstatid = models.IntegerField(primary_key=True)
    userreviewclass = models.CharField(max_length=50, blank=True)
    userreviewitem = models.BigIntegerField(blank=True, null=True)
    userreviewcontent = models.CharField(max_length=1024, blank=True)
    userreviewremarks = models.CharField(max_length=500, blank=True)
    temp_userid = models.ForeignKey(TbUser, related_name='userreviewstat', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_userreviewstat'
        ordering = ['userreviewstatid']



class TbSetmealfoodmapp(models.Model):
    """
    套餐食物映射表
    """
    mealfoodmapid = models.AutoField(primary_key=True)
    temp_commonfoodid = models.ForeignKey(TbCommonfoodinfo, related_name='setmealfoodmapp', blank=True, null=True, on_delete=models.SET_NULL)
    temp_setmealinfoid = models.ForeignKey(TbEatingsetmealinfo, related_name='setmealfoodmapp', blank=True, null=True, on_delete=models.SET_NULL)
    mealfoodmapremarks = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_setmealfoodmapp'
        ordering = ['mealfoodmapid']


class TbVariousindicatorstandard(models.Model):
    """
    各类指标标准表
    """
    indicatorstandardid = models.AutoField(primary_key=True)
    indicatorname = models.CharField(max_length=50, blank=True)
    indicatorcode = models.IntegerField(blank=True, null=True)
    indicatorstatus = models.SmallIntegerField(blank=True, null=True)
    indicatorvalue = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    indicatorremarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_variousindicatorstandard'
        ordering = ['indicatorstandardid']
    def __unicode__(self):
        return '%d:%s' % (self.indicatorstandardid, self.indicatorname)


class TbVariousindicatorlimited(models.Model):
    """
    各类标准限定表
    """
    indicatorlimitedid = models.AutoField(primary_key=True)
    temp_indicatorstandardid = models.ForeignKey(TbVariousindicatorstandard, related_name='variousindicatorlimited', blank=True, null=True, on_delete=models.SET_NULL)
    indicatorstandardname = models.CharField(max_length=50, blank=True)
    indicatorstandardstatus = models.SmallIntegerField(blank=True, null=True)
    indicatorstandardcode = models.IntegerField(blank=True, null=True)
    indicatorstandardvalue = models.CharField(max_length=50, blank=True)
    indicatorstandardstatuslevel = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_variousindicatorlimited'
        ordering = ['indicatorlimitedid']
    def __unicode__(self):
        return '%d:%s' % (self.indicatorlimitedid, self.indicatorstandardname)


class TbIndicatorusermapp(models.Model):
    """
    指标用户映射表
    """
    indicatorusermappid = models.AutoField(primary_key=True)
    temp_userid = models.ForeignKey(TbUser, related_name='indicatorusermapp', blank=True, null=True, on_delete=models.SET_NULL)
    temp_indicatorstandardid = models.ForeignKey(TbVariousindicatorstandard, related_name='indicatorusermapp', blank=True, null=True, on_delete=models.SET_NULL)
    userindicatorvalue = models.CharField(max_length=50, blank=True)
    userindicatorexp = models.CharField(max_length=200, blank=True)
    userindicatorremarks = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_indicatorusermapp'
        ordering = ['indicatorusermappid']
    def __unicode__(self):
        return '%d:%s' % (self.indicatorusermappid, self.userindicatorvalue)




class Doctorview(models.Model):
    doctorid = models.IntegerField(primary_key=True)
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
    temp_picturelocationid = models.ForeignKey(TbPicturelist, related_name='doctorview', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'doctorview'
        ordering = ['doctorid']
    def __unicode__(self):
        return '%d:%s' % (self.doctorid, self.doctorname)

class Userhealthknowledge(models.Model):
    """
    个人养生知识视图
    """
    userknowledgemappid = models.IntegerField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=30, blank=True)
    healthknowltypeid = models.IntegerField(blank=True, null=True)
    healthknowltypename = models.CharField(max_length=50, blank=True)
    healthknowledgetitle = models.CharField(max_length=200, blank=True)
    healthknowledgecontent = models.CharField(max_length=1024, blank=True)
    healthknowledgetime = models.DateTimeField(blank=True, null=True)
    healthknowledgecode = models.IntegerField(blank=True, null=True)
    temp_picturelistid = models.ForeignKey(TbPicturelist, related_name='userhealthknowledge', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'userhealthknowledge'
        ordering = ['userknowledgemappid']

class TbExpertcollect(models.Model):
    """
    专家收藏表
    """
    expertcollectid = models.AutoField(primary_key=True)
    temp_userid = models.ForeignKey(TbUser, related_name='tbexpertcollect', blank=True, null=True, on_delete=models.SET_NULL)
    temp_doctorid = models.ForeignKey(TbTcmdcotorsinfo, related_name='tbexpertcollect', blank=True, null=True, on_delete=models.SET_NULL)
    collectiontime = models.DateTimeField(blank=True, null=True)
    collectionremarks = models.CharField(max_length=1024, blank=True)
    collectionstatusflag = models.SmallIntegerField(blank=True, null=True)
    collectioncontentsnapshot = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_expertcollect'
        ordering = ['expertcollectid']
class TbHealthrecommendscollection(models.Model):
    """
    养生建议收藏表
    """
    healthrecommendscolid = models.AutoField(primary_key=True)
    temp_userid = models.ForeignKey(TbUser, related_name='tbhealthrecommendscollection', blank=True, null=True, on_delete=models.SET_NULL)
    temp_healthsuggestid = models.ForeignKey(TbHealthsuggestions, related_name='tbhealthrecommendscollection', blank=True, null=True, on_delete=models.SET_NULL)
    collectiontime = models.DateTimeField(blank=True, null=True)
    collectionremarks = models.CharField(max_length=1024, blank=True)
    collectionstatusflag = models.SmallIntegerField(blank=True, null=True)
    collectioncontentsnapshot = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthrecommendscollection'
        ordering = ['healthrecommendscolid']

class TbHealthknowledgecollection(models.Model):
    """
    养生知识收藏表
    """
    healthknowledgecollid = models.AutoField(primary_key=True)
    temp_userid = models.ForeignKey(TbUser, related_name='tbhealthknowledgecollection', blank=True, null=True, on_delete=models.SET_NULL)
    temp_healthknowledgeid = models.ForeignKey(TbTcmhealthknowledge, related_name='tbhealthknowledgecollection', blank=True, null=True, on_delete=models.SET_NULL)
    collectiontime = models.DateTimeField(blank=True, null=True)
    collectionremarks = models.CharField(max_length=1024, blank=True)
    collectionstatusflag = models.SmallIntegerField(blank=True, null=True)
    collectioncontentsnapshot = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_healthknowledgecollection'
        ordering = ['healthknowledgecollid']

class TbFoodmedicinaleffecttype(models.Model):
    """
    食物药用功效类别
    """
    medicinaleffecttypeid = models.AutoField(primary_key=True)
    medicinaleffecttypename = models.CharField(max_length=100, blank=True)
    medicinaleffecttypecode = models.IntegerField(blank=True, null=True)
    medicinaleffecttypeexp = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodmedicinaleffecttype'
        ordering = ['medicinaleffecttypeid']
    def __unicode__(self):
        return '%d:%s' % (self.medicinaleffecttypeid, self.medicinaleffecttypename)

class TbFoodmedicinalprop(models.Model):
    """
    食物药用属性表
    """
    foodmedicinalpropid = models.AutoField(primary_key=True)
    medicineproperty = models.CharField(max_length=50, blank=True)
    medicineflavor = models.CharField(max_length=50, blank=True)
    medicineeffect = models.CharField(max_length=1024, blank=True)
    medicinepropremarks = models.CharField(max_length=1024, blank=True)
    temp_medicinaleffecttypeid = models.ForeignKey(TbFoodmedicinaleffecttype, related_name='tbfoodmedicinalprop', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'tb_foodmedicinalprop'
        ordering = ['foodmedicinalpropid']
    def __unicode__(self):
        return '%d:%s' % (self.foodmedicinalpropid, self.medicineproperty)

class TbFoodmedicinalpropmapp(models.Model):
    """
    食物药用属性映射表
    """
    foodmedicinalpropmappid = models.IntegerField(primary_key=True)
    temp_commonfoodid = models.ForeignKey(TbCommonfoodinfo, related_name='tbfoodmedicinalpropmapp', blank=True, null=True, on_delete=models.SET_NULL)
    temp_foodmedicinalpropid = models.ForeignKey(TbFoodmedicinalprop, related_name='tbfoodmedicinalpropmapp', blank=True, null=True, on_delete=models.SET_NULL)
    foodmedicinalpropmappexp = models.CharField(max_length=1024, blank=True)

    class Meta:
        managed = False
        db_table = 'tb_foodmedicinalpropmapp'
        ordering = ['foodmedicinalpropmappid']
