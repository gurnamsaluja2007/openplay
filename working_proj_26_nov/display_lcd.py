import serial
from upm import pyupm_jhd1313m1

ard = serial.Serial('/dev/ttyS2', 9600,timeout=1)
lcd = pyupm_jhd1313m1.Jhd1313m1(0, 0x3e, 0x62)

def showAngle(angle):
	lcd.clear()
	lcd.setCursor(0, 0)
	#lcd.write(humid)
	#lcd.setCursor(1, 0)
	lcd.write("Digital_val:" + angle + " Degree")
	lcd.setColor(255, 180, 180)

if __name__ == '__main__':
	print("Welcome to my world!!!")
        print("Serial port:",ard.name)
        #ard.write(b'helloos')
	try:
		while True:
                        #ard.write(b'helloos')
                        #print("Ardout name ",ard.name)
			ardOut = ard.readline()
                        print("Ardout ",ardOut)
		        showAngle(ardOut)
			#if ardOut.find("Digital_val:") != -1:
			#	showAngle("11")
	except KeyboardInterrupt:
		lcd.setColor(0,0,0)
		lcd.clear()
		print("CTRL-C!! Exiting...")


