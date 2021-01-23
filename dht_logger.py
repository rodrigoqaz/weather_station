import time
import Adafruit_DHT
from db_conn import Database

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

database = Database()

print(time.strftime('%Y-%m-%d'), time.strftime('%H:%M:%S'))

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        database.insert_dht22(
            data=time.strftime('%Y-%m-%d'),
            hora=time.strftime('%H:%M:%S'),
            umidade=humidity,
            temperatura=temperature
        )
    else:
        print("falha ao coletar dados do sensor")

    time.sleep(60)