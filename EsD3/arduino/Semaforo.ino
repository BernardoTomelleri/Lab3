/*state
 * 0= ALL OFF
 * 1= RED ON
 * 2= RED YELLOW ON
 * 3= GREEN ON
 * 4= GREEN YELLOW ON
 * 5= YELLOW ON
 * 
 */
void setup() {
  pinMode(5, OUTPUT); //Led Rosso
  pinMode(6, OUTPUT); //Led Giallo
  pinMode(7, OUTPUT); //Led Verde
  pinMode(8, INPUT_PULLUP); //Pin di Enable
}
int tickGREEN=1000; //Temporizzazione dello stato VERDE
int tickRED=1000; //Temporizzazione dello stato ROSSO
int tickYELLOW=1000; //Temporizzazione dello stato GIALLO
int tickREDYELLOW=1000; //Temporizzazione dello stato ROSSOGIALLO
int tickGREENYELLOW=1000; //Temporizzazione dello stato VERDEGIALLO
int tickOFF=1000; //Temporizzazione dello stato spento
int CurrentState=0; //stato iniziale impostato sul tutto spento


void loop() {
  //viene controllato se il semaforo \`e abilitato
  if(CheckEnable()){ 
    
    // nel caso in cui il semaforo sia abilitato
    switch(CurrentState){  
    case 1: //se lo stato precedente risulta essere rosso e giallo
      CurrentState=3; //lo stato corrente viene spostato a verde
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      digitalWrite(7,HIGH);  
      delay(tickGREEN); 
      break; 
    case 3: //se lo stato precedente risulta essere solo verde
      CurrentState=4; //lo stato corrente viene portato a giallo e verde
      digitalWrite(6,HIGH);
      delay(tickGREENYELLOW);
      break;
      
    default: // in qualunque altro caso di stato precedente, se il semaforo \`e abilitato, lo stato inizializzato \`e quello rosso
      CurrentState=1;
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      delay(tickRED); 
    }
    
  }else { 
    //nel caso in cui il semaforo sia disabilitato
    switch(CurrentState){
      case 5: // se lo stato precedente risulta essere giallo 
        CurrentState=0; //imposta lo stato corrente a tutto spento
        digitalWrite(6,LOW);
        delay(tickOFF); 
        break;     
      default: // in qualunque altro caso di stato precedente, lo stato inizializzato \`e quello giallo
        CurrentState=5;
        digitalWrite(6,HIGH);
        digitalWrite(5,LOW);
        digitalWrite(7,LOW);
        delay(tickYELLOW);
      }
  }
}

bool CheckEnable(){ 
  //Algoritmo di controllo per Enable
  
  int check =digitalRead(8);
  return (check== HIGH);
}
