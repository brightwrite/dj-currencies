# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "bynt$r#e8#+(qwjpx4g1_s5%nv8&(6%ah@)hfl+0qk8b(-ius^"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xcover',
        'USER': 'xcover_dev',
        'HOST': 'localhost',
        'PASSWORD': 'xcover_local_pwd',
        'PORT': '5432',
    }
}

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "dj_currencies",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()


django.setup()
