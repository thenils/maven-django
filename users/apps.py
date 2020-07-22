from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(Self):
    	import users.signals
