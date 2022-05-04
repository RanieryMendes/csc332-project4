from flask import Flask, render_template, request, Response, jsonify,make_response 
import datetime

import Adafruit_DHT

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
   now = datetime.datetime.now()
   timeString = now.strftime("%d-%m-%Y %H:%M")
   t,humidity=read_sensor()
   templateData = {
      'title' : 'HELLO!',
      'time': timeString,
      'temp':t,
      'hum':humidity
      }
   return render_template('index.html', **templateData)

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
   app.run(host='0.0.0.0', port=80, debug=True)