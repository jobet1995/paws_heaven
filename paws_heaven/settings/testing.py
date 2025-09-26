"""
Testing settings for Paws Heaven project.
"""
import logging
import os
from pathlib import Path

from .base import (
    INSTALLED_APPS, MIDDLEWARE, ROOT_URLCONF, TEMPLATES, WSGI_APPLICATION,
    AUTH_PASSWORD_VALIDATORS, LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_TZ,
    STATIC_URL, STATIC_ROOT, STATICFILES_DIRS, MEDIA_URL, MEDIA_ROOT,
    DEFAULT_AUTO_FIELD, SECURE_SSL_REDIRECT, SECURE_PROXY_SSL_HEADER,
    SECURE_HSTS_SECONDS, SECURE_HSTS_INCLUDE_SUBDOMAINS, SECURE_HSTS_PRELOAD,
    SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE, SECURE_CONTENT_TYPE_NOSNIFF,
    SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_REFERRER_POLICY,
    SESSION_COOKIE_HTTPONLY, CSRF_COOKIE_HTTPONLY, BASE_DIR
)

# SECURITY WARNING: don't run with debug turned on in testing!
DEBUG = False

# Use a fast password hasher for testing
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Security settings for testing
SECRET_KEY = 'django-insecure-test-key-1234567890-1234567890-1234567890-1234567890'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testserver']

# Disable security features that would interfere with testing
SECURE_HSTS_SECONDS = 0  # Disable HSTS for testing
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Use faster password hashing for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # Use in-memory SQLite for faster tests
    }
}

# Disable password validation in tests
AUTH_PASSWORD_VALIDATORS = []

# Disable caching for tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Disable logging during tests
logging.disable(logging.CRITICAL)
