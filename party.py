import sys
from time import sleep
import relay_controller as relay

relay.init()

print ""
print(" INITIATING PARTY SEQUENCE")
sleep(1)

print ""
print ""
print(" OK ")
sleep(1)
print("..")
sleep(1.5)
print(" HERE WE GO")

# Turn on smoke :P
relay.on(0)

sleep(1)

print ""
print "Is that enough??"

sleep(1)

print "No, don't think soo ... ;)"

# Okay that's fine!
relay.off(0)

print "Okay, lets party!"