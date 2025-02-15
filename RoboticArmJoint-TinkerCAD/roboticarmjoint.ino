#include <Servo.h>

/*Steps :
- parse target angles from serial input 
- move each servo to target angle simultaneously step by step : check whether current angle of each servo reach its target angle 
    - if current angle of each servo is less than target angle, increment current angle by 1
    - if current angle is greater than target angle, decrement current angle by 1 
    - move servo to current angle ie increment or decrement by 1 thus initiating clockwise or anti-clockwise rotation by 1 degree
*/


Servo servos[6]; //6 servo objects
int spins[] = {4,5,6,7,9,10}; //servo pins
int tangles[6]; //target angles
int cangles[] = {90, 90, 90, 90, 90, 90}; //initialize current angles to 90 degs


//parse target angles from serial input
void parseAngles(String inp){
    int i = 0;
    inp.trim();
    char inpbuf[50];
    inp.toCharArray(inpbuf, 50); //convert string to C char array
        
    char *angle = strtok(inpbuf, " "); //split string by space returning a pointer to the first substring

    while (angle != NULL && i < 6) {
        tangles[i] = atoi(angle);  //ascii to integer char conversion
        angle = strtok(NULL, " "); //get next substring
        i++;
    }
}

//simultaneous smooth movement of all servos to target angles one by one
void move(){
    bool status = true;
    //each iteration of while loop moves each servo by 1 degree
    while (status){
        status = false;
        for (int i=0; i<6; i++){
            if (cangles[i] != tangles[i]){
                status = true; //still increment/decrement left for that servo to reach target angle
                if (cangles[i] < tangles[i]){
                    cangles[i]++; //rotation in clockwise direction
                } else {
                    cangles[i]--; //rotation in anti-clockwise direction
                }
                servos[i].write(cangles[i]);
                delay(10); //servo movement speed
            }

        }
    }
}

void setup() {
    Serial.begin(9600);
    
    for (int i = 0; i < 6; i++) {
        servos[i].attach(spins[i]);
        servos[i].write(cangles[i]);
    }
    
    Serial.println("Enter angles of rotation for servos (space-separated): ");
}

void loop() {
    if (Serial.available()) {
        String inp = Serial.readStringUntil('\n');
        parseAngles(inp);
        move();
    }
}
