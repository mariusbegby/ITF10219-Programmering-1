import random

full_deck = {"Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
             "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
             "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
             "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
             "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
             "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
             "Ace of diamonds": 11,
             "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
             "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
             "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
             "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
             "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
             "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
             }


def get_new_shuffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


def get_card_value(card):
    return full_deck[card]


def calculate_hand_value(hand):
    hand_value = 0

    for card in hand:
        card_value = get_card_value(card)
        if card_value == 11 and hand_value > 10:
            hand_value += 1
        else:
            hand_value += card_value

    return hand_value


def deal_initial_cards(shuffled_deck, player_hand, dealer_hand):
    player_hand.extend([shuffled_deck.pop(), shuffled_deck.pop()])
    dealer_hand.extend([shuffled_deck.pop(), shuffled_deck.pop()])


def print_initial_cards(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = get_card_value(dealer_hand[0])
    print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[1]}, with a total value of {player_value}.\nThe dealers visible card is a {dealer_hand[0]}, with a value of {dealer_value}.")


def player_hit(shuffled_deck, player_hand):
    new_card = shuffled_deck.pop()
    new_card_value = get_card_value(new_card)
    player_hand.append(new_card)
    print(f"\nYou got a new card: {new_card} with a value of {new_card_value}")


def stand(shuffled_deck, player_hand, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        new_card = shuffled_deck.pop()
        dealer_hand.append(new_card)
        print(f"The dealer got a new card {new_card} with a value of {get_card_value(new_card)}")

    print("\nThe dealer has the following cards:")
    print_hand(dealer_hand)

    print("\nYou have the following cards:")
    print_hand(player_hand)


def print_result(player_hand, dealer_hand, player_chips, bet):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        player_chips = player_chips + bet
        print(f"\nDealer bust. You won {bet} chips and now have {player_chips} chips in total.")
        return player_chips
    elif player_value > dealer_value:
        player_chips = player_chips + bet
        print(f"\nPlayer has won. You won {bet} chips and now have {player_chips} chips in total.")
        return player_chips
    elif dealer_value > player_value:
        player_chips = player_chips - bet
        print(f"\nDealer has won. You lost {bet} chips and now have {player_chips} chips left.")
        return player_chips
    else: # same value
        print(f"\nTied. You did not lose any chips and still have {player_chips} chips left.")
        return player_chips

def print_hand(hand):
    for card in hand:
        print(card)
    print(f"With a total value of {calculate_hand_value(hand)}")