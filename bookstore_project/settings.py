import os
from pathlib import Path
from django.contrib.messages import constants as messages

# กำหนดเส้นทางโฟลเดอร์หลักของโปรเจกต์
BASE_DIR = Path(__file__).resolve().parent.parent

# กำหนดค่า secret key
SECRET_KEY = 'your-secret-key'
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
    'store',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# การกำหนด Tags สำหรับข้อความแจ้งเตือน
MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

# เส้นทาง URL หลัก
ROOT_URLCONF = 'bookstore_project.urls'

# Template Settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # กำหนดเส้นทางไปยังโฟลเดอร์ templates
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

# การกำหนด WSGI Application
WSGI_APPLICATION = 'bookstore_project.wsgi.application'

# Database (ใช้ SQLite ในโหมดพัฒนา)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# การตรวจสอบความปลอดภัยของรหัสผ่าน
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

# การตั้งค่า Static และ Media Files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email Backend สำหรับโหมดพัฒนา
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_USE_TLS = True

# การตั้งค่าสำหรับไฟล์ Static ในโหมด Production
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
