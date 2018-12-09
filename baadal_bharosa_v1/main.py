import serial
import json
import time
import uuid
import random
from datetime import datetime
from upm import pyupm_jhd1313m1

ard = serial.Serial('/dev/ttyS2', 9600,timeout=1)
lcd = pyupm_jhd1313m1.Jhd1313m1(0, 0x3e, 0x62)

def showTemplcd(angle):
	lcd.clear()
	lcd.setCursor(0, 0)
        #For writing on next line 
	#lcd.setCursor(1, 0)
	lcd.write("Dig_val:" + angle + " Deg")
	lcd.setColor(255, 180, 180)

def report_val(temp_val):
    '''
    Write out temperature to a random json file
    '''
    #v = fake_fan_sensor()
    fname = str(uuid.uuid4()) + ".json"
    d = {
        'metric': {
            'name': 'Furnace Temperature',
            'source': 'sensor_1',
            'kind': 'gauge',
            'unit': 'Farenheit',
            'value': temp_val,
            'timestamp': int(time.time()),
            'date': datetime.utcnow().strftime("%Y-%m-%d"),
            'time': datetime.utcnow().strftime("%H-%M-%S")
        }
    }
    with open(fname, 'w') as fp:
        json.dump(d, fp)
        print("Recorded furnace temp at %s Farenheit in %s" %(temp_val, fname))

if __name__ == '__main__':
	print("Welcome to my world!!!")
        print("Serial port:",ard.name)
	try:
		while True:
                        time.sleep(1)
			ardOut = ard.readline()
                        print("Ardout ",ardOut)
		        showTemplcd(ardOut)
                        #report_val(ardOut)
                        time.sleep(1)
			#if ardOut.find("Digital_val:") != -1:
			#	showTemplcd("11")
	except KeyboardInterrupt:
		lcd.setColor(0,0,0)
		lcd.clear()
		print("CTRL-C!! Exiting...")


