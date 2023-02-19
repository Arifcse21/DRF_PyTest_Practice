# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'TEST': {
        #     'NAME': BASE_DIR / 'db.sqlite3',
        # }
    }
}
