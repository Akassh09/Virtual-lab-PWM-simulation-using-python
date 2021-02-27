const int pin[]={2,3,4,5};
int i,j,k,a[4];
void setup() {
  // put your setup code here, to run once:
for(i=0;i<4;i++)
{
  pinMode(pin[i],OUTPUT);
}
pinMode(6,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(6,LOW);
for(i=0;i<16;i++)
{
  k=i;
  for(j=0;j<4;j++)
  {
    a[j]=k%2;
    k/=2;
  }
  for(j=0;j<4;j++)
  {
    digitalWrite(pin[j],a[j]);
  }
  delay(1000);
}
}
