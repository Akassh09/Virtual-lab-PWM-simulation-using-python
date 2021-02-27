const int pwm=3;
const int dir=4;
int a;
String st;
void setup() {
  // put your setup code here, to run once:
pinMode(pwm,OUTPUT);
pinMode(dir,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
a=map(analogRead(A0),0,1023,0,255);
analogWrite(pwm,a);
if(Serial.available())
{
  st=Serial.readString();
}
if(st=="0")
{
  digitalWrite(dir,LOW);
}
else if(st=="1")
{
  digitalWrite(dir,HIGH);
}
}
