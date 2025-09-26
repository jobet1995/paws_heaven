"""
Production settings for Paws Heaven project.
"""
import os
from pathlib import Path
import dj_database_url
from decouple import config

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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# Ensure the secret key is strong enough
if len(SECRET_KEY) < 50 or SECRET_KEY.startswith('django-insecure-'):
    raise ValueError('SECRET_KEY must be at least 50 characters long and not start with django-insecure-')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Security settings
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='.animalshelter.com,localhost,127.0.0.1').split(',')

# Ensure we have at least one allowed host
if not ALLOWED_HOSTS:
    raise ValueError('DJANGO_ALLOWED_HOSTS must be set in production')

# Security middleware settings
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HSTS Settings
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=31536000, cast=int)  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=True, cast=bool)

# Secure Cookies
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)

# Security Headers
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=True, cast=bool)
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=True, cast=bool)
X_FRAME_OPTIONS = config('X_FRAME_OPTIONS', default='DENY')
SECURE_REFERRER_POLICY = config('SECURE_REFERRER_POLICY', default='same-origin')

# Session settings
SESSION_COOKIE_HTTPONLY = config('SESSION_COOKIE_HTTPONLY', default=True, cast=bool)
CSRF_COOKIE_HTTPONLY = config('CSRF_COOKIE_HTTPONLY', default=True, cast=bool)

# Database configuration
DATABASES = {
    'default': {
        **dj_database_url.config(
            default=config('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=True
        ),
        'OPTIONS': {
            'sslmode': 'require',
            'connect_timeout': 10,
        }
    }
}

# Database connection health checks
DATABASES['default']['ATOMIC_REQUESTS'] = True  # Wrap each HTTP request in a transaction
DATABASES['default']['CONN_MAX_AGE'] = 600  # Reuse database connections for up to 10 minutes

# Security settings
# HSTS Settings - Enable only if you're sure
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# SSL/HTTPS settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Session settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# CSRF settings
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = [
    'https://animalshelter.com',
    'https://www.animalshelter.com',
    'https://staging.animalshelter.com',
    'https://dev.animalshelter.com',
    'https://qa.animalshelter.com',
    'https://sit.animalshelter.com',
]

# Referrer Policy
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

# Content Security
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Ensure the static and media directories exist
os.makedirs(STATIC_ROOT, exist_ok=True)
os.makedirs(MEDIA_ROOT, exist_ok=True)

# Session settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

# Security headers
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# CSRF settings
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_USE_SESSIONS = False
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

# Trusted origins for CSRF and other security features
CSRF_TRUSTED_ORIGINS = [
    'https://animalshelter.com',
    'https://www.animalshelter.com',
    'https://staging.animalshelter.com',
    'https://dev.animalshelter.com',
    'https://qa.animalshelter.com',
    'https://sit.animalshelter.com',
]

# Content Security Policy (CSP) - Uncomment and configure as needed
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", 'cdn.jsdelivr.net', 'code.jquery.com')
# CSP_STYLE_SRC = ("'self'", 'cdn.jsdelivr.net')
# CSP_IMG_SRC = ("'self'", 'data:', 'blob:')
# CSP_FONT_SRC = ("'self'", 'cdn.jsdelivr.net')
# CSP_CONNECT_SRC = ("'self'")
# CSP_OBJECT_SRC = ("'none'")
# CSP_BASE_URI = ("'self'")
# CSP_FORM_ACTION = ("'self'")
# CSP_FRAME_ANCESTORS = ("'none'")

# Security middleware - ensure these are in your MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
] + MIDDLEWARE

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@animalshelter.com')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_errors.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Security middleware
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

# Content Security Policy (CSP) - Configure based on your needs
# Requires django-csp to be installed
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_IMG_SRC = ("'self'", 'data:')
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")

# HTTPS settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

# Session settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_SAVE_EVERY_REQUEST = True

# CSRF settings
CSRF_COOKIE_AGE = 31449600  # 1 year in seconds
CSRF_USE_SESSIONS = False

# Static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
