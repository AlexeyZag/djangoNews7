from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'

    def ready(self):
        import news.signals

        """from .tasks import send_mails
        from .scheduler import appointment_scheduler
        print('started')"""