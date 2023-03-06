# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "postgres",
        'PASSWORD': "postgres",
        'USER': "postgres",
        'HOST': "db",
        'PORT': "5432"
    }
}
