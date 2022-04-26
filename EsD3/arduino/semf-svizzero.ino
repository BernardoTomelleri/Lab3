#define Epin 9  // enable
#define Rpin 12  // red
#define Ypin 11  // yellow
#define Gpin 10  // green

/* Dichiariamo i possibili stati della macchina e lo stato corrente. Gli stati
 * sono quelli di default dati da enum, i.e. numeri interi da 0 a 5: tale
 * fatto verrà sfruttato successivamente usando il valore di currState come
 * indice per accedere agli elementi di array. */
enum state { G, GY, R, RY, OFF, Y } currState;

/* Dichiariamo il tempo di attesa, lo stato dei led e lo stato successivo (sia
 * abilitato che disabilita
to) per ognuno degli stati. */
const unsigned wait[] = { 1000, 1000, 1000, 1000, 1000, 1000 };
const unsigned ledStates[][3] = {
    // R   Y   G
    {LOW, LOW, HIGH},
    {LOW, HIGH, HIGH},
    {HIGH, LOW, LOW},
    {HIGH, HIGH, LOW},
    {LOW, LOW, LOW},
    {LOW, HIGH, LOW}
};
const state nextEnabled[] = { GY, R, RY, G, R, R };
const state nextDisabled[] = { OFF, OFF, OFF, OFF, Y, OFF };

void setup() {
    /* Dichiariamo i pin di output */
    pinMode(Rpin, OUTPUT);
    pinMode(Ypin, OUTPUT);
    pinMode(Gpin, OUTPUT);

    /* Dichiariamo il pin enable come input, in modo che sia alto se
     * scollegato */
    pinMode(Epin, INPUT_PULLUP);

    /* Fissiamo lo stato iniziale */
    currState = OFF;
}

void loop() {
    /* Calcoliamo lo stato successivo in base al valore di enable e dello
    * stato precedente */
    currState = (digitalRead(Epin) == HIGH) ?
        nextEnabled[currState] : nextDisabled[currState];

    /* Codifichiamo il nuovo stato nei led e aspettiamo il tempo
     * appropriato */
    digitalWrite(Rpin, ledStates[currState][0]);
    digitalWrite(Ypin, ledStates[currState][1]);
    digitalWrite(Gpin, ledStates[currState][2]);
    delay(wait[currState]);
}
