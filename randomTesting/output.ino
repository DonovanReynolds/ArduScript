
void setup(){
Serial.begin(9600);
pinMode(8,INPUT);
pinMode(5,OUTPUT);
}
void loop() {
if ((digitalRead(8) == false)){
digitalWrite(5,HIGH);
delay(2000);
}
}
