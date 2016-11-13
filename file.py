import serial
ser = serial.Serial('/dev/ttyACM0',9600)
var=str(ser.readline())
file = open("newfile.csv", "w")
file.write(var)
file.write(",")
file.close()
