import random
from math import *
import time

lam=0.9 #Arrival Rate
mu=1 #service rate

n=0 #number of clients serviced
t=0 #overall system time
ta=0 #arrival time
ts=0 #service time
q=0 #queue length
w=[] #array of wait times

def generateArr():
	ua=random.uniform(0, 1)
	arr= log(1-ua)/(-lam)
	return arr

def generateServ():
	us=random.uniform(0, 1)
	serv= log(1-us)/(-mu)
	return serv

ta=generateArr()
ts=generateServ()

while n<1000:
	if q==0:
		t=t+ta
		q=1
		ta=generateArr()
	else:
		if ts<ta:
			t=t+ts
			q=q-1
			ta=ta-ts
			ts=generateServ()
			n+=1
		else:
			t=t+ta
			q=q+1
			ts=ts-ta
			ta=generateArr()
	print("%d  %f  %d" %(n,t,q))




		


