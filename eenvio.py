#!/usr/bin/env python
import serial
import time
import sys

if __name__ == '__main__':
  ser = serial.Serial('COM3', 57600, timeout=1)  # open serial port
  print(ser.name)         # check which port was really used
  while 1:
      try:
        ser.write(b'el proyecto valio')     # write a string
        print("sent \n")
        time.sleep(1)
      except (SystemExit, KeyboardInterrupt) :
        ser.close()             # close port
        sys.exit(0)