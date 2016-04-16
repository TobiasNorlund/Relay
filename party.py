import sys
from time import sleep
from random import randint
import relay_controller as relay

printOutDelay = 0.07
def write(text): sys.stdout.write(text)
def printOut(text):
	for c in text:
		write(c)
		sys.stdout.flush()
		sleep(printOutDelay)
	write("\n")

relay.init()

def partyInit():

	print ""
	printOut("INITIATING PARTY SEQUENCE...............")
	sleep(7)
	
	print ""
	print ""
	printOut("OK ......")
	sleep(1.5)
	print ""
	print ""
	
	# Turn on smoke :P
	relay.on(0)
	
	printOut("HERE WE GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO :D")
	print ""
	print ""
	
	sleep(10)
	
	# Okay that's fine!
	relay.off(0)
	
	sleep(2)
	
	printOut("LET'S PARTY!!!!")
	
try:

	if any(s == "-init" for s in sys.argv):
		partyInit()
	
	while(True):
		
		# Wait this long until next smoke epoch
		sleep(randint(30, 500))
	
		# Smoke!
		relay.on(0)
		sleep(randint(7,15))
		relay.off(0)
finally:
	print "Unexpected error, shutting down!"
	relay.off(0)
