import datetime
import os
import glob
import requests
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
print glob.glob(base_dir + '10-0008026d6277')
device_folder = glob.glob(base_dir + '10-0008026d6277')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string)/1000.0
        temp_f = temp_c * 9.0/5.0 + 32.0
        return [temp_c, temp_f, datetime.datetime.now().strftime('%c')]

def post_reading(cel, fah, ts):
    reading = {'celsius': cel, 'fahrenheit': fah, 'timestamp': ts}
    r = requests.post('http://pi-temperature.appspot.com', data = reading)
    
    
