# -*- coding: utf-8 -*-

from .common import *

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'domain_info'
EMAIL_HOST_PASSWORD = 'password'
DEFAULT_FROM_EMAIL = 'info@domain.com.co'
SERVER_EMAIL = 'info@domain.com.co'

SECURITY_MIDDLEWARE = (
    'djangosecure.middleware.SecurityMiddleware',
)

# Make sure djangosecure.middleware.SecurityMiddleware is listed first
MIDDLEWARE_CLASSES = SECURITY_MIDDLEWARE + MIDDLEWARE_CLASSES

# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SECURE_SSL_REDIRECT = True



