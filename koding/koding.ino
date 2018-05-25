
#define ACTIVATED LOW
char H,offse;
unsigned long t;
int buzzer = 7;
void setup() {
  Serial.begin(9600);
  pinMode(buzzer,OUTPUT);
  offse = 0;
  t = millis();
}

void loop() {
if (Serial.available()) {
  H = Serial.read();
}

//int H[5]= {261.63,293.66,329.63,392,440};
Serial.println (H);

if (H == '1'){
  tone(buzzer,131);
  }
else if (H == '2' ){
  tone(buzzer,147);
  }
else if (H == '3' ){
  tone(buzzer,165);
  }
else if (H == '4' ){
  tone(buzzer,175);
  }
else if (H == '5' ){
  tone(buzzer,196);
  }
else if (H == '6' ){
  tone(buzzer,220);
  }
else if (H == '7' ){
  tone(buzzer,247);
}
else {
  noTone(buzzer);
//for (int i=0; i <= 5; i++){   
  // tone(buzzer,H[i]);
  // delay(1000);
   // }
}   
if (millis() - t > 300) {
   offse = (offse + 1) % 2;
   t = millis();}
}
