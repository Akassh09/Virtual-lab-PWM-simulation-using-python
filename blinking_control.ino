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
if(st.toInt()==1)
{
  digitalWrite(led,HIGH);
}
else if(st.toInt()==2)
{
  digitalWrite(led,LOW);
}
}
