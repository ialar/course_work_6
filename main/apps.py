from time import sleep

from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # def ready(self):
    #     from main.management.commands.runmailing import mailing_job
    #     sleep(2)
    #     mailing_job()
