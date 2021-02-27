#include<Servo.h>
Servo servo;
String i="";
void setup() {
  // put your setup code here, to run once:
servo.attach(5);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available())
{
  i=Serial.readString();
}
servo.write(i.toInt());
}
