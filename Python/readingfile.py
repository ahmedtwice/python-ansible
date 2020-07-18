#!/usr/bin/python3

# Script to read a file

#easy reading of file
testFile = open("testfile.txt", "r" )
print(testFile.read())
testFile.close()

# read file line by line
testFile = open("testfile.txt", "r")
for line in testFile:
    if line.startswith("A"):
        print(line)
testFile.close()

# Read file using  with statement
with open("testfile.txt", "r") as testFile:
    print(testFile.read())


