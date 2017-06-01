int i = 0;  
int r0 = 0;      //
int r1 = 0;      //
int r2 = 0;      //

int a = A0;
int b = A1;
int c = A1;
int d = A1;
int e = A1;

int s0 = 2;
int s1 = 3;
int s2 = 4;

void setup(){  
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
}
//
//float X[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0} ;

int n = 0;

void loop () {
//if (n == 0) {
//for (int i = 0 ; i < 10 ; i ++) 
//{
//for (i=0; i<=7; i++) 
//{
//
//    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     
//
//    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     
//
//    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     
//
//   
//    digitalWrite(s0, r0);
//
//    digitalWrite(s1, r1);
//
//    digitalWrite(s2, r2);
//    
//   X[i] = analogRead(A0) ;
//   
//}
//
//for (i=0; i<=7; i++) {
//
//    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     
//
//    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     
//
//    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     
//
//   
//    digitalWrite(s0, r0);
//
//    digitalWrite(s1, r1);
//
//    digitalWrite(s2, r2);
//    
//   X[i+8] = analogRead(A1) ;
//   Serial.print(" ");
//}}
//}

  for (i=0; i<8; i++) 
  {

    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     

    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     

    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     

   
    digitalWrite(s0, r0);

    digitalWrite(s1, r1);

    digitalWrite(s2, r2);

 //Serial.print(digitalRead(s2));
    //Serial.print(digitalRead(s1));
    //Serial.print(digitalRead(s0));
    
   
     Serial.print (analogRead(A0));
     Serial.print(" ");
  }
     for (i=0; i<8; i++) {

    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     

    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     

    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     

   
    digitalWrite(s0, r0);

    digitalWrite(s1, r1);

    digitalWrite(s2, r2);

 //Serial.print(digitalRead(s2));
    //Serial.print(digitalRead(s1));
    //Serial.print(digitalRead(s0));
    
   
     Serial.print (analogRead(A1));
     Serial.print(" ");
  }  
  for (i=0; i<8; i++) {

    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     

    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     

    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     

   
    digitalWrite(s0, r0);

    digitalWrite(s1, r1);

    digitalWrite(s2, r2);

 //Serial.print(digitalRead(s2));
    //Serial.print(digitalRead(s1));
    //Serial.print(digitalRead(s0));
    
   
     Serial.print (analogRead(A2));
     Serial.print(" ");
  }  
  for (i=0; i<8; i++) {

    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     

    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     

    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     

   
    digitalWrite(s0, r0);

    digitalWrite(s1, r1);

    digitalWrite(s2, r2);

 //Serial.print(digitalRead(s2));
    //Serial.print(digitalRead(s1));
    //Serial.print(digitalRead(s0));
    
   
     Serial.print (analogRead(A3));
     Serial.print(" ");
  }  
  Serial.print("\n");
  for (i=7; i>= 0; i--)
  {

    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     

    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     

    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     

   
    digitalWrite(s0, r0);

    digitalWrite(s1, r1);

    digitalWrite(s2, r2);

 //Serial.print(digitalRead(s2));
    //Serial.print(digitalRead(s1));
    //Serial.print(digitalRead(s0));
    
   
     Serial.print (analogRead(A4));
     Serial.print(" ");
  } 
  
  for (i=7; i>=0; i--)
   {

    r0 = bitRead(i,0);    // use this with arduino 0013 (and newer versions)     

    r1 = bitRead(i,1);    // use this with arduino 0013 (and newer versions)     

    r2 = bitRead(i,2);    // use this with arduino 0013 (and newer versions)     

   
    digitalWrite(s0, r0);

    digitalWrite(s1, r1);

    digitalWrite(s2, r2);

 //Serial.print(digitalRead(s2));
    //Serial.print(digitalRead(s1));
    //Serial.print(digitalRead(s0));
    
   
     Serial.print (analogRead(A5));
     Serial.print(" ");
  }
  Serial.print("\n");
}
