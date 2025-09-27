from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('new_game/', views.new_game, name='new_game'),
    path('play/<int:game_id>/', views.play_game, name='play_game'),
    path('reports/', views.reports, name='reports'),
]
