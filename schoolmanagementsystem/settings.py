"""
Django settings for schoolmanagementsystem project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0vix_w(31%o^nstx$wdnb1mm&*f5=5tu*h#kvu&gt=e(r&i+x$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["schoolmanagementsystem-production.up.railway.app","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
    'sales',
    'account',
    'students',
    'parents',
    'classes',
    "fees",
    'core',
    "enrolment",
    "mathfilters",
    "billing",
    "subjects",
    "payments",
    "num2words"
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'schoolmanagementsystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # os.path.join(BASE_DIR, 'account', 'templates','account'),
            # os.path.join(BASE_DIR, 'parents', 'templates','parents'),
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\parents\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\sales\template", 
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\account\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\students\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\classes\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\fees\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\core\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\enrolment\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\billing\template",
            # r"C:\Users\stev\Desktop\myenv\SCHOOLMANAGEMENTSYSTEM\subjects\template",

            ],
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

WSGI_APPLICATION = 'schoolmanagementsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL =  'static/'       #'https://schoolmanagementsystem-production.up.railway.app/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = ['https://schoolmanagementsystem-production.up.railway.app']

