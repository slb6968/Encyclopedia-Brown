 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
"""Encyclopedia Brown, user reviews"""


import sys
import os
import datetime
import pickle
import csv
import pprint


LOCALES = ['NYC', 'Paris', 'Bangkok', 'Sydney', 'Rio', 'Accra']


def initialize_reviewdict():
    """initializes the text file to an empty dictionary."""
    i = 1
    reviewdict = {}
    for locale in LOCALES:
        reviewdict[locale] = {}
    with open('reviews.txt', 'ab') as f:
        pickle.dump(reviewdict, f)
        f.close

def print_locales(locales):
    """prints the list of locations, along with a number."""
    i = 1
    for locale in locales:
        print i, " - ", locale
        i += 1

def get_locale():
    """Asks the user to select a locale, and returns the locale."""
    print_locales(LOCALES) 
    localenum = raw_input("Enter the number corresponding to your locale: ")
    locale = LOCALES[int(localenum)-1]
    return locale

def add_review():
    """Adds a user-created review to the reviews.txt file."""
    with open('reviews.txt', 'rb') as f:
        reviewdict = pickle.load(f)
        f.close
    print "To which locale does this review pertain? "
    locale = get_locale()
    reviewer = raw_input("Please enter a user name: ")
    reviewdate = datetime.datetime.now()
    reviewsubject = raw_input("Enter the subject of this review: ")
    reviewtext = raw_input("You may now type your review: ")
    reviewdict[locale][locale+str(reviewdate)+reviewer] = [locale,
                                                           reviewdate,
                                                           reviewsubject,
                                                           reviewtext,
                                                           reviewer]
    with open('reviews.txt', 'wb') as f:
        pickle.dump(reviewdict, f)
        f.close

# 'Search and read reviews'

def search_reviews():
    """Allows a user to search for reviews from a specific locale."""
    print "To which locale does this review pertain? "
    locale = get_locale()
    with open("reviews.txt", 'rb') as f:
        reviewdict = pickle.load(f)
        f.close
    count = 0
    print 'Search Results for {}: \n'.format(locale)
    for key, value in reviewdict.iteritems():
        if key == locale:
            for innerkey, innerlist in value.items():
                count += 1
                print '{} - {} added by {} on {}'.format(count,
                                                            value[innerkey][2],
                                                            value[innerkey][4],
                                                            value[innerkey][1])
                print value[innerkey][3], '\n'

# 'Search locale information'

"""These are the fields in the CSV file:
CITY,COUNTRY,REGION,COMPARATIVE AREA,CLIMATE,LANGUAGES,RELIGIONS,POPULATION,
TIME ZONE,CURRENCY,CURRENCY - PER USD, FLIGHTS , HOTELS , MEALS + INCIDENTALS"""

def search_locales():
    """Allows a user to search for information about a specific locale."""
    locale = get_locale()
    print '     \nHere\'s some information about {}.\n'.format(locale)
    f = csv.DictReader(open("cities.txt"))
    for row in f:
        if row['CITY'] == locale:
            pprint.pprint(row)
            print ' . . . '
            break
    print '     \nFor more information, visit the CIA WorldFactbook site.\n'
