import time
from thermometer import *

while True:
    try:
        reading = read_temp()
        post_reading(reading[0], reading[1], reading[2])
    except:
        pass
    time.sleep(10)
