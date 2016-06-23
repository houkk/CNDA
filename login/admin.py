from django.contrib import admin
from login.models import backuser
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# Register your models here.

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = backuser

class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            backuser.objects.get(username=username)
        except backuser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])
    class Meta(UserCreationForm.Meta):
        model = backuser

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('username', 'password','area')}),
    )

admin.site.register(backuser, MyUserAdmin)