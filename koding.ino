int buzzer = 7;
void setup() {
  pinMode(buzzer,OUTPUT);
}

void loop() {
int H = Serial.read();
Serial.print (H);
tone(buzzer,H);
}


