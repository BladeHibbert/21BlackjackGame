import random
import time
global deck, players_hand, cont, computer_hand, comp_cont, player_score, computer_score, chips
deck = ["A\u2665", "2\u2665", "3\u2665", "4\u2665", "5\u2665", "6\u2665", "7\u2665", "8\u2665","9\u2665", "10\u2665", "J\u2665", "Q\u2665", "K\u2665",
        "A\u25C6", "2\u25C6", "3\u25C6", "4\u25C6", "5\u25C6", "6\u25C6", "7\u25C6", "8\u25C6","9\u25C6", "10\u25C6", "J\u25C6", "Q\u25C6", "K\u25C6",
        "A\u2660", "2\u2660", "3\u2660", "4\u2660", "5\u2660", "6\u2660", "7\u2660", "8\u2660","9\u2660", "10\u2660", "J\u2660", "Q\u2660", "K\u2660",
        "A\u2663", "2\u2663", "3\u2663", "4\u2663", "5\u2663", "6\u2663", "7\u2663", "8\u2663","9\u2663", "10\u2663", "J\u2663", "Q\u2663", "K\u2663"]
chips = 10

def print_delay(string):
    print(string)
    time.sleep(1)
    
def winner(player, computer, bet):
    global chips
    if player == computer:
        print_delay("Draw")
    if player > computer and player <= 21:
        winnings = bet * 2
        print_delay("Player Wins. Chip winnings: " + str(winnings))
        chips += winnings
    elif player > computer and player > 21:
        print_delay("Player bust... Computer Wins")
    elif player < computer and computer <=21:
        print_delay("Computer Wins")
    elif player < computer and computer > 21:
        winnings = bet * 2
        print_delay("Computer bust... Player Wins. Chip winnings: " + str(winnings))
        chips += winnings

def calculate_score(hand):
    total = 0
    tens = ["A", "1", "J", "Q", "K"]
    for card in hand:
        if card[0] in tens:
            total += 10
        else:
            total += int(card[0])
    return total

def twist(hand):
    global deck
    card = random.choice(deck)
    hand.append(card)
    print_delay(card)
    print_delay("Total: " + str(calculate_score(hand)))

def players_option():
    global cont, player_score, players_hand
    options = ["stick", "twist"]
    choice = input("Would you like to stick or twist? ").lower()
    while choice not in options:
        choice = input("Would you like to stick or twist? ").lower()
    if choice == "stick":
        player_score = calculate_score(players_hand)
        print_delay("You have stuck with a total of: " + str(player_score))
        cont = False
        return cont
    elif choice == "twist":
        print_delay("Dealing another card...")
        twist(players_hand)

def players_start_turn():
    global deck, players_hand
    players_hand = []
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    players_hand.append(card1)
    players_hand.append(card2)
    print_delay("You have been dealt: " + card1 + " " + card2)
    print_delay("Total: " + str(calculate_score(players_hand)))

def computer_start_turn():
    global deck, computer_hand, comp_cont, computer_score, player_score
    comp_cont = True
    computer_hand = []
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    computer_hand.append(card1)
    computer_hand.append(card2)
    print_delay("Computer has: " + card1 + card2)
    print_delay("Total: " + str(calculate_score(computer_hand)))
    while comp_cont == True and calculate_score(computer_hand) < 17:
        print_delay("Computer twists....")
        twist(computer_hand)
    computer_score = calculate_score(computer_hand)

def players_turn():
    global cont, player_score, players_hand
    cont = True
    players_start_turn()
    while cont == True and calculate_score(players_hand) <= 21:
        players_option()
        if calculate_score(players_hand) > 21:
            print_delay("Sorry you have bust! End of go....")
    player_score = calculate_score(players_hand)

def game():
    global chips
    dealing = True
    print("Starting chip balance: ", chips)
    while dealing == True:
        bet = int(input("Please enter your betting amount: "))
        while bet > chips:
            print_delay("Bet exceeds chip balance!")
            bet = int(input("Please enter your betting amount: "))
        chips -= bet
        players_turn()
        computer_start_turn()
        winner(player_score, computer_score, bet)
        print_delay("Current chip balance: " + str(chips))
        again = input("Would you like to deal again? Y / N: ").upper()
        while again != "Y" and again != "N":
            again = input("Would you like to deal again? Y / N: ").upper()
        if again == "N":
            dealing = False
            print_delay("Thank you for playing BlackJack today!")
            print_delay("Your closing chip balance is: " + str(chips))

game()