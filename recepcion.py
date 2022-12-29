#!/usr/bin/env python
import serial
import time
import sys

ser = serial.Serial('COM3', 57600, timeout=1)
timeout = time.time() + 10   # 5 minutes from now
while True:
    test = 0        
    try:
        d=ser.read(57600)
        string = d.decode('utf-8')
        print(string)
        print(type(string))

    except (SystemExit, KeyboardInterrupt):
        ser.close()
        sys.exit(0)  
    if test == 10 or time.time() > timeout:
        break
    test = test - 1




