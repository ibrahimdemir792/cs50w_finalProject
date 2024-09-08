from django.urls import path
from . import views

urlpatterns = [
    # ... (keep other URL patterns)
    path('study/<int:deck_id>/', views.study_deck, name='study_deck'),
    path('api/flashcards/<int:deck_id>/', views.get_flashcards, name='get_flashcards'),
]