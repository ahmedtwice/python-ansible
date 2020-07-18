#!/usr/bin/python3

# Basic function

def func1():
    print("somehting func-y")
# Function that takes an arguement
def addNums(val1, val2):
    print(val1 + val2)
# function that returns a value
def cube(x):
    return x * x * x

# function with default value
def power(num, power=2):
    result = 1
    for i in range(power):
        result = result * num
    print(result)


# call functions
#func1()
#print(func1())
#print(func1)

#addNums (5, 6)
#addNums(val2 = 11, val1 = 9)


#print(cube(5))

power(6,6)
power(6,2)
power(6)
