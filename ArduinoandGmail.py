#! /usr/bin/env python
# Code by Mike Hord and Paul Subzak
# Gmail and Arduino
# Twin Cites Maker, Minneapolis, MN

#uses Python 2
#uses Arduino 1.0

import serial
import time
import imaplib
import re
import string

# interval change for less often 
INTERVAL = 1 # check every INTERVAL minutes

last_check = time.time() - INTERVAL*60 # subtract so that we check first time

#change between the ticks your serial link on arduino
s = serial.Serial('/dev/tty.usbserial-A6008dvx', 9600)

time.sleep(1.5)
s.write('L')
IMAP_SERVER='imap.gmail.com'
IMAP_PORT=993
M = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

#insert username then password
rc, resp = M.login('USERNAME', 'PASSWORD')
print rc, resp

# main loop
while True:
        if time.time() - last_check < INTERVAL*5:
            continue
        last_check = time.time()

        status_string = M.status('INBOX', '(UNSEEN)')[1]
        print status_string[0]
        p = re.compile('\d+')
        unread_count = string.atoi(p.findall(status_string[0])[0],10)
        print unread_count
        if unread_count > 0:
            s.write('H')
        else:
            s.write('L')
