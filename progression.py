"""
km - Kilometer
m - mile

Q1. A taxi charges 15$ for the first mile/kilometer and after the 1st m/km, the taxi charges 8$ per each m/km

This code would help you solve this question 
"""

s = int(input("How many kilometers/miles : ")) # Getting an integer input
a = 15; # declaring values for the first km/m
b = 8; # declaring values for the seconds km/m
c = s-1 # getting out the first km/m for 15$
print(c*b+a) # calculating the price
