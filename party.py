import sys
from time import sleep
import relay_controller as relay

relay.init()

print ""
sys.stdout.write(" INITIATING PARTY SEQUENCE")
sleep(2)
for i in range(20):
    sys.stdout.write(".")
    sleep(0.4)

print ""
print ""
sys.stdout.write(" OK ")
sleep(1)
sys.stdout.write("..")
sleep(1.5)
sys.stdout.write(" HERE WE GO")

# Turn on smoke :P
relay.on(1)

for i in range(15):
    sys.stdout.write("O")
    sleep(0.2)

sys.stdout.write("!")

sleep(5000)

print ""
print "Is that enough??"

sleep(2000)

print "No, don't think soo ... ;)"

# Okay that's fine!
relay.off(1)