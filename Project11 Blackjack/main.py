import random
from art import logo


def game_over(condition = "lose"):
    if condition == "lose":
        print(f"You lose")
    elif condition == "win":
        print(f"You win")
    else:
        print(f"Draw")

def draw_card(hand, score):
    """Takes a list (hand) as input and returns the same list
    with one additional card added to it. Also updates current
    hand total"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))
    score += hand[-1]
    return hand, score

def play_round():
    drawing = True

    players_hand = []
    computers_hand = []
    player_score = 0
    computer_score = 0

    print(logo)
    draw_card(players_hand, player_score)
    draw_card(players_hand, player_score)
    draw_card(computers_hand, computer_score)
    while drawing:
        print(f"Your cards: {players_hand}")
        print(f"Computer's hand: {computers_hand}")
        user_rsp = input("Draw another card? (Y/N): ")
        if user_rsp == "N":
            drawing = False
        elif user_rsp == "Y":
            draw_card(players_hand, player_score)
        else:
            print("Incorrect Response.")

        # Check if player has gone bust
        # Escape loop and deal with this outside of while loop
        if player_score > 21:
            drawing = False

    # Check if player has won
    # 'Reveal' other computer cards
    draw_card(computers_hand, computer_score)


def play():
    keep_playing = True
    while keep_playing:
        user_rsp = input("Do you want to play a game of Blackjack? (Y/N): ")
        if user_rsp == "N":
            keep_playing = False
        else:
            play_round()


play()
