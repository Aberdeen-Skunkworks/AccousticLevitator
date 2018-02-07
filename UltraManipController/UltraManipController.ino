#include <HardwareSerial.h>

HardwareSerial to_FPGA(1); //Use UART 1
const int baud = 460800;

void setup() {
  Serial.begin(baud);
  to_FPGA.begin(baud, SERIAL_8N1, 19, 23);
}
void loop() {
  if (to_FPGA.available()) {
    Serial.write(to_FPGA.read());
  }
  if (Serial.available()) {
    to_FPGA.write(Serial.read());
  }
}

