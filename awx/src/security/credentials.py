DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "cEt3aXVxV1YzOFB1aDNldlJKZ0lZaG5UbkEuczNfbFNseHBFemVhb1phQUZQNGNvcktTTGsyU1l5U09iay0xR3JjWmwyZU5QbFl6bFViM3RCMy1SVF9wLlgubVhJYjIzOF9MaUtuSk1PTnFMSFNPaUxHM2gucFZZOVlrdmEwOGE="
