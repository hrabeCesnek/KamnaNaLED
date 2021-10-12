import serial
import sys

MaxTemp = 300
MinTemp = 520
direction = "U"
newdirection = "U" 
Set_Temp = MinTemp

ser = serial.Serial('/dev/ttyACM0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)


with open("./TempNum.txt") as file:
    Temp_old = int(file.readline())
    Set_Temp = Temp_old
    direction = file.readline()
    newdirection = direction
    if(direction == "D" and Temp_old > MaxTemp):
        Set_Temp = Temp_old - 10
    elif(direction == "D" and Temp_old == MaxTemp):
        newdirection = "U"
    elif(direction == "U" and Temp_old < MinTemp):
        Set_Temp = Temp_old + 10
    elif(direction == "U" and Temp_old == MinTemp):
        newdirection = "D"

    with open("./TempNum.txt",'w') as file:
        file.write(str(Set_Temp)+"\n")
        file.write(str(newdirection))
        

print(Set_Temp)

an_int = Set_Temp
a_bytes_big = an_int.to_bytes(2, 'big')
begin = bytes('S', 'ascii')
ser.write(begin)
ser.write(a_bytes_big)