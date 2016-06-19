# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random


# initialize global variables used in your code
num_range = 100
num_guess = 7
secret_num = random.randrange(0, 100)

# helper function to start and restart the game
def new_game():
    global num_range, num_guess, secret_num
    if num_range == 100:
        num_guess = 7
    elif num_range == 1000:
        num_guess = 10
    secret_num = random.randrange(0, num_range)
    print "New game.","Range is from 0 to", num_range
    print "Number of remaining guesses is", num_guess
    print ""
    input_guess
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, num_guess, secret_num
    num_range = 100
    num_guess = 7
    print "New game.","Range is from 0 to", 100
    print "Number of remaining guesses is", 7
    print ""
    secret_num = random.randrange(0, 100)
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, num_guess, secret_num
    num_range = 1000
    num_guess = 10
    print "New game.","Range is from 0 to", 1000
    print "Number of remaining guesses is", 10
    print ""
    secret_num = random.randrange(0, 1000)
 
    
def input_guess(guess):
    # main game logic goes here	
    global num_guess, secret_num
    guess_num = int(guess)
    print "Guess was", guess
    num_guess = num_guess - 1
    if num_guess == 0 and guess_num == secret_num:
        print "Number of remaing guesses is", num_guess
        print "Correct!"
        print ""
        new_game()
    elif num_guess == 0 and guess_num != secret_num:
        print "Number of remaing guesses is", num_guess
        print "You ran out of guesses.""The number was", secret_num
        print ""
        new_game()
    else:
        print "Number of remaing guesses is", num_guess
        if guess_num > secret_num:
            print "Lower!"
            print ""
        elif guess_num < secret_num:
            print "Higher!"
            print ""
        elif guess_num == secret_num:
            print "Correct!"
            print ""
            new_game()
        else: 
            print "error"
            print ""
    

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game()
f.start()


# always remember to check your completed program against the grading rubric
