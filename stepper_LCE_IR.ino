 // defining the constants
# define move_pin 10
# define dir_pin 2
# define button_pin 4

 // defining the variables

double distance = 1.5; // distance the translator has to travel = amount for which we want the sample to stretch

double num_steps = 0;
double wait_time = 300; // in microseconds
bool dir = 0;

 // functions

void getNumSteps() {
  num_steps = 
}
 
void changeDir() {
  dir = !dir;
  digitalWrite(dir_pin, dir);
}

void stopStepper() {
  digitalWrite(move_pin, 0);
}

void moveStepper() {
  digitalWrite(move_pin, 1);
  delayMicroseconds(wait_time);
  digitalWrite(move_pin, 0);
  delayMicroseconds(wait_time);
}


void setup() {

  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(move_pin, OUTPUT);
  pinMode(dir_pin, OUTPUT);
  pinMode(button_pin, INPUT_PULLUP);

  Serial.begin(9600);

  digitalWrite(dir_pin, 0);

}

void loop() {

  // until the button isn't pressed, just wait
  // while (digitalRead(button_pin) == 1) {
  //   delay(10);
  // }

  // if the button has been pressed, do the following:

  moveStepper();

}
