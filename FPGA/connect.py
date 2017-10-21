#!/usr/bin/python

class Controller():
    def __init__(self):
        import serial
        self.com = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=0.5)

    def sendCmd(self, byte1, byte2, byte3):
        #Serial communication is carried out using 8 bit/byte
        #chunks. To be able to communicate all the data we need, we
        #use commands composed of 3 bytes. We use the highest bit of
        #each byte to denote if it is the first byte in a command.
        #The remaining bytes must not have the uppermost bit set (to
        #prevent errors in communication causing the controller to
        #assume they are the start of a command), thus only 21bits of
        #information are available for each command.
        cmd=bytearray([byte1, byte2, byte3])
        self.com.write(cmd)
        #The controller echos back the first byte when it processes a
        #command as an acknowledgement, we check here for that to see
        #if something went wrong.
        ack = bytearray(self.com.read(1))
        if ack[0] != byte1:
            raise Exception("Bad ACK")
        if len(ack) == 0:
            raise Exception("Timeout waiting for ACK")

    def sendReset(self):
        self.sendCmd(0b10000000, 0, 0)
    
ctl = Controller()

ctl.sendReset()
