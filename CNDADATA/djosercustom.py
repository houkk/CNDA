# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from djoser.views import UserView, RegistrationView, SetPasswordView, PasswordResetView, LoginView
from djoser import settings, utils, constants
import simplejson
from django.contrib.auth import authenticate, get_user_model
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings as django_settings
from CNDADATA.filter import TbUserFilter
from CNDADATA.models import TbUser, RestFrameworkToken
from CNDADATA.LianBiaoSerializer import TbUserCombineSerializer
from rest_framework import permissions, status, response, serializers, viewsets, generics
class userview(serializers.ModelSerializer):
    temp_picturelocationid = serializers.ImageField(source='temp_picturelocationid.originalpicturepath')
    class Meta:
        model = TbUser
        fields = (
            'userid', 'username', 'usersex', 'userage','name',
            'userphonenumber', 'email', 'userrank', 'userwroktype', 'userbmiindex',
            'temp_sleepfeatureid', 'temp_exercisefeatureid', 'temp_eatingfeatureid', 'temp_adminisareaid',
            'temp_picturelocationid',
        )
class customuserview(viewsets.ModelViewSet):
    model = TbUser
    #serializer_class = userview
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filter_class = TbUserFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return TbUserCombineSerializer
        if self.action == 'partial_update':
            return TbUserCombineSerializer
        return userview
    def get_queryset(self):
        return TbUser.objects.filter(userid=self.request.user.userid)

class changepassword(SetPasswordView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        from djoser import serializers
        print serializers.SetPasswordSerializer
        if settings.get('SET_PASSWORD_RETYPE'):
            return serializers.SetPasswordRetypeSerializer
        return serializers.SetPasswordSerializer
    def action(self, serializer):
        self.request.user.set_password(serializer.data['new_password'])
        self.request.user.save()
        RestFrameworkToken.objects.filter(user=self.request.user).delete()
        return response.Response(status=status.HTTP_200_OK)
def validate(request):
    result = {}
    if request.method == 'GET':
        if request.GET.get('username'):
            username = request.GET.get('username')
            re = TbUser.objects.filter(username=username)
            if re:
                result['result'] = 1
            else:
                result['result'] = 0
        elif request.GET.get('email'):
            email = request.GET.get('email')
            re = TbUser.objects.filter(email=email)
            if re:
                result['result'] = 1
            else:
                result['result'] = 0
        else:
            request['result'] = 0
    else:
        result['result'] = 0
    return HttpResponse(simplejson.dumps(result))
def send_email(to_email, from_email, context, subject_template_name,
               plain_body_template_name, html_body_template_name=None):
    subject = loader.render_to_string(subject_template_name, context)
    subject = ''.join(subject.splitlines())
    body = loader.render_to_string(plain_body_template_name, context)
    email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
    if html_body_template_name is not None:
        html_email = loader.render_to_string(html_body_template_name, context)
        email_message.attach_alternative(html_email, 'text/html')
    email_message.send()
def encode_uid(pk):
    try:
        from django.utils.http import urlsafe_base64_encode
        from django.utils.encoding import force_bytes
        return urlsafe_base64_encode(force_bytes(pk)).decode()
    except ImportError:
        from django.utils.http import int_to_base36
        return int_to_base36(pk)
class SendEmailViewMixin(object):
    def send_email(self, to_email, from_email, context):
        send_email(to_email, from_email, context, **self.get_send_email_extras())

    def get_send_email_kwargs(self, user):
        return {
            'from_email': getattr(django_settings, 'DEFAULT_FROM_EMAIL', None),
            'to_email': user.email,
            'context': self.get_email_context(user),
        }

    def get_send_email_extras(self):
        raise NotImplemented

    def get_email_context(self, user):
        token = self.token_generator.make_token(user)
        uid = encode_uid(user.pk)
        return {
            'user': user,
            'domain': settings.get('DOMAIN'),
            'site_name': settings.get('SITE_NAME'),
            'uid': uid,
            'token': token,
            'protocol': 'https' if self.request.is_secure() else 'http',
        }

class Passwordresert(utils.ActionViewMixin, SendEmailViewMixin, generics.GenericAPIView):
    from djoser import serializers
    serializer_class = serializers.PasswordResetSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    token_generator = default_token_generator

    def action(self, serializer):
        print serializer.data['email']

        for user in self.get_users(serializer.data['email']):
            self.send_email(**self.get_send_email_kwargs(user))
        return response.Response(status=status.HTTP_200_OK)

    def get_users(self, email):
        print email
        active_users = TbUser.objects.filter(#_default_manager
            email=email,
            #is_active=True,
        )
        print active_users
        return (u for u in active_users if u.has_usable_password())

    def get_send_email_extras(self):
        return {
            'subject_template_name': 'password_reset_email_subject.txt',
            'plain_body_template_name': 'password_reset_email_body.txt',
        }

    def get_email_context(self, user):
        context = super(Passwordresert, self).get_email_context(user)
        context['url'] = settings.get('PASSWORD_RESET_CONFIRM_URL').format(**context)
        return context







User = get_user_model()
def create_username_field():
    username_field = User._meta.get_field(User.REQUIRED_FIELDS[0])
    if hasattr(serializers.ModelSerializer, 'field_mapping'):  # DRF 2.x
        mapping_dict = serializers.ModelSerializer.field_mapping
    elif hasattr(serializers.ModelSerializer, '_field_mapping'):  # DRF 3.0
        mapping_dict = serializers.ModelSerializer._field_mapping.mapping
    elif hasattr(serializers.ModelSerializer, 'serializer_field_mapping'):  # DRF 3.1
        mapping_dict = serializers.ModelSerializer.serializer_field_mapping
    else:
        raise AttributeError(
            'serializers.ModelSerializer doesn\'t have any of these attributes: '
            'field_mapping, _field_mapping, serializer_field_mapping '
        )
    field_class = mapping_dict[username_field.__class__]
    return field_class()

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'password',
        )
        write_only_fields = (
            'password',
        )

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.fields[User.REQUIRED_FIELDS[0]] = create_username_field()
    def validate(self, attrs):
        b = User.objects.filter(email=attrs[User.REQUIRED_FIELDS[0]])
        if b[0].check_password(attrs['password']):
            self.object = b[0]
        else:
            self.object = None
        #self.object = authenticate(email=attrs[User.REQUIRED_FIELDS[0]], password=attrs['password'])
        if self.object:
            if not self.object.is_active:
                raise serializers.ValidationError(constants.DISABLE_ACCOUNT_ERROR)
            return attrs
        else:
            raise serializers.ValidationError(constants.INVALID_CREDENTIALS_ERROR)
class customlogin(LoginView):
    serializer_class = UserLoginSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def action(self, serializer):
        from djoser import serializers
        token, _ = Token.objects.get_or_create(user=serializer.object)
        return Response(
            data=serializers.TokenSerializer(token).data,
            status=status.HTTP_200_OK,
        )


