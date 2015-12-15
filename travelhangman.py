 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
"""Encyclopedia Brown, the hangman game"""


import random

wrtr = "\n Escape the tree!"
wr1 = "\n   O"
wr2 = "\n   |"
wr3 = "\n  \|"
wr4 = "\n  \|/"
wr5 = "\n _/"
wr6 = "\n _/ \_"
wrgr = "\n Land on your feet"

HMIMAGES = [wrtr+wrgr, wrtr+wr1+wrgr, wrtr+wr1+wr2+wrgr, wrtr+wr1+wr3+wrgr,\
            wrtr+wr1+wr4+wrgr, wrtr+wr1+wr4+wr5+wrgr, wrtr+wr1+wr4+wr6+wrgr]

travelwds = 'wayfarer cosmopolitan sojourn gallivant traipse \
            globetrotter peregrinate wanderlust'.split()

def pick_travel_word(wordlist):
    """Picks a random word from a list of words."""
    return wordlist[random.randint(0, len(wordlist)-1)]

def print_HM_game(HMIMAGES, hmword, missedltrs, rightltrs):
    """Prints game board."""
    try: 
        print HMIMAGES[len(missedltrs)]
    except IndexError:
        print 'GAME OVER - too many guesses.'
    print '\n'
    print 'Missed letters: '
    for letter in missedltrs:
        print letter
    blanks = '_' * len(hmword)
    print '\nYour secret travel word has {0} letters: '.format(len(hmword))

    for i in range(len(hmword)): # replace blanks with correct guesses
        if hmword[i] in rightltrs:
            blanks = blanks[:i] + hmword[i] + blanks[i+1:]
    print blanks

def get_ltr(alreadyentered):
    """Ensures that a single letter is entered, and returns that letter."""
    print '\n / - - - - - - - - - - - - - - - - - - - - - - - - - \ '
    while True:
        print 'What\'s your guess? '
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyentered:
            print('Pay Attention! You already entered that letter. Try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER (a-z OR A-Z).')
        else:
            return guess
                    
def playAgain():
    """Returns True if the player wants to play again, else it returns False."""
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')


def go_play_hm():
    """Game play for Hangman."""
    print('ENCYCLOPEDIA BROWN\'S TRAVEL HANGMAN')
    missedltrs = ''
    rightltrs = ''
    hmword = pick_travel_word(travelwds)
    finished = False

    while True:
        print_HM_game(HMIMAGES, hmword, missedltrs, rightltrs)
        guess = get_ltr(missedltrs + rightltrs)
        if guess in hmword:
            rightltrs = rightltrs + guess
            foundAllLetters = True
            for i in range(len(hmword)):
                if hmword[i] not in rightltrs:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print 'You guessed the secret travel word of ',  hmword, '!'
                finished = True
        else:
            missedltrs = missedltrs + guess
            if len(missedltrs) == len(HMIMAGES) - 1:
                print_HM_game(HMIMAGES, missedltrs, rightltrs, hmword)
                print 'You have run out of guesses!\nThe word was ', hmword
                finished = True
        if finished:
            if playAgain():
                missedltrs = ''
                rightltrs = ''
                finished = False
                hmword = pick_travel_word(travelwds)
            else:
                break

