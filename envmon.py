#!/usr/bin/python3
from gpiozero import CPUTemperature
from datetime import datetime
import Adafruit_DHT
import subprocess

# Threshold values to trigger an alert - adjust as desired 
CORE_ALERT = 60
TEMP_ALERT = 40
HUMID_ALERT = 95
ALERT = False

now = datetime.now()
datestamp = now.strftime("%Y%m%d %H:%M:%S")
cpu = CPUTemperature()
dhtSensor = Adafruit_DHT.DHT22
coreT = round( cpu.temperature, 1 )
scoreT = str( coreT )
if coreT >= CORE_ALERT:
   scoreT = "*" + scoreT
   ALERT = True

humid, ambiT = Adafruit_DHT.read_retry(dhtSensor, 4)

envmon = datestamp + " " + scoreT + " "

if humid is not None and ambiT is not None:
   shumid = str( round( humid, 1 ) )
   sambiT = str( round( ambiT, 1 ) )
   if humid >= HUMID_ALERT:
      shumid = "*" + shumid
      ALERT = True

   if ambiT >= TEMP_ALERT:
      sambiT = "*" + sambiT
      ALERT = True

   envmon = envmon + sambiT + " " + shumid
else:
   envmon = envmon + "Failed to read data from DHT22"

out = open( "/var/log/envmon.log", "a" )
out.write( envmon )
out.write( "\n" )
out.close()

command = 'echo ' + envmon + ' | mail -s "EnvMon Report" -a "From: admin@mail.net" you@mail.com'
if (ALERT == True):
   subprocess.call( command, shell=True )

