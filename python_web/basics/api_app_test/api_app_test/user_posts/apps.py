from django.apps import AppConfig


class UserPostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app_test.user_posts'

    def ready(self):
        import api_app_test.user_posts.signals
