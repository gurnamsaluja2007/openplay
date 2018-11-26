//pins used for components
const int buzzer = 4;
const int sensor = A1;

//this is the threshold value for the light sensor
//to make the light sensor more sensitive, lower this value

void setup(){
        pinMode(sensor, INPUT);  // set pin for button input
        Serial.begin(9600);
        //Serial.print("Waiting ...");
}

void loop() {
        int sensorVal = analogRead(sensor);
        if (isnan(sensorVal)) {
            Serial.println("Failed to read");
            return;
        }

        //Serial.print("G:Digital_val ");
        Serial.println(sensorVal);
        delay(2000);
}

