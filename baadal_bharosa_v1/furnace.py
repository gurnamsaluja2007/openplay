import json
import time
import uuid
import random
from datetime import datetime


def fake_temperature_sensor():
    '''
    Return a fake temperature as a double rounded to two points
    '''
    return round(random.uniform(500, 700), 2)


def fake_fan_sensor():
    return (random.randint(100,300))


def report_fan():
    '''
    Write out temperature to a random json file
    '''
    v = fake_fan_sensor()
    fname = str(uuid.uuid4()) + ".json"
    d = {
        'metric': {
            'name': 'Furnace Fan RPM',
            'source': 'sensor_2',
            'kind': 'gauge',
            'unit': 'RPM',
            'value': v,
            'timestamp': int(time.time()),
            'date': datetime.utcnow().strftime("%Y-%m-%d"),
            'time': datetime.utcnow().strftime("%H-%M-%S")
        }
    }
    with open(fname, 'w') as fp:
        json.dump(d, fp)
        print("Recorded fan running at %d RPM in %s" %(v, fname))


def report_temp():
    '''
    Write out temperature to a random json file
    '''
    v = fake_temperature_sensor()
    fname = str(uuid.uuid4()) + ".json"
    d = {
        'metric': {
            'name': 'Furnace Temperature',
            'source': 'sensor_1',
            'kind': 'gauge',
            'unit': 'Farenheit',
            'value': v,
            'timestamp': int(time.time()),
            'date': datetime.utcnow().strftime("%Y-%m-%d"),
            'time': datetime.utcnow().strftime("%H-%M-%S")
        }
    }
    with open(fname, 'w') as fp:
        json.dump(d, fp)
        print("Recorded temperature sensor at %d Farenheit in %s" %(v, fname))


def main():
    counter = 0
    while True:
        if counter % 10 == 0:
            print("Furnace synced at loop: %d" % counter)
        if random.randint(0,1) == 1:
            report_temp()
        else:
            report_fan()
        time.sleep(5)
        counter = counter + 1


if __name__ == '__main__':
    main()
