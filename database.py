import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name='weather_data.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        
    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT,
                    temp REAL,
                    feels_like REAL,
                    weather_condition TEXT,
                    dt INTEGER
                )
            ''')
    
    def store_weather_data(self, data):
        with self.conn:
            self.conn.execute('''
                INSERT INTO weather (city, temp, feels_like, weather_condition, dt)
                VALUES (?, ?, ?, ?, ?)
            ''', (data['city'], data['temp'], data['feels_like'], data['weather_condition'], data['dt']))
