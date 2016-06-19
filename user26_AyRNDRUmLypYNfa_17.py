# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


outcome2 = "Hit or stand?"

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        ans = ""
        for card in self.hand:
            ans = ans + str(card) + " "
        return "Hand contains " + ans	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)
        # add a card object to a hand     

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        ace = False
        for card in self.hand:  
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = True
        if ace == True and value + 10 <= 21:
            value += 10      
        return value
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        global player_hand, dealer_hand
        # draw a hand on the canvas, use the draw method for cards                 
        k = 0
        for card in self.hand:
            if k <= 4:                         
                card.draw(canvas, pos)
                pos[0] +=100 
                k += 1
        
        
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
                
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)   # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        dec = ""
        for deckcard in self.deck:
            dec = dec + str(deckcard) + " "	# return a string representing the deck
        return "Deck contains " + dec


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, outcome, outcome2, score
    if not in_play:
        outcome = ''
        outcome2 = "Hit or stand?"
        deck = Deck()
        deck.shuffle()
        dealer_hand = Hand()
        player_hand = Hand()
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        in_play = True
    else:
        outcome = "You lose."
        outcome2 = "New deal?"
        score -= 1
        in_play = False

def hit():
    global player_hand, outcome, in_play, score, outcome2
    if in_play:
        if player_hand.get_value() <= 21:           
            player_hand.add_card(deck.deal_card())
        else:
            outcome = "You went bust and lose."
            outcome2 = "New deal?"
            in_play = False
            score -= 1
     
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer_hand, outcome, in_play, score, outcome2
    if in_play:
        while dealer_hand.get_value() < 17:           
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21 and player_hand.get_value() <= 21:
            outcome = "You win."
            outcome2 = "New deal?"
            in_play = False
            score += 1
      
        elif player_hand.get_value() > 21:
            outcome = "You went bust and lose."
            outcome2 = "New deal?"
            in_play = False
            score -= 1
           
        elif player_hand.get_value() <= 21 and dealer_hand.get_value() <= 21:
            if player_hand.get_value() > dealer_hand.get_value():
                outcome = "You win."
                outcome2 = "New deal?"
                score += 1
                in_play = False
               
            elif player_hand.get_value() <= dealer_hand.get_value():
                outcome = "You lose."
                outcome2 = "New deal?"
                score -= 1
                in_play = False
                
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', (100, 80), 50, 'Blue')
    canvas.draw_text('Score ' + str(score), (400, 80), 30, 'Black')
    canvas.draw_text('Dealer', (80, 200), 30, 'Black')
    canvas.draw_text('Player', (80, 400), 30, 'Black')
    canvas.draw_text(outcome, (250, 200), 30, 'Black')
    canvas.draw_text(outcome2, (250, 400), 30, 'Black')
    player_hand.draw(canvas, [80, 430])
    dealer_hand.draw(canvas, [80, 230])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                          [80 + CARD_BACK_CENTER[0], 
                         230 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric