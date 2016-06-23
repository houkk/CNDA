# -*- coding: utf-8 -*-
"""
Django settings for CNDA project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j0u$#f=4v@fj9bp3+i5rp#r+%*bltr^mssl)f_9k$&5*h7k3hy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'CNDADATA',
    'corsheaders',
    'djoser',
    'rest_framework_bulk',
    'rest_framework.authtoken'
)

MIDDLEWARE_CLASSES = (
    'CNDADATA.views.DisableCSRFCheck',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CNDA.urls'

WSGI_APPLICATION = 'CNDA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'CNDA',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '10.120.56.110',
        #'HOST': '127.0.0.1',
        'PORT': '15432',
    }
}
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)


REST_FRAMEWORK = {
    #'PAGINATE_BY': 20,
    #'PAGINATE_BY_PARAM': 'limit',
    #'MAX_PAGINATE_BY': 100,# 最大值限制使用时允许 '?page_size = xxx
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_FILTER_BACKENDS': ['rest_framework_filters.backends.DjangoFilterBackend'],
    #'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.DjangoFilterBackend'],
    #'DEFAULT_RENDERER_CLASSES': ['rest_framework_jsonp.renderers.JSONPRenderer'],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    #'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
    #'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser'],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    # ),

}

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOGIN_REDIRECT_URL = '/login/loginsuccess/'

AUTH_USER_MODEL = 'CNDADATA.TbUser'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR, 'login/templates'),
    os.path.join(BASE_DIR, 'static')
)
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, STATIC_URL.replace("/", "")),
   os.path.join(BASE_DIR, STATIC_URL.replace("../static/", "")),
)
MEDIA_URL = unicode('/')
MEDIA_ROOT = '/home/Mesogene/PycharmProjects/CNDA/'
DATETIME_FORMAT = ('Y-m-d H:M:S',)
DJOSER = {
    'DOMAIN': '127.0.0.1:8000',
    'SITE_NAME': 'CNDADATA',
    'PASSWORD_RESET_CONFIRM_URL': '/auth/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'LOGIN_AFTER_REGISTRATION': True,
    #'LOGIN_AFTER_ACTIVATION': True,
    #'SEND_ACTIVATION_EMAIL': True,
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'                   #SMTP地址
EMAIL_PORT = 587                                 #SMTP端口
EMAIL_HOST_USER = '1061235338@qq.com'           #自己的邮箱名
EMAIL_HOST_PASSWORD = 'houkaiyueyueyue'           #自己的邮箱密码
EMAIL_SUBJECT_PREFIX = '2BiTT'            #为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = True
