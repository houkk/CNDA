from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from CNDADATA.models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.
#class RegisterAdmin(admin.ModelAdmin):
#    list_display = ('id','name', 'gender', 'country', 'aboutYou', 'mailinglist')

class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )
    class Meta:
        model = TbUser
        fields = ('username', 'email')
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = TbUser
        fields = ('__all__')
    def clean_password(self):

        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login',)
    fieldsets = (

        (None, {'fields': ('username', 'email', 'password', 'usersex', 'userage', 'userphonenumber')}),
        ('Personal info', {'fields': ('userrank', 'userwroktype', 'userbmiindex', 'temp_sleepfeatureid',
                            'temp_exercisefeatureid', 'temp_eatingfeatureid', 'temp_adminisareaid', 'temp_picturelocationid',
                                )
                            }
        ),

        ('Permissions', {'fields': ('is_admin', 'is_active')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    filter_horizontal = ()
    add_fieldsets = (
        (

            None,
            {
                 'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            }
        ),
    )


admin.site.register(Register)#, RegisterAdmin)
admin.site.register(TbAdminisarea)
admin.site.register(TbAverageamountstd)
admin.site.register(TbCommondiseaseinfo)
admin.site.register(TbCommondiseasetype)
admin.site.register(TbCommonfoodinfo)
admin.site.register(TbCommonfoodtype)
admin.site.register(TbCommonnutrientintake)
admin.site.register(TbConstituteidentifyresult)
admin.site.register(TbCtreatmentrecords)
admin.site.register(TbDataacquiretype)
admin.site.register(TbDataacquisition)
admin.site.register(TbDeviceacquiredatarecords)
admin.site.register(TbDeviceparacode)
admin.site.register(TbDeviceparamapp)
admin.site.register(TbDiagnosistrendsrecords)
admin.site.register(TbDietaryrecords)
admin.site.register(TbDoctorexpertiseinfo)
admin.site.register(TbDoctorexpertisetype)
admin.site.register(TbEatinganalysis)
admin.site.register(TbEatingpreferrecords)
admin.site.register(TbEatingsetmealinfo)
admin.site.register(TbExercisetype)
admin.site.register(TbExerciseinfo)
admin.site.register(TbExercisepreferrecords)
admin.site.register(TbFoodfeature)
admin.site.register(TbFoodnutritioncontent)
admin.site.register(TbHealthindicatorinfo)
admin.site.register(TbHealthknowledgetype)
admin.site.register(TbHealthknowledgelimited)
admin.site.register(TbHealthsuggestions)
admin.site.register(TbHealthsuggestionsmapp)
admin.site.register(TbHealthsuggestlimited)
admin.site.register(TbHealthsuggtype)
admin.site.register(TbHealthtrendrecords)
admin.site.register(TbHealthwarningmess)
admin.site.register(TbHealthwarningtype)
admin.site.register(TbIndicatorusermapp)
admin.site.register(TbUserhealthwarningmapp)
admin.site.register(TbHospitaldoctorrel)
admin.site.register(TbHospitalinfo)
admin.site.register(TbHospitalofficesinfo)
admin.site.register(TbIdentificationissuess)
admin.site.register(TbIdentifydiseaserel)
admin.site.register(TbIntelligentdeviceinfo)
admin.site.register(TbIdentifychoices)
admin.site.register(TbLocationinfo)
admin.site.register(TbManager)
admin.site.register(TbMeasurementunit)
admin.site.register(TbMedicalhistoryrecords)
admin.site.register(TbMedicineinfo)
admin.site.register(TbMedicineprescription)
admin.site.register(TbMedicineprescriptionmapp)
admin.site.register(TbMedicineuseinfo)
admin.site.register(TbMycollection)
admin.site.register(TbPhoneappinfo)
admin.site.register(TbPhoneinfo)
admin.site.register(TbPhonemonitorrecords)
admin.site.register(TbPhonepreferuserecords)
admin.site.register(TbPhysiqueinfo)
admin.site.register(TbPicturelist)
admin.site.register(TbSetmealfoodmapp)
admin.site.register(TbSleepinforecords)
admin.site.register(TbSleeppreferrecords)
admin.site.register(TbSportinforecords)
admin.site.register(TbStatisticofclick)
admin.site.register(TbSupervisorylevel)
admin.site.register(TbTcmdcotorsinfo)
admin.site.register(TbTcmdiagnosisobj)
admin.site.register(TbTcmdiagnosistype)
admin.site.register(TbTcmhealthknowledge)
admin.site.register(TbUser, MyUserAdmin)
admin.site.register(TbUseranswerrecords)
admin.site.register(TbUserexercisefeature)
admin.site.register(TbUserknowledgemapp)
admin.site.register(TbUserreviewstat)
admin.site.register(TbUsersleepfeature)
admin.site.register(TbVariousindicatorstandard)
admin.site.register(TbVariousindicatorlimited)
admin.site.register(TbWesmedicineexamitem)
admin.site.register(TbWtreatmentrecords)