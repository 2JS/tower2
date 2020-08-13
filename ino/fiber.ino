// Include the Arduino Library
#include <Arduino.h>

// Number of steps per output rotation
#define MOTOR_STEPS 200 // For 1.8 degrees/step motors

// The pin Arduino
#define DIR 8
#define STEP 9
#define MS1 10
#define MS2 11
#define MS3 12

#define UP HIGH
#define DOWN LOW

// interval in microseconds
// current_interval = (3*10^5)/(RPM)
long current_interval= 5000;
double current_RPM = 0;
int current_DIR = DOWN;

// GLOBAL VARIABLES
unsigned long previousMicros = 0;

void setup()
{
  // limit switch setting
  pinMode(DIR, OUTPUT);
  pinMode(STEP, OUTPUT);
  pinMode(MS1, OUTPUT);
  pinMode(MS2, OUTPUT);
  pinMode(MS3, OUTPUT);

  // only full steps will be used in the current system.
  digitalWrite(MS1, LOW);
  digitalWrite(MS2, LOW);
  digitalWrite(MS3, LOW);

  // initialize the serial port:
  Serial.begin(115200);
}

void loop()
{
  handleSerial();
}

void handleSerial()
{
  /*
  Serial input form
  (floating point number)('+' or '-')('\n')
  floating point number: speed(RPM) 
  ('+' or '-'): direction
  ('\n'): delimiter
  */
  while(Serial.available() > 0){
    // get serial input
    String incomingString = Serial.readStringUntil('\n');
    int clength = incomingString.length();

    // get RPM, diretion, and location
    double incomingRev = incomingString.toDouble();
    char incomingDir = incomingString[clength-1];

    //set parameters
    current_RPM = incomingRev;
    current_interval = (3e+5)/(current_RPM);
    if(incomingDir == '+'){
      current_DIR = UP;
      digitalWrite(DIR, UP);
    }else if(incomingDir == '-'){
      current_DIR = DOWN;
      digitalWrite(DIR, DOWN);
    }

    // actual turning
    Serial.println("Fiber Process Starts");
    handleMove();
  }
}

void handleMove()
{
  while(true){
    unsigned long currentMicros = micros();

    // FIBER pulse
    if(currentMicros - previousMicros >= current_interval){
      previousMicros = currentMicros;

      // delay at least 2 microseconds
      digitalWrite(STEP, HIGH);
      delayMicroseconds(2);
      digitalWrite(STEP, LOW);

      // left time
      // (1) serial command
      if(Serial.available() > 0) {
        String incomingString = Serial.readStringUntil('\n');
        if(incomingString.equals("stop")){ // stop command => stop fiber motor
          digitalWrite(STEP, LOW);
          current_RPM = 0;
          Serial.println("Fiber Process Ends");
          return;
        }else{ // speed command => change speed immediately
          // get RPM, diretion, and location
          int clength = incomingString.length();
          double incomingRev = incomingString.toDouble();
          char incomingDir = incomingString[clength-1];

          //set parameters
          current_RPM = incomingRev;
          current_interval = (3e+5)/(current_RPM);
          if(incomingDir == '+'){
            current_DIR = UP;
            digitalWrite(DIR, UP);
          }else if(incomingDir == '-'){
            current_DIR = DOWN;
            digitalWrite(DIR, DOWN);
          }
        }
      }

      // (2) acceleration (deprecated)
      /*
      if(current_RPM < want_RPM){
        current_RPM += (current_interval/(1e+6))*(MOTOR_ACCEL);
        current_interval = (3e+5)/(current_RPM);
      }else{
        current_RPM -= (current_interval/(1e+6))*(MOTOR_DECEL);
        current_interval = (3e+5)/(current_RPM);
      }
      */

      //end left time
    }
  }
}
