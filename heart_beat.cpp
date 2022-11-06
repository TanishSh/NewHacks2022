/*
Arduino-MAX30100 oximetry / heart rate integrated sensor library
Copyright (C) 2016  OXullo Intersecans <x@brainrapers.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <Wire.h>
#include "MAX30100_PulseOximeter.h"

#define REPORTING_PERIOD_MS     100
#define SAMPLING_WINDOW   30
#define AWAKE_HEART_RATE 40

// PulseOximeter is the higher level interface to the sensor
// it offers:
//  * beat detection reporting
//  * heart rate calculation
//  * SpO2 (oxidation level) calculation
PulseOximeter pox;

uint32_t tsLastReport = 0;
int count = 0;
int heart_rate_sum = 0;
int sleepingRate = 55;
int buzzer = 12;
// Callback (registered below) fired when a pulse is detected
void onBeatDetected()
{
    //Serial.println("Beat!");
}

void setup()
{
    pinMode(buzzer, OUTPUT);
    Serial.begin(9600);

   // Serial.print("Initializing pulse oximeter..");

    // Initialize the PulseOximeter instance
    // Failures are generally due to an improper I2C wiring, missing power supply
    // or wrong target chip
    if (!pox.begin()) {
        //Serial.println("FAILED");
        for(;;);
    } else {
        //Serial.println("SUCCESS");
    }

    // The default current for the IR LED is 50mA and it could be changed
    //   by uncommenting the following line. Check MAX30100_Registers.h for all the
    //   available options.
    // pox.setIRLedCurrent(MAX30100_LED_CURR_7_6MA);

    // Register a callback for the beat detection
    pox.setOnBeatDetectedCallback(onBeatDetected);
}

void loop()
{
    // Make sure to call update as fast as possible
    pox.update();
      
    // Asynchronously dump heart rate and oxidation levels to the serial
    // For both, a value of 0 means "invalid"
    
    if (millis() - tsLastReport > REPORTING_PERIOD_MS) {
        //Serial.print("Heart rate:");
        //Serial.print(pox.getHeartRate());
        //Serial.println();
        tsLastReport = millis();
        
        if(count!=SAMPLING_WINDOW){
          heart_rate_sum += (pox.getHeartRate()); // dividing by 2 for error
          count++;
        }
        else if(count==SAMPLING_WINDOW){
          //Serial.print("Heart rate:");
          // csv format
          Serial.print(millis());
          Serial.print(",");
          Serial.print(heart_rate_sum/(2*SAMPLING_WINDOW));
          Serial.println();
          if (heart_rate_sum < AWAKE_HEART_RATE){
            //turn on buzzer 
            digitalWrite(buzzer, HIGH);
            delay(5000); // sec
            //turn off the buzzer
            digitalWrite(buzzer, LOW);
            delay(10000); //sec
          }
          heart_rate_sum = 0;
          count = 0;
        }
    }
}