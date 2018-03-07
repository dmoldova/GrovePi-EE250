import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
#sys.path.append('../../Software/Python/')



#import sys
import socket
#sys.path.append('../../Software/Python/')

import time
#from grovepi import *

#from grovepi import *

def Main():
    #host = '10.0.2.15'
    port = 9006
    server_addr = '192.168.1.112'

    s = socket.socket()
    s.connect((server_addr,port))

    message = input("->")

    while message != 'q':
        s.send(message.encode('utf-8'))
        #s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        #execfile('../../Software/Python/grove_led_blink.py')
        #data = c.recv(1024).decode('utf-8')
        print("Received from server: " + data)
        message = input("->")
    s.close()

if __name__ == '__main__':
    Main()
