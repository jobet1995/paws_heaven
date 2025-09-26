"""
Production settings for Paws Heaven project.
"""
import os

import dj_database_url

from .base import (
    ALLOWED_HOSTS, AUTH_PASSWORD_VALIDATORS, BASE_DIR, CSRF_COOKIE_SECURE,
    DATABASES, DEBUG, DEFAULT_AUTO_FIELD, INSTALLED_APPS, LANGUAGE_CODE,
    MIDDLEWARE, ROOT_URLCONF, SECRET_KEY, SECURE_HSTS_SECONDS,
    SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, STATICFILES_DIRS, STATIC_ROOT,
    STATIC_URL, TEMPLATES, TIME_ZONE, USE_I18N, USE_TZ, WSGI_APPLICATION,
    MEDIA_URL, MEDIA_ROOT, STATICFILES_STORAGE
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Allowed hosts - update this in production
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
