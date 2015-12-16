#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Encyclopedia Brown, a traveler's resource"""

import random
import reviews
import travelhangman

def printEBmenu():
    """prints the main menu."""
    EBmenu = ['Add a new review',
              'Search and read reviews',
              'Search locale information',
              'Play EB\'s Travel Hangman',
              'Feeling Lucky?',
              'Exit?']
    i = 1
    print '-' * 55
    for item in EBmenu:
        print i, " - ", item
        i += 1
    print '-' * 55, '\n'


print ' ' * 18, 'WELCOME TO ENCYCLOPEDIA BROWN'
print 'a resource for world travelers to learn, explore, and communicate'
print '_' * 65, '\n'

exit = False
while not exit:
    printEBmenu()
    choice = raw_input('What would you like to do? ')
    if choice == '1':
        reviews.add_review()
    elif choice == '2':
        reviews.search_reviews()
    elif choice == '3':
        reviews.search_locales()
    elif choice == '4':
        travelhangman.go_play_hm()
    elif choice == '5':
        print '\nENCYCLOPEDIA BROWN\'s magic 8 ball says you should travel to:'
        print '\n{0} in {1}\n'.format(random.choice(reviews.LOCALES).upper(),
                          random.randint(2016, 2046))
    elif choice == '6':
        exit = True
        print 'Thanks for checking out Encyclopedia Brown!'
