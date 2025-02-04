import os

INSTALLED_APPS = [
    # 기본 앱들
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',  # 이 줄이 있는지 확인
    'corsheaders',     # CORS 설정
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 아직 구현되지 않은 미들웨어는 주석 처리 또는 제거
    # 'core.middleware.ip_auth.IPAuthenticationMiddleware',
    # 'core.middleware.custom_middleware.CustomMiddleware',
]

# Django 프로젝트의 기본 설정들
ROOT_URLCONF = 'core.urls'  # URL 설정 파일의 위치

# 템플릿 설정도 필요할 수 있습니다
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
            ],
        },
    },
]

# WSGI 애플리케이션 설정
WSGI_APPLICATION = 'core.wsgi.application'

# DEBUG 모드 설정 (개발 환경에서는 True)
DEBUG = True

# 허용된 호스트 설정
ALLOWED_HOSTS = ['*']  # 개발 환경에서는 모든 호스트 허용

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&p1w)%16k+y-=^rt9k8h5j_7f3c#@x2k5q%6$s!6$y(^3v=4m8'

# Database 설정도 필요합니다
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# 기본 언어 및 시간대 설정
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
