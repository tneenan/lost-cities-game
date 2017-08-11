from variables import *

class Player():
    def __init__(self, player_hand):
        self.hand = player_hand
    
    def playing_card(self):
        move_choice = raw_input('Would you like to play or trade a card? (Type "play" or "trade") ')
        if move_choice == 'play':
            chosen_card = raw_input('Which card would you like to play? ')
            while chosen_card not in self.hand:
                print 'Please choose a card in your hand.'
                chosen_card = raw_input('Which card would you like to play? ')
            else:
                append_player_stack(chosen_card, 'player')
        if move_choice == 'trade':
            trade_card = raw_input('Which card would you like to trade away? ')
            while trade_card not in self.hand:
                print 'Please choose a card in your hand.'
                trade_card = raw_input('Which card would you like to trade away? ')
            else:
                self.hand.remove(trade_card)
                append_trade_stack(trade_card)
    
    def draw_card(self):
        while len(self.hand) < 8:
            trading = raw_input('Would you like to pick a card from the middle (yes or no)? ')
            if trading_board == [[], [], [], [], []] or trading == 'no':
                selection = random.choice(cards)
                self.hand.append(selection)
                cards.remove(selection)
            if trading_board != [[], [], [], [], []] and trading == 'yes':
                    pickup_color = raw_input('Which color would you like? ')
                    desired_stack = determine_stack(pickup_color)
                    while not desired_stack:
                        print 'Please choose a card in the middle.'
                        pickup_color = raw_input('Which color would you like? ')
                        desired_stack = determine_stack(pickup_color)
                    else:
                        pickup_card = desired_stack[-1]
                        self.hand.append(pickup_card)
                        desired_stack.remove(pickup_card)
    