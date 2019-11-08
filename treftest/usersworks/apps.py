from django.apps import AppConfig


class UsersworksConfig(AppConfig):
    name = 'usersworks'


    def ready(self):
        import usersworks.signals
