Template for uploading data to thingspeak channel 
"""
import sys
import random
import time
import urllib3

#for using temperature and humidity sensor
#import Adafruit_DHT as dht

# Enter API key here
myAPI=''
# URL where we will send the data
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
"""
def DHT22_data():
    temp,humid = dht.read_retry(dht.DHT22,18)
    return temp,humid
"""
def getdata():
     # Dummy glucose and blood pressure data
     sugar=random.randrange(90,200)
     bp=random.randrange(100,140)
     return sugar,bp
print("Exit logging data logging with Ctrl+c")
while True:
    try:
        sugar,bp=getdata()
        print('Sugar={0:0.1f} mg/dl Systolic={1:0.1f} mm Hg'.format(sugar,bp))
        #Sending the data to thingspeak cloud
        connection=urllib3.PoolManager()
        response=connection.request('GET',baseURL+'&field1=%s&field2=%s' % (sugar,bp))
        print("Connection Response :",response.status)
        #
        time.sleep(5)
    except KeyboardInterrupt:
        sys.exit()
