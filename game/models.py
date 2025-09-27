from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    games_played_today = models.IntegerField(default=0)
    last_played_date = models.DateField(null=True, blank=True)

    def can_play(self):
        today = timezone.now().date()
        if self.last_played_date != today:
            self.games_played_today = 0
            self.last_played_date = today
            self.save()
        return self.games_played_today < 3

class Word(models.Model):
    text = models.CharField(max_length=5, unique=True)
    def __str__(self):
        return self.text

class Game(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='games')
    word_to_guess = models.ForeignKey(Word, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_won = models.BooleanField(default=False)
    guesses_left = models.IntegerField(default=5)
    def __str__(self):
        return f"{self.user.username}'s game on {self.start_time.strftime('%Y-%m-%d')}"

class Guess(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='guesses')
    word = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Guess '{self.word}' in game {self.game.id}"