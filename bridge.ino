int led=13, i = 0, flag, inoutpin=0;
char z, alpha, cripter, cript;
void setup() {
pinMode (led, OUTPUT);
Serial.begin(9600);
}
int zeka(char z){
  if (Serial.available() > 0) {
      alpha = Serial.read()- '0';
      if (z == '1'){
          i = 1; 
      }
      if (i == 1){
        alpha = Serial.read()- '0';
        inoutpin = 1;
        pinMode (int(alpha), INPUT);
      }
      if (i == 0){
        alpha = Serial.read()- '0';
        pinMode (int(alpha), OUTPUT);
      }

return int(alpha);
}
}
void loop() {
   if (Serial.available() > 0) {
      cripter = Serial.read()- '0';
      flag = zeka(cripter);
      Serial.println(flag);
      cript = Serial.read()- '0';
      if (cript == 1){
        if (inoutpin == 1){
          Serial.write(1);
        }
        else digitalWrite(flag, HIGH);
        
          
      }
      if (cript == 0){
        if (inoutpin == 0){
          digitalWrite(flag, HIGH);
        }
      }
   }
}
        
          
        
       
       
          
