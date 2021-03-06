import mysql.connector
import yaml


class Database:
    def __init__(self):
        with open('config.yaml') as cfg_file:
            credentials = yaml.load(cfg_file, Loader=yaml.FullLoader)
        self.db = mysql.connector.connect(
            host=credentials['host'],
            user=credentials['user'],
            password=credentials['password']
        )

    def insert_dht22(self, data, hora, umidade, temperatura):
        cursor = self.db.cursor()
        sql = "INSERT INTO weather_station.dht22 (data, hora, umidade, temperatura) VALUES (%s, %s, %s, %s)"
        val = (data, hora, umidade, temperatura)
        cursor.execute(sql, val)
        self.db.commit()
        return print(cursor.rowcount, "Registros iseridos")

    def insert_pluviometer(self, data, hora, precipitacao):
        cursor = self.db.cursor()
        sql = "INSERT INTO weather_station.pluviometer (data, hora, precipitacao) VALUES (%s, %s, %s)"
        val = (data, hora, precipitacao)
        cursor.execute(sql, val)
        self.db.commit()
        return print(cursor.rowcount, "Registros iseridos")