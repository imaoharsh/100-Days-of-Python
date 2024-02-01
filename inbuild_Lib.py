
print("Math Library")
import math

x=30.6

print(math.trunc(x))

x=90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))

print('-'*40)

import random
print("Random Library")

#random.seed(40)

print(random.random())
print(random.randint(1,11))
print(random.sample([1,2,3,4,5,6],2))       #create a random list of length 2.

from collections import Counter,defaultdict

lst1=[1,2,3,3,3,4,4,5,6,6]

print(Counter(lst1))                  #return a dict with present integer as key and their count.

d=defaultdict(int)             # Default dict of integer type.

print(d)

import string

print(string.ascii_letters)

