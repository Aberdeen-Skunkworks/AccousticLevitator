#include <HardwareSerial.h>

HardwareSerial to_FPGA(1); //Use UART 1
const int baud = 460800;
bool ledstate = 0;

void setup() {
  //We use active high, inactive Z for the sync line
  pinMode(4, INPUT);
  digitalWrite(4, HIGH);
  
  pinMode(22, OUTPUT);
  digitalWrite(22, LOW);

  Serial.begin(baud);
  to_FPGA.begin(baud, SERIAL_8N1, 19, 23);
}
void loop() {
  if (to_FPGA.available()) {
    Serial.write(to_FPGA.read());
  }
  if (Serial.available()) {
    byte a = Serial.read();
    byte mask = 0b11110000;
    if ((a & mask) == mask) {
      ledstate = !ledstate;
      pinMode(22, ledstate?OUTPUT:INPUT);
      if ((a & (~mask)) == 0b00000001) {
        pinMode(4, OUTPUT);
      } else if ((a & (~mask)) == 0b00000000) {
        pinMode(4, INPUT);
      }
    } else {
      to_FPGA.write(a);
    }
  }
}

