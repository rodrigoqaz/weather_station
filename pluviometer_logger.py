import RPi.GPIO as GPIO
import time
from db_conn import Database

#gpio.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(33, GPIO.RISING, bouncetime=300)

database = Database()

while True:
    if GPIO.event_detected(33):
        database.insert_pluviometer(
            data=time.strftime('%Y-%m-%d'),
            hora=time.strftime('%H:%M:%S'),
            precipitacao=2.5,
        )

