#!/usr/bin/python3

# performing a coin flip

import random

def flipIt():
	flip = random.randrange (0,2)

	# check if heads or tails
	if flip == 0:
		print("tails")
	else:
		print("head")
for i in range (11):
	flipIt()
