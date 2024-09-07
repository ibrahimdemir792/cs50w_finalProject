from django import forms
from .models import Deck, Flashcard

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name', 'language']

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['front', 'back']