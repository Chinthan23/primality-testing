#!/usr/bin/python3
import math
def Primality(x):
	if(x<=1):
		return False
	for i in range(2,math.sqrt(x)+1):
		if x%i==0:
			return False

	return True
