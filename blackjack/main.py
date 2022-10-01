from logo import logo
import random

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    pick_card = random.choice(cards)
    return pick_card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, ai_score):
    if user_score > 21 and ai_score > 21:
        return 'Game Over. You lose.'
    
    if user_score == ai_score:
        return 'Draw.'
    elif ai_score == 0:
        return 'Lose, AI has Blackjack.'
    elif user_score == 0:
        return 'Win with a Blackjack.'
    elif user_score > 21:
        return 'You went over. You lose.'
    elif ai_score > 21:
        return 'AI went over. You win.'
    elif user_score > ai_score:
        return 'You win.'
    else:
        return 'You lose.'

def play_game():
    print(logo)
    
    user = []
    ai = []
    game_over = False
    
    for _ in range(2):
        user.append(deal())
        ai.append(deal())
    
    while not game_over:
        user_score = calc_score(user)
        ai_score = calc_score(ai)
        print(f'Your cards: {user}, current score: {user_score}')
        print(f"AI's first card: {ai[0]}")
        
        if user_score == 0 or ai_score == 0 or user_score > 21:
            game_over = True
        else:
            isMoreDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if isMoreDeal == 'y':
                user.append(deal())
            else:
                game_over = True
    
    while ai_score != 0 and ai_score < 17:
        ai.append(deal())
        ai_score = calc_score(ai)
    
    print(f"   Your final hand: {user}, final score: {user_score}")
    print(f"   Computer's final hand: {ai}, final score: {ai_score}")
    print(compare(user_score, ai_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    play_game()