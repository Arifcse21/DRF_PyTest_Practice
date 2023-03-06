# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'USER': os.environ.get("DB_USER"),
        'HOST': "db",
        'PORT': "5432"
    }
}
