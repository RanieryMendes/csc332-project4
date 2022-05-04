from mq import *
import sys, time
from flask import Flask, render_template, request, Response, jsonify,make_response 
import datetime

import Adafruit_DHT
mq = MQ();
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
   now = datetime.datetime.now()
   timeString = now.strftime("%d-%m-%Y %H:%M")
   t,humidity=read_sensor()
  
   perc = mq.MQPercentage()
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'temp':t, 
      'hum':humidity,
      'co': perc["CO"]
      }

   if((humidity > 93) and (t > 38) ):
      return render_template('index2.html',**templateData )

   if(perc["CO"]> 300):
      return render_template('index2.html',**templateData )
   
   return render_template('index2.html', **templateData)

def read_sensor(*args):
    try:
       
       humidity, temperature = Adafruit_DHT.read_retry(11,4)
      
       print('Temp: {0:0.1f}* C  Humidity: {1:0.1f} %'.format(temperature, humidity))
       t ='{0:0.1f}'.format(temperature)
       return t,humidity
    except Exception as e:
       print ('error '+str(e))
       GPIO.cleanup()

if __name__ == "__main__":
   app.run(host='10.224.137.24', port=80, debug=True)