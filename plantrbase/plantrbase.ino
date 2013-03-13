/*
This is for receiving data from the Xbee module and printing it out
to be interpreted by the python listener
*/

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
}

void loop() {
  // see if there's incoming serial data:
  int INLENGTH = 22;
  char msg[INLENGTH]; 
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    int stat = Serial.readBytesUntil('\n', msg, sizeof(msg));
    String output = String(msg);
    Serial.println(output);
  }
}
