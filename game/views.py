import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, GuessForm
from .models import Word, Game, Guess, CustomUser
from django.utils import timezone
from datetime import date
from .decorators import never_cache

@never_cache
def landing_page(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('reports')
        else:
            return redirect('home')
    return render(request, 'landing_page.html')

@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing_page')

@login_required
@never_cache 
def home(request):
    if request.user.is_superuser:
        return redirect('reports')
    return render(request, 'home.html')

@login_required
@never_cache 
def new_game(request):
    user = request.user
    if not user.can_play():
        return render(request, 'home.html', {'message': "You've already played 3 games today. Come back tomorrow!"})
    word_list = list(Word.objects.all())
    random_word = random.choice(word_list)
    game = Game.objects.create(user=user, word_to_guess=random_word)
    user.games_played_today += 1
    user.save()
    return redirect('play_game', game_id=game.id)

@login_required
@never_cache 
def play_game(request, game_id):
    game = Game.objects.get(id=game_id, user=request.user)
    form = GuessForm()
    if request.method == 'POST' and game.guesses_left > 0 and not game.is_won:
        form = GuessForm(request.POST)
        if form.is_valid():
            guess_word = form.cleaned_data['guess']
            Guess.objects.create(game=game, word=guess_word)
            game.guesses_left -= 1
            if guess_word == game.word_to_guess.text:
                game.is_won = True
                game.end_time = timezone.now()
            game.save()
            return redirect('play_game', game_id=game.id)
    guesses_with_feedback = []
    for guess in game.guesses.all():
        feedback = []
        target_word = game.word_to_guess.text
        for i, letter in enumerate(guess.word):
            if letter == target_word[i]:
                feedback.append({'letter': letter, 'color': 'green'})
            elif letter in target_word:
                feedback.append({'letter': letter, 'color': 'orange'})
            else:
                feedback.append({'letter': letter, 'color': 'grey'})
        guesses_with_feedback.append(feedback)
    context = {'game': game, 'form': form, 'guesses_with_feedback': guesses_with_feedback, 'message': None}
    if game.is_won:
        context['message'] = "Congratulations, you've guessed the word!"
    elif game.guesses_left <= 0:
        context['message'] = f"Better luck next time."
    return render(request, 'game.html', context)

@login_required
@never_cache 
def reports(request):
    if not request.user.is_superuser:
        return redirect('home')
    today = date.today()
    games_today = Game.objects.filter(start_time__date=today)
    users_today = games_today.values('user').distinct().count()
    correct_guesses_today = games_today.filter(is_won=True).count()
    user_report = None
    selected_user_id = request.GET.get('user_id')
    if selected_user_id:
        selected_user = CustomUser.objects.get(id=selected_user_id)
        user_games = Game.objects.filter(user=selected_user).order_by('-start_time').prefetch_related('guesses')
        user_report = {'username': selected_user.username, 'games': user_games}
    all_users = CustomUser.objects.filter(is_superuser=False, is_staff=False)
    context = {'today': today, 'users_today': users_today, 'correct_guesses_today': correct_guesses_today, 'all_users': all_users, 'user_report': user_report}
    return render(request, 'reports.html', context)

