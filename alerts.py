# -*- coding: utf-8 -*-
class Alert:
    def __init__(self):
        self.thresholds = {
            'temperature': 35,  # Celsius
        }
        self.alert_triggered = False
    
    def check_alerts(self, data):
        if data['temp'] > self.thresholds['temperature']:
            if not self.alert_triggered:
                print(f"Alert! {data['city']} temperature exceeds threshold: {data['temp']}�C")
                self.alert_triggered = True
        else:
            self.alert_triggered = False
