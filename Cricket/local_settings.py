import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'Vinay',
    #     'USER': 'postgres',
    #     'PASSWORD': 'tiger',
    #     'HOST': 'localhost',
    #     'PORT': '5432'
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'demo_1',
    #     'USER': 'vinaypgsql',
    #     'PASSWORD': 'awspgsql',
    #     'HOST': 'database-1.c8imznctuyro.us-east-1.rds.amazonaws.com',
    #     'PORT': '5432'
    # }
}
