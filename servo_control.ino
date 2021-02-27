#include<Servo.h>
Servo servo;
int i;
void setup() {
  // put your setup code here, to run once:
servo.attach(5);
}

void loop() {
  // put your main code here, to run repeatedly:
for(i=0;i<=180;i+=30)
{
  servo.write(i);
  delay(1000);
}
for(i=180;i>=0;i-=30)
{
  servo.write(i);
  delay(1000);
}
}
