# abcpHome/apps.py

from django.apps import AppConfig

class AbcpHomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abcpHome'

    def ready(self):
        import abcpHome.signals
        print("Signals are registered")
