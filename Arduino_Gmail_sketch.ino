//Arduino Uno
// Code to run the Arduino
//LED should be conndected to digital pin out 12
//intial code sketch from 
//http://j4mie.org/blog/how-to-make-a-physical-gmail-notifier/


int outPin = 12; // Output connected to digital pin 12
int mail = LOW; // Is there new mail?, start low
int val; // Value read from the serial port

//Setup pyserial communticaion
void setup()
{
    pinMode(outPin, OUTPUT); // sets the digital pin as output
    Serial.begin(9600);
    Serial.flush();
}

//Main loop
//When the serial port is available use the value sent to change the color of an LED
//hooked up to digital output #12

void loop()
{
    // Read from serial port
    if (Serial.available())
    {
        val = Serial.read();
        Serial.println(val);
        if (val == 'M') mail = HIGH;
        else if (val == 'N') mail = LOW;
    }

    // Set the status of the output pin
    digitalWrite(outPin, mail);
}
