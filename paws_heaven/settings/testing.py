"""
Testing settings for Paws Heaven project.
"""
from .base import (
    ALLOWED_HOSTS, AUTH_PASSWORD_VALIDATORS, BASE_DIR, CSRF_COOKIE_SECURE,
    DATABASES, DEBUG, DEFAULT_AUTO_FIELD, INSTALLED_APPS, LANGUAGE_CODE,
    MIDDLEWARE, ROOT_URLCONF, SECRET_KEY, SECURE_HSTS_SECONDS,
    SECURE_SSL_REDIRECT, SESSION_COOKIE_SECURE, STATICFILES_DIRS, STATIC_ROOT,
    STATIC_URL, TEMPLATES, TIME_ZONE, USE_I18N, USE_TZ, WSGI_APPLICATION,
    MEDIA_URL, MEDIA_ROOT, PASSWORD_HASHERS
)

# SECURITY WARNING: keep the secret key used in testing secret!
SECRET_KEY = 'django-insecure-test-key-only'

# SECURITY WARNING: don't run with debug turned on in testing!
DEBUG = False

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable password hashing for faster tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Disable security settings for testing
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
