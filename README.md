# Pi Temperature

Repository contains code for my academic minor project. 

The program runs on a Raspberry Pi: it detects the temperature of the environment using the DS18B20 digital sensor and posts it to a web
application on the url http://pi-temperature.appspot.com using Python's requests library.

The repository of the web application can be found here: https://github.com/raunaqss/pi-temperature

There are a number of ways to connect the RaspberryPi to the internet to be able to post the sensory data:

1. Wifi - if you have a wiki adapter.

2. Bluetooth tethering - if you have a bluetooth adapter and a bluetooth internet hotspot.

3. USB tethering from smartphone (have tested this on iOS only).

The pdf file Pi Temperature Report in the repository is a detailed report on this project.
