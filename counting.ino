const int led[]={2,3,4,5};
int i,j,k,a[4];
void setup() {
  // put your setup code here, to run once:
for(i=0;i<4;i++)
{
  pinMode(led[i],OUTPUT);
}
}

void loop() {
  // put your main code here, to run repeatedly:
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
    digitalWrite(led[j],a[j]);
  }
  delay(1000);
}
}
