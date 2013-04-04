import serial
import time
import random
import requests
import json
import re
import logging
from datetime import datetime

logging.basicConfig(filename='base_log.txt', level=logging.DEBUG)
logging.debug('Base started on {date}'.format(date=datetime.now()))
url = "http://plantr.herokuapp.com/logs"
extract_regex = re.compile(r"i([\w\-]{11})l(\d{1,4})m(\d{1,4})")

while (True):
  print "Waiting"
  ser = serial.Serial('/dev/ttyACM0', 9600)
  
  line = ser.readline()
  extracted = extract_regex.match(line)
  if extracted:
    values = {'sensor_id': extracted.group(1),
            'log[sunlight]': extracted.group(2),
            'log[moisture]': extracted.group(3),
            'log[temperature]': random.randint(30, 70)}
    logging.info(values)
    print values;
    r = requests.post(url, data=values)
  else:
    logging.warning('No regex match! Read {ser_line}'.format(ser_line = line))
  ser.flushInput();
