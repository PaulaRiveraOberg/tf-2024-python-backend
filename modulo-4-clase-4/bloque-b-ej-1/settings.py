INSTALLED_APPS = [
    #...
    'rest_framework',  # Habilita Django REST Framework.
    'rest_framework.authtoken',  # Habilita la autenticación por tokens.
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # Configura la autenticación por token.
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Requiere autenticación para acceder a los endpoints.
    ],
}
