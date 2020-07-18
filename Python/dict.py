#!/usr/bin/python3

#create dicttionary object
eng2esp = { "one": "uno", "two" : "dos", "three" : "tres"  }

print(eng2esp)

#view elements
print(eng2esp["one"])
print(eng2esp["three"])

#add and remove items from dictionary
eng2esp.update({"four":"cuatro", "five":"cinco"})
eng2esp.pop("two")
print(eng2esp)

