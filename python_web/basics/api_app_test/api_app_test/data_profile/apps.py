from django.apps import AppConfig

class DataProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app_test.data_profile'

    def ready(self):
        import api_app_test.data_profile.signals  # noqa