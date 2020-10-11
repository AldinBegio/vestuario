from django.apps import AppConfig


class VestuarioConfig(AppConfig):
    name = 'vestuario'
    def ready(self):
        import vestuario.signals

