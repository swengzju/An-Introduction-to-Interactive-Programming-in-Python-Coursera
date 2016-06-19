# implementation of card game - Memory

import simplegui
import random

cards = range(8)+range(8)
random.shuffle(cards)
exposed = [False, False, False, False, False, False, False, False, False,
           False, False, False, False, False, False, False]
counter = 0
# helper function to initialize globals
def new_game():
    global state, counter, cards, exposed
    counter = 0
    state = 0 
    cards = range(8)+range(8)
    random.shuffle(cards)
    exposed = [False, False, False, False, False, False, False, False, False,
               False, False, False, False, False, False, False]
    label.set_text('Turns = ' + str(counter))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, j, k, counter
    if state == 0:
        j = pos[0] // 50
        if exposed[j]:
            return
        exposed[j] = True
        state = 1
    elif state == 1:
        k = pos[0] // 50
        if exposed[k]:
            return
        exposed[k] = True
        state = 2
        counter +=1
        label.set_text('Turns = ' + str(counter))
    else:
        if cards[j] != cards[k]:
            exposed[j] = False
            exposed[k] = False
            j = pos[0] // 50
            if exposed[j]:
                return
            exposed[j] = True
            state = 1
        else:
            j = pos[0] // 50
            if exposed[j]:
                return
            exposed[j] = True
            state = 1 
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0    
    for n in cards:
        if exposed[i] == False:
            canvas.draw_line((25+50*i, 0), (25+50*i, 100), 48, 'Green')
        elif exposed[i] == True:
            canvas.draw_text(str(n), (15 + 50 * i, 65), 40, 'White')
        i +=1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
