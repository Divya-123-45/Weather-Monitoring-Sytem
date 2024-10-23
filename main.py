# -*- coding: utf-8 -*-
import time
import weather_data
import database
import alerts

def main():
    # Configure your settings
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    api_key = '2ad150e4b5fefe4cbd96239f72eef47e'  # Replace with your API key
    interval = 300  # Interval in seconds (5 minutes)
    
    # Set up database
    db =database.Database()
    alert_system =alerts.Alert()
    
    while True:
        for city in cities:
            # Get weather data
            data = weather_data.get_weather_data(city, api_key)
            if data:
                print(f"Retrieved data for {data['city']}: Temp={data['temp']}degrees, "
                      f"Feels Like={data['feels_like']}degrees, Condition={data['weather_condition']}")
                # Process and store data
                db.store_weather_data(data)
                
                # Check alerts
                alert_system.check_alerts(data)
        
        # Wait for the next interval
        time.sleep(interval)

if __name__ == "__main__":
    main()
