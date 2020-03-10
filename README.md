# Arduino Gmail LED
Turn on a LED using Gmail and Arduino

Arduino with Gmail

The basics were getting Arduino to talk to Gmail and then turn on a LED.

Step one: Load you Arduino with PhysicalPixel. It's under examples, Communication.
Step two: Install Python and Pyserial
Step three download the ArduinoandGmail.py code
Step Four: Edit the Python Code.

You will need to edit two things:
s = serial.Serial('/dev/tty.usbserial-A6008dvx', 9600)

Between the first tick marks enter your serial connection, you can find this by going to the Arduino IDE and then Tools, Serial Port, what is checked is what goes between the tick marks.
#inser username then password
rc, resp = M.login('USERNAME', 'PASSWORD')
print rc, resp
Enter you username and password.

Step Five: Run the python script and you should be good to go, the python will send letter 'H' when you have 1 or more unseen emails and 'L' when you have 0.
Step Six: hook up a LED and Resistor to Pin 13, or hook something else up that you want to turn on.
Step Seven: Get the LED to turn off
