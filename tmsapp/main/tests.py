from django.test import TestCase

import random

colors = ['black','red','yellow','green']

while True:
    mybuddy = input("My buddy ?")
    ran = random.randint(0,len(colors)-1)
    color = colors[ran]
    print(color)