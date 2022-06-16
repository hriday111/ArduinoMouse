

#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>
String res;
bool debug =1;
int z = 1;
bool leftC, rightC;
MPU6050 mpu;
int16_t ax, ay, az, gx, gy, gz;
int vx, vy;
int left=3;
int right=6;

void setup() {

  Serial.begin(9600);
  Wire.begin();
  pinMode(2,OUTPUT);
  pinMode(left, INPUT);
  pinMode(right, INPUT);
  digitalWrite(left,HIGH);
  digitalWrite(right,HIGH);
  mpu.initialize();
  if (!mpu.testConnection()) { while (1); }
  delay(3000);
  mpu.CalibrateGyro();
  mpu.CalibrateAccel();
}

bool range(int start, int num, int last){
  if(num<last&&num>start){return true;}
  else{false;}
  } 
void loop() {
  
  leftC = !digitalRead(left);
  rightC= !digitalRead(right);
  
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  if (range(-15000,ax,15000)&&range(-15000,ay,15000)){
  if(debug){
  ax = map(ax, -15000, 15000, -5, 5);
  ay = map(ay, -15000, 15000, -5, 5);
  //Serial.print("X ");
  Serial.print(ax);
  Serial.print(":");
  //Serial.print("    Y ");
  Serial.print(ay);
  Serial.print(":");
  Serial.print(leftC);
  Serial.print(":");
  Serial.println(rightC);}
  delay(100);

  }

}
