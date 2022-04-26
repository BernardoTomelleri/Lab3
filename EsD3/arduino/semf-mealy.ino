#define Epin 9  // enable
#define Rpin 12  // red
#define Ypin 11  // yellow
#define Gpin 10  // green

enum state { A, B, C } currState;

const unsigned wait[] = { 3000, 3000, 3000 };
const state nextEnabled[] = { B, C, A };
const state nextDisabled[] = { B, A, A };

void setup() {
    pinMode(Rpin, OUTPUT);
    pinMode(Ypin, OUTPUT);
    pinMode(Gpin, OUTPUT);

    pinMode(Epin, INPUT_PULLUP);

    currState = A;
}

void loop() {
    unsigned E = (digitalRead(Epin) == HIGH);
    currState =  E ? nextEnabled[currState] : nextDisabled[currState];

    /* Implementiamo l'appropriata logica combinatoria che associa lo
     * stato dei led allo stato della macchina e all'input */
    digitalWrite(Rpin, currState == C);
    digitalWrite(Ypin, currState == B);
    digitalWrite(Gpin, (currState != C) && E);
    delay(wait[currState]);
}
