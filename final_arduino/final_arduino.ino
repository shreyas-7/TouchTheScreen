
int count = 0;  
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
  
}
//
//float X[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0} ;

int n = 0;

void loop () {
//if (n == 0) {
//for (int i = 0 ; i < 10 ; i ++) 
//{
//for (count=0; count<=7; count++) 
//{
//
//    r0 = bitRead(count,0);    // use this with arduino 0013 (and newer versions)     
//
//    r1 = bitRead(count,1);    // use this with arduino 0013 (and newer versions)     
//
//    r2 = bitRead(count,2);    // use this with arduino 0013 (and newer versions)     
//
//   
//    digitalWrite(s0, r0);
//
//    digitalWrite(s1, r1);
//
//    digitalWrite(s2, r2);
//    
//   X[count] = analogRead(A0) ;
//   
//}
//
//for (count=0; count<=7; count++) {
//
//    r0 = bitRead(count,0);    // use this with arduino 0013 (and newer versions)     
//
//    r1 = bitRead(count,1);    // use this with arduino 0013 (and newer versions)     
//
//    r2 = bitRead(count,2);    // use this with arduino 0013 (and newer versions)     
//
//   
//    digitalWrite(s0, r0);
//
//    digitalWrite(s1, r1);
//
//    digitalWrite(s2, r2);
//    
//   X[count+8] = analogRead(A1) ;
//   Serial.print(" ");
//}}
//}

n = 1;

  for (count=0; count<48; count++) {

    r0 = bitRead(count%8,0);    // use this with arduino 0013 (and newer versions)     

    r1 = bitRead(count%8,1);    // use this with arduino 0013 (and newer versions)     

    r2 = bitRead(count%8,2);    // use this with arduino 0013 (and newer versions)     

   
    digitalWrite(s0, r0);

    digitalWrite(s1, r1);

    digitalWrite(s2, r2);

 //Serial.print(digitalRead(s2));
    //Serial.print(digitalRead(s1));
    //Serial.print(digitalRead(s0));
   if (count < 8) 
   {
     Serial.print (analogRead(A0));
     Serial.print(" ");
   }
   else if (count < 16)
   {
     Serial.print (analogRead(A1));
     Serial.print(" ");
   }
   else if (count < 24)
   {
     Serial.print (analogRead(A2));
     Serial.print(" ");
   }
   else if (count < 32)
   {
     Serial.print (analogRead(A3));
     Serial.print(" ");
   }
  else if (count == 32)
  {
    Serial.print (analogRead(A4));
    Serial.print("\n") ;
  }
  else if (count < 40)
   {
     Serial.print (analogRead(A5));
     Serial.print(" ");
   }
   else if (count == 48)
   {
    Serial.print("\n");
   } 
  }
}
