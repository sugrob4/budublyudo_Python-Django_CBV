"""
Django settings for budublyudo project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from pathlib import Path, PurePath


def get_custom_path(url, arg, kwrg=None):
    if kwrg is not None:
        p = PurePath(url, arg, kwrg)
    else:
        p = PurePath(url, arg)
    return str(p)


PROJECT_PACKAGE = Path(__file__).resolve().parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = str(PROJECT_PACKAGE.parent)

IMAGE_UPLOAD_DIR = "img_article"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'suit',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'budublyudo',
    'loginsys',
    'pages',
    'content',
    'ckeditor',
    'ckeditor_uploader',
    'easy_thumbnails',
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

# APPEND_SLASH = False

ROOT_URLCONF = 'budublyudo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [get_custom_path(PROJECT_PACKAGE, 'templates'),],
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

WSGI_APPLICATION = 'budublyudo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'budublyudo',
        'USER': 'admin',
        'PASSWORD': '12345',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Jerusalem'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = get_custom_path(PROJECT_PACKAGE, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = get_custom_path(PROJECT_PACKAGE, 'media')

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Admin budublyudo',

    # menu
    'MENU_OPEN_FIRST_CHILD': False,

    'SEARCH_URL': '',

    'MENU_ICONS': {
        'content': 'icon-book',
        'auth': 'icon-lock',
        'pages': 'icon-file',
        'filebrowser': 'icon-picture',
    },

    # misc
    'LIST_PER_PAGE': 100
}

CKEDITOR_JQUERY_URL = get_custom_path(STATIC_ROOT, 'js', 'jquery-3.3.1.js')
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'none',
        'width': 'auto',
        'height': 400,
        'forcePasteAsPlainText': True,
        'language': 'ru',
        'filebrowserBrowseUrl': '/admin/filebrowser/browse?pop=3',
        'filebrowserUploadUrl': '/admin/filebrowser/browse?pop=3',
    },
}
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False

'''
django-filebrowser: 
Путь сохранёных изображений по умолчанию `uploads/`,
дубликаты сохраняются в папке `_versions`
'''
FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_ADMIN_VERSIONS = [] # Сохранять только одну версию дубликата
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'


MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'