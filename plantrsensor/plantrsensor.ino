/* This is for reading values
from moisture and light sensor, and
transmitting via Xbee to the PC-connected base
*/

int lightPin = 0;
int sensorValue = 0;
int moisturePin = 1;
int powerPin = 2;
int moistureValue;
String id = String("SeVPHfSsZBo");

void setup() {
  pinMode(powerPin, OUTPUT);
  digitalWrite(powerPin, HIGH);
  Serial.begin(9600);
}

void loop() {
  // Read and store light value in string
  sensorValue = analogRead(lightPin);
  String light = String(int(sensorValue));
  
  // Read and store moisture value in string
  moistureValue = analogRead(moisturePin);
  String moisture = String(int(moistureValue));
  
  Serial.println(String("i"+id+"l"+light+"m"+moisture));
  delay(2000);
}
