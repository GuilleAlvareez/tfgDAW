from .base import *

DEBUG = False

ALLOWED_HOSTS = ['gam.ieshm.org']

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',  # Motor para mysql-connector-python
        'NAME': config('DB_NAME'),  # Nombre de la base de datos
        'USER': config('DB_USER'),                # Usuario de la base de datos
        'PASSWORD': config('DB_PASSWORD'),       # Contraseña del usuario
        'HOST': config('DB_HOST', default='localhost'),               # Dirección del servidor
        'PORT': config('DB_PORT', default='3306'),                    # Puerto de la base de datos
        'OPTIONS': {
            'autocommit': True,
        },
    }
}