import math
from selenium import webdriver
import sys
# print(math.ceil(3.7))

# print(sys.path)

list_1 = [2, 4, 5]
iterator = iter(list_1)
print(next(iterator))

test = -0.00
print(math.exp(test)) 

# print(math.inf)

def outer():

    message = 'Hello'
    def inner():
        nonlocal message
        message = 'World'
        
        print("Inner ", message)
    
    inner()
    print("Outer ", message)

outer() 