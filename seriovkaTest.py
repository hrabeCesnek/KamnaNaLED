import serial
import sys


ser = serial.Serial('/dev/ttyACM0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
an_int = min(int(sys.argv[1]),4096)
a_bytes_big = an_int.to_bytes(2, 'big')
begin = bytes('S', 'ascii')
ser.write(begin)
ser.write(a_bytes_big)

