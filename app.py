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
              
cards =  ['YellowX', 'YellowX', 'YellowX', 'Yellow2', 'Yellow3', 'Yellow4', 
          'Yellow5', 'Yellow6', 'Yellow7', 'Yellow8', 'Yellow9', 'Yellow10',
          'BlueX', 'BlueX', 'BlueX', 'Blue2', 'Blue3', 'Blue4', 
          'Blue5', 'Blue6', 'Blue7', 'Blue8', 'Blue9', 'Blue10',
          'WhiteX', 'WhiteX', 'WhiteX', 'White2', 'White3', 'White4', 
          'White5', 'White6', 'White7', 'White8', 'White9', 'White10',
          'GreenX', 'GreenX', 'GreenX', 'Green2', 'Green3', 'Green4', 
          'Green5', 'Green6', 'Green7', 'Green8', 'Green9', 'Green10',
          'RedX', 'RedX', 'RedX', 'Red2', 'Red3', 'Red4', 
          'Red5', 'Red6', 'Red7', 'Red8', 'Red9', 'Red10']

def deal_cards():
    for i in xrange(8):
        selection1 = random.choice(cards)
        player_hand.append(selection1)
        cards.remove(selection1)
        selection2 = random.choice(cards)
        opponent_hand.append(selection2)
        cards.remove(selection2)
        
def playing_card(player_hand):
    chosen_card = raw_input('Which card would you like to play? ')
    while chosen_card not in player_hand:
        print 'Please choose a card in your hand.'
        chosen_card = raw_input('Which card would you like to play? ')
    else:
        player_hand.remove(chosen_card)
        append_player_stack(chosen_card)

def append_player_stack(chosen_card):
    if 'Yellow' in chosen_card:
        player_yellow_stack.append(chosen_card)
    if 'Blue' in chosen_card:
        player_blue_stack.append(chosen_card)
    if 'White' in chosen_card:
        player_white_stack.append(chosen_card)
    if 'Green' in chosen_card:
        player_green_stack.append(chosen_card)
    if 'Red' in chosen_card:
        player_red_stack.append(chosen_card)

def draw_card(player_hand):
    while len(player_hand) < 8:
        if trading_board != [[],[],[],[],[]]:
            trading = raw_input('Would you like to pick a card from the middle (yes or no)? ')
            if trading == 'yes':
                pickup_card = raw_input('Which card would you like? ')
                desired_stack = determine_stack(pickup_card)
                while pickup_card not in desired_stack:
                    print 'Please choose a card in the middle.'
                    pickup_card = raw_input('Which card would you like? ')
                else:
                    player_hand.append(pickup_card)
                    desired_stack.remove(pickup_card)
            else:
                selection = random.choice(cards)
                player_hand.append(selection)
        else:
            selection = random.choice(cards)
            player_hand.append(selection)
        
def determine_stack(pickup_card):
    if 'Yellow' in pickup_card:
        desired_stack = trade_yellow_stack
    if 'Blue' in pickup_card:
        desired_stack = trade_blue_stack
    if 'White' in pickup_card:
        desired_stack = trade_white_stack
    if 'Green' in pickup_card:
        desired_stack = trade_green_stack
    if 'Red' in pickup_card:
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