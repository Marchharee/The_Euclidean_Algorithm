#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:16:46 2025

@author: Marchhare
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:42:26 2025

@author: Marchhare
"""

class EuclideanAlgorithm:
    
#Encapsulation of the Euclidean algorithm for GCD calculation.

    def calculate_gcd(self, a, b):
        
#Calculate the GCD of two positive integers using the Euclidean algorithm（a is the first input integer,b is the second one)
       
        while b != 0:#the loop should be continue until b=0
            new_b = b#save the b so that it can be calculate again
            b = a % b#get a remainder
            a = new_b#let the a be the formal b
        return a#return to the GCD of a and b

def the_answer():

#let the user to input the value
    a = int(input("Please enter the first positive integer: "))
    b = int(input("Please enter the second positive integer: "))

    if a <= 0 or b <= 0:#make sure a and b be the positive integer
        print("Error: Both numbers must be positive integers.")
        return

    answer = EuclideanAlgorithm()#use the main function
    gcd = answer.calculate_gcd(a, b)
    print(f"The GCD of {a} and {b} is: {gcd}")