"""
Testing settings for Paws Heaven project.
"""
from .base import *

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

# Use in-memory SQLite for faster tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
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
import logging
logging.disable(logging.CRITICAL)
