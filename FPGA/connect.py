#!/usr/bin/python

class Controller():
    def __init__(self):
        import serial
        self.com = serial.Serial(port="/dev/ttyUSB0", baudrate=460800, timeout=0.5)

    def getOutputs(self):
        self.com.write(bytearray([0b11000000,0,0]))
        ack = bytearray(self.com.read(1))[0]
        return ack        
    
    def sendCmd(self, bytestream):
        #Serial communication is carried out using 8 bit/byte
        #chunks. To be able to communicate all the data we need, we
        #use commands composed of 3 bytes. We use the highest bit of
        #each byte to denote if it is the first byte in a command.
        #The remaining bytes must not have the uppermost bit set (to
        #prevent errors in communication causing the controller to
        #assume they are the start of a command), thus only 21bits of
        #information are available for each command.

        # #The structure of a command
        #   23  22  21  20  19  18  17  16  15  14  13  12  11  10  9   8   7   6   5   4   3   2   1   0
        # | 1 | X | X | X | X | X | X | X | 0 | X | X | X | X | X | X | X | 0 | X | X | X | X | X | X | X |
        # 
        self.com.write(bytestream)
        
    def loadOffsets(self):
        self.sendCmd(bytearray([0b10100000, 0, 0]))

    def setOffset(self, clock, offset):
        # #The structure of the command
        #   23  22  21  20  19  18  17  16  15  14  13  12  11  10  9   8   7   6   5   4   3   2   1   0
        # | 1 | 0 | 0 | X | X | X | X | X | 0 | X | X | X | Z | Y | Y | Y | 0 | Y | Y | Y | Y | Y | Y | Y |
        #  X = 8 bit clock select
        #  Y = 10 bit half-phase offset
        #  Z = phase of first oscillation
        sign = 0
        offset = offset % 1250
        if offset > 624:
            sign = 1
            offset = offset - 624
        low_offset =  offset & 0b01111111
        high_offset = ((offset >> 7) & 0b00000111) + (sign << 3)

        b1 = 0b10000000 | (clock>>3)
        b2 = ((clock & 0b00000111)<<4)  | high_offset
        b3 = low_offset
        cmd = bytearray([b1, b2, b3])
        
        self.sendCmd(cmd)

    def benchmark(self):
        import timeit
        start = timeit.default_timer()
        NTests = 1000
        outputs = self.getOutputs()
        for i in range (NTests):
            for i in range(outputs):
                ctl.setOffset(i, 0)
            ctl.loadOffsets()
        end = timeit.default_timer()
        print "Benchmark - Pattern update at ", NTests/float(end-start), "Hz"
        
        
ctl = Controller()
print "Connected to controller with", ctl.getOutputs(), "outputs."

for i in range(ctl.getOutputs()):
    ctl.setOffset(i, i*10)
ctl.loadOffsets()
#ctl.benchmark()
