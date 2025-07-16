import os
from pathlib import Path

# CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
# CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://localhost:6379')
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER='json'
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_TIMEZONE='Asia/Kolkata'

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/django_errors.log',
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

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-srb)9(4iv*1zd7g!+5lv3qex4t$&5q4t(yx+^%ua04#k*ns28!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['web-savileaf.onrender.com']
RECAPTCHA_SITE_KEY='6LfIjXorAAAAAF_-h9v731lG4X8gdOLUpwmYxzgp'
RECAPTCHA_SECRET_KEY='6LfIjXorAAAAAMGK5XwY3wAOwbD89BVvn5UgyyEm'
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'savileaf',
    'corsheaders',
    'django_celery_results'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'savileaf.context_processors.dropdown_items', 
                'savileaf.context_processors.footer_services',

                
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static files settings
STATIC_URL = '/static/'

# This tells Django where to find static files (for development)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'savileaf', 'static'),  # you store images/css here
]

# Only used in production (collectstatic dumps all static files here)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Email (optional, unchanged)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nischalgautam9866@gmail.com'
EMAIL_HOST_PASSWORD = 'zrbv iudw talx psiq'

# Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')