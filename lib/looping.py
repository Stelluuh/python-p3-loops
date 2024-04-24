#!/usr/bin/env python3

# Write a function happy_new_year() using a while loop that outputs numbers starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1

    print("Happy New Year!")

# Write a function square_integers() that takes one argument, a list of integers and returns the list of squared elements.
def square_integers(int_list):
    squared_number = [ i ** 2 for i in int_list]
    return squared_number

def fizzbuzz():
    # code goes here!
    pass
