# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import Adafruit_DHT
import time

DHTSensor = Adafruit_DHT.DHT11

GPIO_PIN = 23

while True:
        humidity,temperature = Adafruit_DHT.read_retry(DHTSensor, GPIO_PIN)
        print 'Temperature : {:.1f}°C, Humidity : {:.1f}%'.format(temperature,humidity)
        time.sleep(0.5)