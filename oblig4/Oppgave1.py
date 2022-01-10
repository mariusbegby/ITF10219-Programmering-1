import blackjack_module as bjm  #importerer blackjack_module.py

# Setter chips til å begynne med
player_chips = 5

# En loop som sjekker om spillet er avsluttet eller ikke.
# Spiller vil fortsette med runder så lenge brukeren ikke vil avslutte.
game_ended = False
while game_ended == False:
    round_ended = False

    # Genererer en tilfeldig ny kortstokk med 52 kort.
    # Setter spiller og dealer hånd til 0 kort i starten av en runde.
    shuffled_deck = bjm.get_new_shuffled_deck()
    player_hand = []
    dealer_hand = []

    # Har spilleren 0 eller under 0 chips, avsluttes spillet.
    if player_chips <= 0:
        print("You have 0 chips left and lost the game. Thanks for playing")
        game_ended = True
        break

    # Sjekker om spilleren gir et gyldig input som innsats.
    try:
        bet = int(input(f"You have {player_chips} chips. How much do you want to bet? "))
        if bet > player_chips:
            print(f"You cannot bet more chips than you have. You have {player_chips} chips.")
            continue
    except ValueError:
        print("You have to enter an integer number.")
        continue
    except:
        print("En feil har oppstått. Du har skrevet inn noe ugyldig. Forsøk igjen.")
        continue


    # Gir de to første kortene til spiller og dealer, og printer dette ut som tekst.
    bjm.deal_initial_cards(shuffled_deck, player_hand, dealer_hand)
    bjm.print_initial_cards(player_hand, dealer_hand)

    # Sjekker om spilleren fikk blackjack på de to første kortene.
    if bjm.calculate_hand_value(player_hand) == 21:
        print(f"\nYou have a value of 21 and hit blackjack!")
        player_chips = player_chips + bet * 2
        print(f"You won {bet*2} chips and now have {player_chips} chips in total.")
        round_ended = True

    # En loop som sjekker om runden er avsluttet eller ikke.
    while round_ended == False:
        # Spør brukeren om de vil ha flere kort eller beholde de kortene de har og ikke få noen fler.
        print(f"\nYou have a value of {bjm.calculate_hand_value(player_hand)}. Do you wish to hit or stand?")
        print("1) Hit")
        print("2) Stand")
        choice = input("Ditt valg: ")

        # HIT
        if choice == "1":
            print("\nYou chose to hit.")
            bjm.player_hit(shuffled_deck, player_hand)
            # Er verdien over 21, tapte spilleren.
            if bjm.calculate_hand_value(player_hand) > 21:
                print("\nYou busted, your total value is over 21.")
                player_chips = player_chips - bet
                print(f"You lost {bet} chips and now have {player_chips} chips left.")
                round_ended = True
            else:
                bjm.print_hand(player_hand)
        # STAND
        elif choice == "2":
            print("\nYou chose to stand.")
            # Hvis spilleren velger å ikke få fler kort, trekker dealeren kort til verdien blir >= 17
            bjm.stand(shuffled_deck, player_hand, dealer_hand)
            player_chips = bjm.print_result(player_hand, dealer_hand, player_chips, bet)
            print("")
            round_ended = True

    # Etter en runde, blir spilleren spurt om de vil spille en runde til. Velger de nei avsluttes spillet.
    play_again = input("The round has ended. Do you want to play another round? y/n: ")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        print("You chose to play again.\n")
        continue
    elif play_again.lower() == "n" or play_again.lower() == "no":
        print("Ending the game. Thanks for playing :)\n")
        game_ended = True
        break
    else:
        print("That is not a valid option.\n")
        break