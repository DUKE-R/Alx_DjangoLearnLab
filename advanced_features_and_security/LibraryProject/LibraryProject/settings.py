"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6wplrk&1s7h$g$0dd1s#i*72=!t@=^_wpl^ha-9!ry!ub4bdjt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf.apps.BookshelfConfig'
    'relationship_app.apps.RelationshipAppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'  # Redirect after login
LOGOUT_REDIRECT_URL = 'login'  # Redirect after logout

import os

# Security settings
DEBUG = False  # Set to False in production
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']  # Add your domain names

# Browser-side security protections
"SECURE_BROWSER_XSS_FILTER" = True
"X_FRAME_OPTIONS" = 'DENY'
"SECURE_CONTENT_TYPE_NOSNIFF" = True

# CSRF and session cookie settings
"CSRF_COOKIE_SECURE" = True
"SESSION_COOKIE_SECURE" = True

# Additional security headers (CSP is addressed later)
SECURE_HSTS_SECONDS = 31536000  # Enforce HTTPS for one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure HTTPS is used (for production) 1
SECURE_SSL_REDIRECT = True

INSTALLED_APPS += ['csp']

MIDDLEWARE += ['csp.middleware.CSPMiddleware']

CSP_DEFAULT_SRC = ("'self'",)  # Allow resources from the same origin
CSP_SCRIPT_SRC = ("'self'", 'https://trusted-cdn.com')  # Allow inline and trusted CDN scripts
CSP_STYLE_SRC = ("'self'", 'https://trusted-cdn.com')  # Allow styles from trusted sources
CSP_IMG_SRC = ("'self'", 'data:')  # Allow images from the same origin and inline

# Security settings for the LibraryProject

# Prevent Cross-Site Scripting (XSS) attacks
SECURE_BROWSER_XSS_FILTER = True

# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from guessing MIME types
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure CSRF and session cookies are transmitted over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

import os

# Determine environment: development or production
IS_PRODUCTION = os.getenv('DJANGO_PRODUCTION', 'False') == 'True'

if IS_PRODUCTION:
    DEBUG = False  # Always False in production
    SECURE_BROWSER_XSS_FILTER == True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
else:
    DEBUG = True

AUTH_USER_MODEL = 'bookshelf.CustomUser'

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'  # Prevents the site from being framed (clickjacking protection)
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie is sent over HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookie is sent over HTTPS

ALLOWED_HOSTS = ['yourdomain.com', 'subdomain.yourdomain.com']
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS

