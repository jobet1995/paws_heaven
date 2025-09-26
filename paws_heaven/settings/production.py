"""
Production settings for Paws Heaven project.
"""
from .base import *
import os
import dj_database_url
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Security settings
ALLOWED_HOSTS = [
    'animalshelter.com',
    'www.animalshelter.com',
    'staging.animalshelter.com',
    'dev.animalshelter.com',
    'qa.animalshelter.com',
    'sit.animalshelter.com',
]

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

# Security settings - these should be set in your environment variables
# and will be loaded via base.py

# Additional security settings
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

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
