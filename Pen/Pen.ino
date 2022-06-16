

#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>
#include <Mouse.h>
#define prnt Serial.print
#define pl Serial.println
int z = 1;
bool leftC, rightC;
MPU6050 mpu;
int16_t ax, ay, az, gx, gy, gz;
int vx, vy;
int left=3;
int right=6;
bool debug= true;
bool rock_there=false;
void setup() {

  Serial.begin(9600);
  //while(1){if(Serial.available()){break;}}
  Wire.begin();
  //pl("Begun  ");
  pinMode(2,OUTPUT);
  pinMode(left, INPUT);
  pinMode(right, INPUT);
  digitalWrite(left,HIGH);
  digitalWrite(right,HIGH);
  mpu.initialize();
  if (!mpu.testConnection()) { while (1); }
  //delay(5000);
  //mpu.CalibrateGyro();
  //mpu.CalibrateAccel();
}

bool range(int start, int num, int last){
  if(num<last&&num>start){return true;}
  else{false;}
  } 
  
void loop() {
  
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  ax=(ax/1000);
  ay=(ay/1000);
  az=(az/1000);

  gx=(gx/1000);
  gy=(gy/1000);
  gz=(gz/1000);
 /* prnt(" Ax: ");
  prnt(ax);
  prnt(" Ay: ");
  prnt(ay);
  prnt(" Az: ");
  prnt(az);*/
  if(!debug){
  if(ax>11&&ax<16&&ay<6&&!rock_there){
    pl("Rock.PullUp()");
    rock_there=true;
    }
  if(rock_there&&ax<10&&ay>12&&ay<17){
    pl("Rock.Throw()");
    rock_there=false;
    }
  else{pl("none");}}
  if(debug){
  //prnt(" Ax: ");
  prnt(ax);
  prnt(",");
  //prnt(" Ay: ");
  prnt(ay);
  prnt(",");
  //prnt(" Az: ");
  prnt(az);
  prnt(",");
  prnt(!digitalRead(left));
  prnt(",");
  pl(!digitalRead(right));
  
  }
  delay(100);
  }
