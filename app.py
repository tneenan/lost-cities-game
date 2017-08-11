import random
from variables import *
from players import Player

def deal_cards():
    for i in xrange(8):
        selection1 = random.choice(cards)
        player_hand.append(selection1)
        cards.remove(selection1)
        selection2 = random.choice(cards)
        opponent_hand.append(selection2)
        cards.remove(selection2)

def computer_play_card(opponent_hand):
    move_choice = random.randint(0,2)
    tries = 0
    if move_choice == 1: # <- computer is trading
        trade_card = random.choice(opponent_hand)
        append_trade_stack(trade_card)
        opponent_hand.remove(trade_card)
    else: # <- computer is playing
        chosen_card = random.choice(opponent_hand)
        failure = append_player_stack(chosen_card, 'opponent')
        while failure == True:
            if tries < 6:
                chosen_card = random.choice(opponent_hand)
                failure = append_player_stack(chosen_card, 'opponent')
            else:
                trade_card = random.choice(opponent_hand)
                append_trade_stack(trade_card)
                opponent_hand.remove(trade_card)
                failure = False
        
def append_trade_stack(trade_card):
    color, number = trade_card.split(' ')
    if color in colors:
        color_stack = 'trade_{}_stack'.format(color.lower())
        trade_stack = eval(color_stack)
        trade_stack.append(trade_card)

def append_player_stack(chosen_card, player_or_opponent):
    color, number = chosen_card.split(' ')
    chosen_card_number = int(number)
    whose_hand = '{}_hand'.format(player_or_opponent)
    hand = eval(whose_hand)
    if color in colors:
        color_stack = '{}_{}_stack'.format(player_or_opponent, color.lower())
        player_stack = eval(color_stack)
        if player_stack != []:
            color2, number2 = player_stack[-1].split(' ')
            player_stack_number = int(number2)
            if player_stack_number > chosen_card_number:
                if player_or_opponent == 'opponent': return True
                else: print 'Unacceptable move. Please try again.'
            else:
                player_stack.append(chosen_card)
                hand.remove(chosen_card)
        else:
            player_stack.append(chosen_card)
            hand.remove(chosen_card)

def computer_draw_card(opponent_hand):
    move_choice = random.randint(0,1)
    if move_choice == 0 and trading_board != [[],[],[],[],[]]:
        pickup_color = random.choice(colors)
        desired_stack = determine_stack(pickup_color)
        while not desired_stack:
            pickup_color = random.choice(colors)
            desired_stack = determine_stack(pickup_color)
        else:
            pickup_card = desired_stack[-1]
            opponent_hand.append(pickup_card)
            desired_stack.remove(pickup_card)
    else:
        selection = random.choice(cards)
        opponent_hand.append(selection)
        cards.remove(selection)
        
def determine_stack(pickup_color):
    if pickup_color in colors:
        color_stack = 'trade_{}_stack'.format(pickup_color.lower())
        desired_stack = eval(color_stack)
        return desired_stack
    else: return nil
    
def show_board(opponent_board, trading_board, game_board):
    print
    print 'Cards left: {}'.format(len(cards))
    print
    print "Opponent's board: {}".format(opponent_board)
    print
    print 'Trade: {}'.format(trading_board)
    print
    print 'Your board: {}'.format(game_board)
    print
    
print 'Welcome to Lost Cities'
deal_cards()
first_player = Player(player_hand)
while len(cards) > 0:
    print 'Here is your hand: {}'.format(player_hand)
    show_board(opponent_board, trading_board, game_board)
    first_player.playing_card()
    first_player.draw_card()
    computer_play_card(opponent_hand)
    computer_draw_card(opponent_hand)
    print
    print '-' * 100
    print
