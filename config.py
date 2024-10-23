# config.py
OPENWEATHERMAP_API_KEY = '2ad150e4b5fefe4cbd96239f72eef47e'
LOCATIONS = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
API_CALL_INTERVAL = 300  # Interval to call the API (in seconds, 5 minutes)
TEMP_THRESHOLD = 35  # Alert if temperature exceeds this value
ALERT_CONSECUTIVE_UPDATES = 2  # Number of consecutive updates that need to breach the threshold
DATABASE_FILE = 'weather_data.db'  # SQLite database file

