from django.core.management.base import BaseCommand
from themes.models import Theme

class Command(BaseCommand):
    help = 'Initialize default themes'

    def handle(self, *args, **options):
        Theme.create_default_themes()
        self.stdout.write(self.style.SUCCESS('Successfully initialized themes'))
