from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Deck, Flashcard
from .forms import DeckForm, FlashcardForm
from django.utils import timezone
import random
from django.http import JsonResponse

def home(request):
    if request.user.is_authenticated:
        decks = Deck.objects.filter(user=request.user)
    else:
        decks = []
    return render(request, 'flashcards/index.html', {'decks': decks})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'flashcards/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'flashcards/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    decks = Deck.objects.filter(user=request.user)
    return render(request, 'flashcards/profile.html', {'decks': decks})

@login_required
def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('deck_detail', deck_id=deck.id)
    else:
        form = DeckForm()
    return render(request, 'flashcards/create_deck.html', {'form': form})

@login_required
def deck_detail(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    flashcards = Flashcard.objects.filter(deck=deck)
    return render(request, 'flashcards/deck_detail.html', {'deck': deck, 'flashcards': flashcards})

@login_required
def add_flashcard(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.deck = deck
            flashcard.save()
            return redirect('deck_detail', deck_id=deck.id)
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_flashcard.html', {'form': form, 'deck': deck})

@login_required
def edit_flashcard(request, deck_id, card_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    flashcard = get_object_or_404(Flashcard, id=card_id, deck=deck)
    
    if request.method == 'POST':
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            form.save()
            return redirect('deck_detail', deck_id=deck.id)
    else:
        form = FlashcardForm(instance=flashcard)
    
    return render(request, 'flashcards/edit_flashcard.html', {
        'form': form,
        'deck': deck,
        'flashcard': flashcard
    })

@login_required
def delete_flashcard(request, deck_id, card_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    flashcard = get_object_or_404(Flashcard, id=card_id, deck=deck)
    flashcard.delete()
    return redirect('deck_detail', deck_id=deck.id)

@login_required
def study(request):
    decks = Deck.objects.filter(user=request.user)
    return render(request, 'flashcards/study_list.html', {'decks': decks})

@login_required
def study_deck(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    return render(request, 'flashcards/study.html', {'deck': deck})

@login_required
def get_flashcards(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    flashcards = list(Flashcard.objects.filter(deck=deck).values('id', 'front', 'back'))
    return JsonResponse(flashcards, safe=False)

@login_required
def study_results(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    return render(request, 'flashcards/study_results.html', {'deck': deck})