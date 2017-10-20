#!/usr/bin/python

import serial

s = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)

s.write(bytearray([77,66]))
print(repr(bytearray(s.read(2))))
