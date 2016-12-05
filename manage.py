#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os, sys
sys.dont_write_bytecode = True

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', 'TESTTESTTESTTESTTESTTESTTESTTEST')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,testserver').split(',')
BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
from django.conf import settings
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',  # better runserver
        'sniplates',
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    },
    STATIC_ROOT=os.path.join(BASE_DIR, '__static__'),
    MEDIA_ROOT=os.path.join(BASE_DIR, '__uploads__'),
    STATIC_URL='/__static__/',
    MEDIA_URL='/__uploads__/',
    MESSAGE_STORAGE='django.contrib.messages.storage.cookie.CookieStorage',
    SESSION_ENGINE='django.contrib.sessions.backends.signed_cookies',
    SITE_ID=1,
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    }],
    SECURE_BROWSER_XSS_FILTER=True,
    SECURE_CONTENT_TYPE_NOSNIFF=True,
)
def lazy_urls():
    # We make this lazy so that we can import stuff as necessary
    # slightly later than first-execution, which would cause issues
    # due to not having finished bootstrapping.
    from django.conf.urls import url
    from views import sniplate_widget, include, root
    # from django.contrib import admin
    urlpatterns = [
        url(r'^sniplate/$', sniplate_widget, name='sniplate_widget'),
        url(r'^include/$', include, name='include'),
        url(r'^$', root, name='index'),
    ]
    return urlpatterns
from django.utils.functional import SimpleLazyObject
urlpatterns = SimpleLazyObject(lazy_urls)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
