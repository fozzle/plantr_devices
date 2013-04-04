import serial
import time
import random
import requests
import json
import re
import logging
from datetime import datetime

url = "http://plantr.herokuapp.com/logs"
extract_regex = re.compile(r"i([\w\-]{11})l(\d{1,4})m(\d{1,4})")
moisture = 100
sensor_id = 'wIlNX4hvkDs'
sunlight = 70
incrementor = 20

while (True):
  print "Waiting"
  time.sleep(300)

  # FLip flop moisture just to trigger alerts
  if moisture < 500:
    moisture = 550
  else:
    moisture = 100

  # Have sunlight on a steady rise and fall
  if sunlight > 900 and incrementor > 0:
    incrementor = -20
  elif sunlight < 100 and incrementor < 0:
    incrementor = 20 
  sunlight += incrementor

  
  values = {'sensor_id': sensor_id,
            'log[sunlight]': sunlight,
            'log[moisture]': moisture,
            'log[temperature]': random.randint(30, 70)}
  r = requests.post(url, data=values)
  
 
