"""
Paws Heaven settings package.
"""
import os
from .base import *  # noqa

# Import the appropriate settings based on the environment
ENV = os.environ.get('DJANGO_ENV', 'development')

if ENV == 'production':
    from .production import *  # noqa
else:
    from .development import *  # noqa
