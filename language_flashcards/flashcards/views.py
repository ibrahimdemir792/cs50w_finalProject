from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Deck, Flashcard
from .forms import DeckForm, FlashcardForm
from datetime import datetime, timedelta


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'flashcards/register.html', {'form': form})

def index(request):
    return render(request, 'flashcards/index.html')


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
    flashcards = deck.flashcard_set.all()
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
def statistics(request):
    user_decks = Deck.objects.filter(user=request.user)
    total_cards = Flashcard.objects.filter(deck__in=user_decks).count()
    total_study_sessions = StudySession.objects.filter(user=request.user).count()
    
    # Add more complex statistics calculations here
    
    context = {
        'total_decks': user_decks.count(),
        'total_cards': total_cards,
        'total_study_sessions': total_study_sessions,
    }
    return render(request, 'flashcards/statistics.html', context)


@login_required
def study_card(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id, user=request.user)
    card = deck.flashcard_set.filter(last_reviewed__lte=datetime.now() - timedelta(days=1)).first()
    
    if request.method == 'POST':
        quality = int(request.POST.get('quality', 3))
        card.ease_factor = max(1.3, card.ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        card.interval = card.interval * card.ease_factor
        card.last_reviewed = datetime.now()
        card.save()
        return redirect('study_card', deck_id=deck.id)
    
    return render(request, 'flashcards/study_card.html', {'card': card})