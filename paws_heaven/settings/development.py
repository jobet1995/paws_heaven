"""
Development settings for Paws Heaven project.
"""
from .base import *
import socket

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dev-key-only'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow all hosts in development
ALLOWED_HOSTS = ['*']

# Get the hostname to allow access from the local network
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2'] + [ip[: ip.rfind(".")] + ".1" for ip in ips]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable security settings for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
