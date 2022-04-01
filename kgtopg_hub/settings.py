"""
Django settings for kgtopg_hub project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@izgnxdy5orljjht_t2c3)qia@43^wz_%w3w8&zy!i3gpu6+0j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', 'https://kgtopg.com', "192.168.1.100", ]


# Application definition

INSTALLED_APPS = [
    'base.apps.BaseConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kgtopg_hub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kgtopg_hub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'kgtopg_blog',
        'USER': 'depl',
        'PASSWORD': 'depl@0369',
        'HOST': '192.168.1.100'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "noreply2.kgtopg@gmail.com"
EMAIL_HOST_PASSWORD = "Kgtopg@123$"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CORS_ORIGIN_ALLOW_ALL = True


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# SITE_URL = 'http://127.0.0.1:8000'
# AUTH_URL = 'http://127.0.0.1:8001'
# PLATFORM_URL = 'http://127.0.0.1:8002'
# PARTNER_URL = 'http://127.0.0.1:8004'
# PUSTAK_URL = 'http://127.0.0.1:8003'
# SCHOOLER_URL = 'https://kgtopg.com'
# QBANK_URL = 'http://127.0.0.1:8005'
SITE_URL = 'http://192.168.1.101:8000'
AUTH_URL = 'http://192.168.1.101:8001'
PLATFORM_URL = 'http://192.168.1.101:8002'
PARTNER_URL = 'http://192.168.1.101:8004'
PUSTAK_URL = 'http://192.168.1.101:8003'
SCHOOLER_URL = 'http://192.168.1.100:8080/my-webapp/'
QBANK_URL = 'http://192.168.1.101:8005'
