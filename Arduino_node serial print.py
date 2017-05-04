import serial # pyserial library required
import requests # pip install requests
while(1):
	
	ser = serial.Serial('/dev/ttyACM1',9600)  # check the arduino monitor for port and change accordingly 
	response = requests.get('http://192.168.43.65:8080') #Ip address chages based on the router
	var = str(ser.readline())
	x = response.text
	a,b,c=var.split(',')
	d= x[-5:]
	print(a)
	print(b)
	print(c)
	print(d)
