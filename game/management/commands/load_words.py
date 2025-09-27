from django.core.management.base import BaseCommand
from game.models import Word

class Command(BaseCommand):
    help = 'Loads initial words into the database'

    def handle(self, *args, **kwargs):
        words = [
            'APPLE', 'BEACH', 'BRAIN', 'BREAD', 'BRUSH',
            'CHAIR', 'CHEST', 'CHORD', 'CLICK', 'CLOCK',
            'CLOUD', 'DANCE', 'DIARY', 'DRINK', 'EARTH',
            'FLUTE', 'FRUIT', 'GHOST', 'GRAPE', 'GREEN'
        ]

        for word_text in words:
            Word.objects.get_or_create(text=word_text)
        self.stdout.write(self.style.SUCCESS('Successfully loaded words'))
