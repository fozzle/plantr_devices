import serial
import time
import random
import requests
import json
import re

url = "http://plantr.herokuapp.com/logs"
extract_regex = re.compile(r"i([\w\-]{11})l(\d{3})m(\d{3})")

while (True):
  print "Awake!"
  ser = serial.Serial('/dev/ttyACM0', 9600)

  line = extract_regex.match(ser.readline())
  if line:
    values = {'sensor_id': line.group(1),
            'log[sunlight]': line.group(2),
            'log[moisture]': line.group(3),
            'log[temperature]': random.randint(30, 70)}
    print str(values)
    r = requests.post(url, data=values) 
    print "Sleeping now!"
    time.sleep(5)
