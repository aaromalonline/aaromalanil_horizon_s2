#include <Servo.h>

Servo servos[6];
int spins[] = {10, 9, 7, 6, 5, 4};
int angles[6];

void parseAngles(String inp){
    int i = 0;
    inp.trim();
    char inpbuf[50];
    inp.toCharArray(inpbuf, 50);
        
    char *angle = strtok(inpbuf, " ");

    while (angle != NULL && i < 6) {
        angles[i] = atoi(angle);  
        angle = strtok(NULL, " "); 
        i++;
    }

}

void setup() {
    Serial.begin(9600);
    
    for (int i = 0; i < 6; i++) {
        servos[i].attach(spins[i]);
        servos[i].write(90);
    }
    
    Serial.println("Enter angles of rotation for servos (space-separated): ");
}

void loop() {
    if (Serial.available()) {
        String inp = Serial.readStringUntil('\n');
        parseAngles(inp);

        Serial.print("Received angles: ");
        for (int i = 0; i < 6; i++) {
            Serial.print(angles[i]);
            Serial.print(" ");
            for (int j = 0; j < angles[i]; j++){
                servos[i].write(j);
                delay(15);
            }
        }

    }
}
