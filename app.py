import random

player_hand = []
opponent_hand = []
player_yellow_stack = [] 
player_blue_stack = [] 
player_white_stack = []
player_green_stack = []
player_red_stack = []
trade_yellow_stack = []
trade_blue_stack = []
trade_white_stack = []
trade_green_stack = []
trade_red_stack = []

trading_board = [trade_yellow_stack, trade_blue_stack, trade_white_stack,
                 trade_green_stack, trade_red_stack]

game_board = [player_yellow_stack, player_blue_stack, player_white_stack,
              player_green_stack, player_red_stack]
              
cards =  ['Yellow X', 'Yellow X', 'Yellow X', 'Yellow 2', 'Yellow 3', 'Yellow 4', 
          'Yellow 5', 'Yellow 6', 'Yellow 7', 'Yellow 8', 'Yellow 9', 'Yellow 10',
          'Blue X', 'Blue X', 'Blue X', 'Blue 2', 'Blue 3', 'Blue 4', 
          'Blue 5', 'Blue 6', 'Blue 7', 'Blue 8', 'Blue 9', 'Blue 10',
          'White X', 'White X', 'White X', 'White 2', 'White 3', 'White 4', 
          'White 5', 'White 6', 'White 7', 'White 8', 'White 9', 'White 10',
          'Green X', 'Green X', 'Green X', 'Green 2', 'Green 3', 'Green 4', 
          'Green 5', 'Green 6', 'Green 7', 'Green 8', 'Green 9', 'Green 10',
          'Red X', 'Red X', 'Red X', 'Red 2', 'Red 3', 'Red 4', 
          'Red 5', 'Red 6', 'Red 7', 'Red 8', 'Red 9', 'Red 10']

def deal_cards():
    for i in xrange(8):
        selection1 = random.choice(cards)
        player_hand.append(selection1)
        cards.remove(selection1)
        selection2 = random.choice(cards)
        opponent_hand.append(selection2)
        cards.remove(selection2)
        
def playing_card(player_hand):
    move_choice = raw_input('Would you like to play or trade a card? (Type "play" or "trade") ')
    if move_choice == 'play':
        chosen_card = raw_input('Which card would you like to play? ')
        while chosen_card not in player_hand:
            print 'Please choose a card in your hand.'
            chosen_card = raw_input('Which card would you like to play? ')
        else:
            append_player_stack(chosen_card)
    if move_choice == 'trade':
        trade_card = raw_input('Which card would you like to trade away? ')
        while trade_card not in player_hand:
            print 'Please choose a card in your hand.'
            trade_card = raw_input('Which card would you like to trade away? ')
        else:
            player_hand.remove(trade_card)
            append_trade_stack(trade_card)
            

def append_trade_stack(trade_card):
    if 'Yellow' in trade_card:
        trade_yellow_stack.append(trade_card)
    if 'Blue' in trade_card:
        trade_blue_stack.append(trade_card)
    if 'White' in trade_card:
        trade_white_stack.append(trade_card)
    if 'Green' in trade_card:
        trade_green_stack.append(trade_card)
    if 'Red' in trade_card:
        trade_red_stack.append(trade_card)

def append_player_stack(chosen_card):
    if 'Yellow' in chosen_card:
        if player_yellow_stack != []:
            color, number = player_yellow_stack[-1].split(' ')
            color2, number2 = chosen_card.split(' ')
            if number >= number2 and number != 'X':
                print 'Unacceptable move. Please try again.'
            else:
                player_yellow_stack.append(chosen_card)
                player_hand.remove(chosen_card)
        else:
            player_yellow_stack.append(chosen_card)
            player_hand.remove(chosen_card)
    if 'Blue' in chosen_card:
        if player_blue_stack != []:
            color, number = player_blue_stack[-1].split(' ')
            color2, number2 = chosen_card.split(' ')
            if number >= number2 and number != 'X':
                print 'Unacceptable move. Please try again.'
            else:
                player_blue_stack.append(chosen_card)
                player_hand.remove(chosen_card)
        else:
            player_blue_stack.append(chosen_card)
            player_hand.remove(chosen_card)
    if 'White' in chosen_card:
        if player_white_stack != []:
            color, number = player_white_stack[-1].split(' ')
            color2, number2 = chosen_card.split(' ')
            if number >= number2 and number != 'X':
                print 'Unacceptable move. Please try again.'
            else:
                player_white_stack.append(chosen_card)
                player_hand.remove(chosen_card)
        else:
            player_white_stack.append(chosen_card)
            player_hand.remove(chosen_card)
    if 'Green' in chosen_card:
        if player_green_stack != []:
            color, number = player_green_stack[-1].split(' ')
            color2, number2 = chosen_card.split(' ')
            if number >= number2 and number != 'X':
                print 'Unacceptable move. Please try again.'
            else:
                player_green_stack.append(chosen_card)
                player_hand.remove(chosen_card)
        else:
            player_green_stack.append(chosen_card)
            player_hand.remove(chosen_card)
    if 'Red' in chosen_card:
        if player_red_stack != []:
            color, number = player_red_stack[-1].split(' ')
            color2, number2 = chosen_card.split(' ')
            if number >= number2 and number != 'X':
                print 'Unacceptable move. Please try again.'
            else:
                player_red_stack.append(chosen_card)
                player_hand.remove(chosen_card)
        else:
            player_red_stack.append(chosen_card)
            player_hand.remove(chosen_card)

def draw_card(player_hand):
    while len(player_hand) < 8:
        if trading_board != [[],[],[],[],[]]:
            trading = raw_input('Would you like to pick a card from the middle (yes or no)? ')
            if trading == 'yes':
                pickup_color = raw_input('Which color would you like? ')
                desired_stack = determine_stack(pickup_color)
                while not desired_stack:
                    print 'Please choose a card in the middle.'
                    pickup_color = raw_input('Which color would you like? ')
                else:
                    pickup_card = desired_stack[-1]
                    player_hand.append(pickup_card)
                    desired_stack.remove(pickup_card)
        if trading_board == [[],[],[],[],[]] or trading == 'no':
            selection = random.choice(cards)
            player_hand.append(selection)
        
def determine_stack(pickup_color):
    if 'Yellow' in pickup_color:
        desired_stack = trade_yellow_stack
    if 'Blue' in pickup_color:
        desired_stack = trade_blue_stack
    if 'White' in pickup_color:
        desired_stack = trade_white_stack
    if 'Green' in pickup_color:
        desired_stack = trade_green_stack
    if 'Red' in pickup_color:
        desired_stack = trade_red_stack
    return desired_stack
    
def show_board(trading_board, game_board):
    print 'Trade: {}'.format(trading_board)
    print 'Game board: {}'.format(game_board)
    
print 'Welcome to Lost Cities'
deal_cards()
while len(cards) > 0:
    print 'Here is your hand: {}'.format(player_hand)
    show_board(trading_board, game_board)
    playing_card(player_hand)
    draw_card(player_hand)
    print
    print '-' * 100
    print

show_board(trading_board, game_board)
