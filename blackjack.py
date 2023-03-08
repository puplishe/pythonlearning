__name__ = 'blackjack'
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
marks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace':11}
class Card:
    def __init__(self, suit, mark):
        self.suit = suit
        self.mark = mark
        self.value = values[mark]
    def __str__(self) -> str:
        return self.mark + 'of' + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for mark in marks:
                self.cards.append(Card(suit, mark))
    def shuffler(self):
        return random.shuffle(self.cards)
    def draw(self):
        return self.cards.pop()
    

class Balance:
    def __init__(self, money) -> None:
        self.money = money 
    def won_bet(self, bet_amount):
        self.money += bet_amount
    def lost_bet(self, bet_amount):
        self.money -= bet_amount
    def blackjack_win(self, bet_amount):
        self.money += (3/2)*bet_amount
    def __str__(self) -> str:
        return f'You now have:  {self.money} of money'



class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
    def add_card(self, new_card):
        if type(new_card) == type([]):
            self.cards.extend(new_card) 
        else:
            self.cards.append(new_card)
    def remove(self):
        return self.cards.pop(0)
    def __str__(self):
        return f'You have number of cards:   {len(self.cards)}'

class Value_Check:
    def __init__(self, list):
        self.list = list
        self.value = values
        self.total_value = 0
        self.i = 0
        if self.i <= len(self.list):
            self.list[self.i[1]]
            self.value += self
    def check(self, cards):
         self.list = cards
         return self.list
    def __str__(self) -> str:
        return f'Your score is: {self.total_value}'

exit
import pdb
new_deck = Deck()
new_deck.shuffler()
game_on = True
player_one = Player('casino')
player_two = Player('Player')
round_on = 0
#game starts
    
#print(player_one_cards[0].value)
two_hearts = Card(suits[0], marks[0])
print(two_hearts.value)
player_two_balance = Balance(500) 
while game_on:
    print(player_two_balance)
    if len(player_one.cards) != 2:
        player_one.add_card(new_deck.draw())
        player_one.add_card(new_deck.draw())
    if len(player_two.cards) != 2:
        player_two.add_card(new_deck.draw())
        player_two.add_card(new_deck.draw())
    player_one_cards = []
    player_two_cards = []
    if len(player_one_cards) < 2:
        player_one_cards.append(player_one.remove())
        player_one_cards.append(player_one.remove())
    if len(player_two_cards) < 2:
        player_two_cards.append(player_two.remove())
        player_two_cards.append(player_two.remove())
    at_table = True
    i = 0
    j = 0
    total_value_one = 0 
    total_value_two = 0
    ace_chance_one = 0
    ace_chance_two = 0
    user_draw = True
    ace_chance_two = 0
    ace_player_one = 0
    while at_table:
        round_on += 1
        print('Current round is: ', round_on)
        while i < len(player_one_cards):
           total_value_one += player_one_cards[i].value
           if player_one_cards[i].mark == 'Ace':
               ace_player_one = 1
           i += 1
        while j < len(player_two_cards):
            total_value_two += player_two_cards[j].value
            if player_two_cards[j].mark == 'Ace':
                ace_player_two = 1
            j += 1
        while total_value_one <= 17:
            player_one.add_card(new_deck.draw())
            player_one_cards.append(player_one.remove())
            total_value_one += player_one_cards[-1].value
            if total_value_one > 21 and ace_player_one == 1 and ace_chance_one == 0:
                total_value_one -= 10
                ace_chance_one = 1
            if total_value_one > 16:
                break 
        while user_draw:
            print(f'total score of your cards are:{total_value_two}')
            print(f'Do you want to draw? Y/N(dealer has:{player_one_cards[0].mark})')
            user_choice = input()
            if user_choice == 'Y':
                player_two.add_card(new_deck.draw())
                player_two_cards.append(player_two.remove())
                total_value_two += player_two_cards[-1].value
                if player_two_cards[-1].mark == 'Ace':
                    ace_player_two = 1
                if total_value_two > 21 and ace_player_two == 1 and ace_chance_two == 0:
                    total_value_two -= 10
                    ace_chance_two = 1
                if total_value_two > 21:
                    print('Busted')
                    player_two_balance.lost_bet(100)
                    user_draw = False
                    break
            if user_choice == 'N':
                user_draw = False
                break
        if total_value_one > 21 and total_value_two <= 21:
            print('dealer busted')
            player_two_balance.won_bet(100)
            user_draw = False
            break
        if total_value_one < total_value_two and total_value_one <= 21 and total_value_two <= 21:
            print('Player won')
            player_two_balance.won_bet(100)
            user_draw = False
            break
        if total_value_one > total_value_two and total_value_one <= 21 and total_value_two <= 21:
            print('Dealer won')
            player_two_balance.lost_bet(100)
            user_draw = False
            break
    print('Do you want to play another round? Y/N')
    user_choice_another_round = input()
    if user_choice_another_round == 'Y':
        game_on = True
    if user_choice_another_round == 'N':
        game_on = False
        break