"""
Django settings for restaurant project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url  # Allows configuring the database via an environment variable

# If an env.py file exists, import it (used for environment variables)
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3c)tmjt&9e7m82+fmrb!o_-u(8d6+ekm-!-gow(vhr2v5k(a)3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Should be False in production for security

ALLOWED_HOSTS = ['restaurant-res.herokuapp.com', 'localhost']  # Hosts that can access the Django app (add domain/IP in production)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin panel
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Message framework
    'cloudinary_storage',  # Cloudinary storage for media files
    'django.contrib.staticfiles',  # Static files handling
    'cloudinary',  # Cloudinary API for image storage
    'reservation',  # Custom Django app for reservations
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages sessions
    'django.middleware.common.CommonMiddleware',  # Handles various common tasks
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Handles user authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Manages messages framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents clickjacking
]

ROOT_URLCONF = 'restaurant.urls'  # Points to the project's URL configuration

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template engine
        'DIRS': [TEMPLATES_DIR],  # Can specify directories for templates if needed
        'APP_DIRS': True,  # Enables searching templates within installed apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Adds request object to templates
                'django.contrib.auth.context_processors.auth',  # Adds user authentication to templates
                'django.contrib.messages.context_processors.messages',  # Enables messages in templates
            ],
        },
    },
]

WSGI_APPLICATION = 'restaurant.wsgi.application'  # WSGI application for deployment

# Database configuration (uses SQLite by default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database backend
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file path
    }
}

# Password validation (security settings for user authentication)
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'  # Language setting
TIME_ZONE = 'UTC'  # Time zone setting
USE_I18N = True  # Enables translation
USE_L10N = True  # Enables localized formatting
USE_TZ = True  # Uses time zone support

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # URL path for serving static files
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashed'  # Cloudinary storage for static files

# This is for collecting static files from different sources
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]  

# This is where collected static files will be stored when running collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files (uploads like images)
MEDIA_URL = '/media/'  # URL path for serving media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'  # Cloudinary storage for media files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default primary key type for models
