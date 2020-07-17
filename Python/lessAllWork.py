#!//usr/bin/python3

import time
import random

def WriteChars(setence):
	for i in list(sentence):
	  print(i,end="", flush= True)
	  time.sleep(random.uniform(0, 0.4))
	print()
while True:
	WriteChars("All work and no play makes Jack a dull boy.")
