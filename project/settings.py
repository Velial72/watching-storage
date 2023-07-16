import os
from environs import Env


env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': os.environ['DB_ENGINE'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

DEBUG = os.getenv("DEBUG", False)

SECRET_KEY = os.environ['SECRET_KEY']

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = os.getenv('localhost')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
