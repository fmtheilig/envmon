Environmental Monitor using a Raspberry Pi and the DHT22 temperature and humidity sensor

Create a simple temperature and humidity sensor on any Raspberry Pi using the DHT22 sensor.

I got details primarily from: 
https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/

but I started with this tutorial: 
https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9

The Medium.com article documents a much broader project and included stuff not relevant
to my goals. I just wanted to log temperature and humidity, plus CPU core temperature
(because why not). Also, I had issues with their code. The PiMyLifeUp.com article seemed to
be using a different piece of hardware as it had four pins and requires the use of a resistor,
but the code worked. The sensors I picked up ($12 for two on Amazon) matched the wiring in
the Medium.com article: (+) on the DHT22 to pin 2 (5V power), (-) to pin 5 (ground), and the
center to pin 7 (GPIO 4).

envmon.py logs the CPU core temperature, ambient temperature, and humidity to
/var/log/envmon.log. It also will send an email alert if one of the values exceeds a
set value. Move the file 'envmon' to /etc/logrotate.d for log rotation. Edit as desired.

INSTALLATION 

I upgraded my device to Buster, but that was not actually required: 
https://pimylifeup.com/upgrade-raspbian-stretch-to-raspbian-buster/

sudo apt install python3-dev python3-pip 

sudo python3 -m pip install --upgrade pip setuptools wheel 

sudo pip3 install Adafruit_DHT 

I put envmon.py into /usr/bin and added the following line to /etc/crontab:

*/10 *   * * *   root   /usr/bin/envmon.py

This checks the environmental conditions once every ten minutes and must be run as root.
The code should be self explanitory. Enjoy.
