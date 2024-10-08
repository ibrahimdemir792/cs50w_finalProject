"""
URL configuration for language_flashcards project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flashcards import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_deck/', views.create_deck, name='create_deck'),
    path('deck/<int:deck_id>/', views.deck_detail, name='deck_detail'),
    path('deck/<int:deck_id>/add_flashcard/', views.add_flashcard, name='add_flashcard'),
    path('deck/<int:deck_id>/edit_flashcard/<int:card_id>/', views.edit_flashcard, name='edit_flashcard'),
    path('deck/<int:deck_id>/delete_flashcard/<int:card_id>/', views.delete_flashcard, name='delete_flashcard'),
    path('deck/<int:deck_id>/delete/', views.delete_deck, name='delete_deck'),
    path('study/', views.study, name='study'),
    path('deck/<int:deck_id>/study/', views.study_deck, name='study_deck'),
    path('get_flashcards/<int:deck_id>/', views.get_flashcards, name='get_flashcards'),
    path("__reload__/", include("django_browser_reload.urls")),
    
]
