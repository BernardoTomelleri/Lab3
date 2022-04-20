
/* 
 *   FSM example on arduino: 
 *   Abilitato:
 *   LedVerde per 4 secondi -> 
 *   LedRosso LedVerde per 2 secondi -> 
 *   LedRosso per 4 secondi
 *   Disabilitato:
 *   LedVerde 4 secondi ->
 *   tutto spento 1 secondo
 */

const int LVpin = 9; // led verde
const int LRpin = 11; // led rosso  
const int ENpin = 8; // input pin for enable

const int timeV = 4000; //time of verde (ms)
const int timeVR = 2000; //time of verde rosso (ms)
const int timeR = 4000; //time of rosso (ms)
const int timeVOFF =  1000; // time del lampeggiante

#define LVstate 0
#define LVRstate 1
#define LRstate 2
#define LOFFstate 3

int thisState = LOFFstate; // this state
int nextState = LOFFstate; // next state
int stateWait = timeVOFF; // state wait
bool inEnable = false; // enable bit


void setup() {
  // put your setup code here, to run once:
  pinMode(LVpin, OUTPUT);
  Serial.begin(9600);
  pinMode(LRpin, OUTPUT);
  pinMode(ENpin, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:
  //
  // 1. read the input
  // with (state) 
  // 2. generate the output
  // 3. calculate the next state
  // 4. wait for this state to complete
  inEnable = readEnable();
  Serial.println(thisState);
  Serial.println(inEnable);
  switch (thisState) {
  case LVstate:
    // green state
    stateWait = timeV;
    setOutput(HIGH, LOW);
    if (inEnable) {
      nextState = LVRstate;
    } else {
      nextState = LOFFstate;
    }
    break;
//
  case  LVRstate:
    stateWait = timeVR;
    setOutput(HIGH, HIGH);
    if (inEnable) {
      nextState = LRstate;
    } else {
      nextState = LOFFstate;
    }
    break;
//    
  case LRstate:
    // red state
    stateWait = timeR;
    setOutput(LOW, HIGH);
    if (inEnable) {
      nextState = LVstate;
    } else {
      nextState = LOFFstate;
    }
    break;
//    
  case LOFFstate:
    // OFF state
    stateWait = timeVOFF;
    setOutput(LOW, LOW);
    if (inEnable) {
      nextState = LRstate;
    } else {
      nextState = LVstate;
    }
    break;
//    
  default:
  // should never get here
  break;
  }
/*
 wait for the stateWait ms time
*/
  delay(stateWait);
/* 
 *  goto next state
 */
  
  thisState = nextState;
}

bool readEnable(){
  // read the value of the enable pin
  int val;
  val = digitalRead(ENpin);
  return ( val == HIGH);
}

int setOutput(int LV, int LR) {
  //Serial.println("setOutput");
  //Serial.print( LV);  
  //Serial.print( LR);
  //
  digitalWrite(LVpin, LV);  
  digitalWrite(LRpin, LR);
}
