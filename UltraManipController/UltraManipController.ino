#define BypassSerial

#ifdef BypassSerial
void setup() {
    pinMode(35, INPUT);
    pinMode(34, INPUT);
}
void loop() {}
#endif

#ifdef SoftwareSerial
void setup() {
   Serial.setup();
    pinMode(35, INPUT);
    pinMode(34, INPUT);
}
void loop() {}
#endif
