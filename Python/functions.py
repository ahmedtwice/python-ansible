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
# varible nubmer of parameters
def mulitAdd(*args):
    result = 0
    for x in args:
        result += x
    return result

# call functions
#func1()
#print(func1())
#print(func1)

#addNums (5, 6)
#addNums(val2 = 11, val1 = 9)


#print(cube(5))

#power(6,6)
#power(6,2)
#power(6)

print(mulitAdd(5,6,9,15,9))
print(mulitAdd())
print(mulitAdd(5,45,2,65,5,45,21,854,24,85,2185,485,254,85,2,58,524,584,2,185,2,8,24,8,452,485,25))
