from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create superuser custom command'

    def handle(self, *args, **kwargs):
        try:
            User.objects.create_superuser('admin', 'admin@example.com', '2128506')
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(self.style.SUCCESS("created superuser"))