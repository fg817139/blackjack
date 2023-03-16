import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        if card.value == "A":
            self.aces += 1
        self.value += self.get_card_value(card)

    def get_card_value(self, card):
        if card.value in ["J", "Q", "K"]:
            return 10
        elif card.value == "A":
            return 11
        else:
            return int(card.value)

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}.")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal_card())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == "h":
            hit(deck, hand)

        elif x[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player):




