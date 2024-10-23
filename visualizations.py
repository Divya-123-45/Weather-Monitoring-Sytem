 # visualizations.py
import matplotlib.pyplot as plt
import sqlite3
import config

def plot_daily_weather(city):
    conn = sqlite3.connect(config.DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT temp, timestamp FROM weather_data
        WHERE city = ? ORDER BY timestamp
    ''', (city,))
    data = cursor.fetchall()
    conn.close()

    temps = [row[0] for row in data]
    timestamps = [row[1] for row in data]
    
    plt.plot(timestamps, temps, label=f'Temperature in {city}')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Trend for {city}')
    plt.legend()
    plt.show()

