// Select appropriate port
// Baud rate 9600

int photo_diode_output = A0; 

void setup()
{
  Serial.begin(9600);
}

void loop ()
{
  float voltage = analogRead(A0) ;
  Serial.print (voltage);
  Serial.print("\n") ;
}
