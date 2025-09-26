"""
Testing settings for Paws Heaven project.
"""
from .base import *

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
