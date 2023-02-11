# Application definition

PREINSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'drf_yasg',
    'diodes',

]

INSTALLED_APPS = PREINSTALLED_APPS + PROJECT_APPS

