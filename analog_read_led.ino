const int a[]={2,3,4,5};
int i,j,k,b[4],l;
void setup() {
  // put your setup code here, to run once:
for(i=0;i<4;i++)
{
  pinMode(a[i],OUTPUT);
}
}

void loop() {
  // put your main code here, to run repeatedly:
l=map(analogRead(A0),0,1023,0,15);
for(i=0;i<l;i++)
{
  k=i;
  for(j=0;j<4;j++)
  {
    b[j]=k%2;
    k/=2;
  }
  for(j=0;j<4;j++)
  {
    digitalWrite(a[j],b[j]);
  }
  delay(500);
}
}
