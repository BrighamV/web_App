from django.apps import AppConfig

# adding our calc app
class CalcConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calc'
