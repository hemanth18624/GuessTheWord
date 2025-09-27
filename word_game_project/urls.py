from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from game import views as game_views

urlpatterns = [
    path('', game_views.landing_page, name='landing_page'),
    path('site-admin/', admin.site.urls),
    path('admin/login/', auth_views.LoginView.as_view(
            template_name='registration/admin_login.html',
            redirect_authenticated_user=True,
            next_page='reports'
        ), name='admin_login'),
    path('reports/', game_views.reports, name='reports'),
    path('home/', game_views.home, name='home'),
    path('register/', game_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
            template_name='registration/login.html',
            redirect_authenticated_user=True
        ), name='login'),
    path('logout/', game_views.logout_view, name='logout'),
    path('game/', include('game.urls')),
]