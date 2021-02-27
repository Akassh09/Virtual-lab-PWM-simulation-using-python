const int led=2;
String st="";
void setup() {
  // put your setup code here, to run once:
pinMode(led,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available())
{
  st=Serial.readString();
}
if(st=="on" || st=="True")
{
  digitalWrite(led,HIGH);
}
else if(st=="off" || st=="False")
{
  digitalWrite(led,LOW);
}
}
