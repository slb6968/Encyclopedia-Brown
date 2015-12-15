 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
"""Encyclopedia Brown, user reviews"""


import sys
import os
import datetime

locales = ['NYC', 'Paris', 'Bangkok', 'Sydney', 'Rio', 'Accra']

def print_locales(locales):
    i = 1
    for locale in locales:
        print i, " - ", locale
        i += 1
        
def add_review():
    print "To which locale does this review pertain? "
    print_locales(locales) 
    localenum = raw_input("Enter the number corresponding to your locale: ")
    locale = locales[int(localenum)-1]
    reviewer = raw_input("Please enter a user name: ")
    reviewdate = datetime.datetime.now()
    reviewsubject = raw_input("Enter the subject of this review: ")
    reviewtext = raw_input("You may now type your review: ")

    reviewdict = {locale: {locale+str(reviewdate)+reviewer:
                  (locale, reviewdate, reviewsubject, reviewtext, reviewer)}}
    with open('user_reviews.txt', 'a+') as f:
        f.write(str(reviewdict))
        f.close
