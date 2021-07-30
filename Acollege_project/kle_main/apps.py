from django.apps import AppConfig


class KleMainConfig(AppConfig):
    name = 'kle_main'

    def ready(self):
        import kle_main.signals