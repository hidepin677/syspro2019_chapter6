#!/usr/bin/env python

import cgi
import cgitb
import time
import RPi.GPIO as GPIO

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<input type="number" name="degree">')
print('<input type="submit" name="submit">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(degree):
        set=9.5/180*(90+degree)+2.5
        servo.ChangeDutyCycle(set)
	time.sleep(0.5)
form = cgi.FieldStorage()
value = form.getvalue("degree")
print(int(value))
setservo(int(value))
print(int(value))
GPIO.cleanup()
