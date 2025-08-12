#!/usr/bin/env python3
"""
WeatherBot - Automated weather reporting and reminder system
"""

import os
import json
import logging
import time
from dotenv import load_dotenv
from modules.weather_api import WeatherAPI
from modules.notifier import Notifier
from modules.scheduler import Scheduler

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("weatherbot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class WeatherBot:
    """Main WeatherBot class that orchestrates the weather reporting system"""
    
    def __init__(self, config_path="config.json"):
        """Initialize WeatherBot with configuration"""
        logger.info("Starting WeatherBot")
        
        # Load environment variables
        load_dotenv()
        
        # Load configuration
        try:
            with open(config_path, 'r') as config_file:
                self.config = json.load(config_file)
            logger.info("Configuration loaded successfully")
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            raise
        
        # Initialize components
        self.api_key = os.getenv("WEATHER_API_KEY")
        if not self.api_key:
            logger.error("Weather API key not found in environment variables")
            raise ValueError("Weather API key not found")
        
        self.weather_api = WeatherAPI(self.api_key)
        self.notifier = Notifier(self.config["notification_methods"])
        self.scheduler = Scheduler()
        
    def get_weather_for_locations(self):
        """Fetch weather data for all configured locations"""
        weather_data = {}
        
        for location in self.config["locations"]:
            try:
                data = self.weather_api.get_weather(location)
                weather_data[location] = data
                logger.info(f"Weather data fetched for {location}")
            except Exception as e:
                logger.error(f"Error fetching weather for {location}: {e}")
        
        return weather_data
    
    def check_alerts(self, weather_data):
        """Check if any weather conditions meet alert thresholds"""
        alerts = []
        thresholds = self.config["alert_thresholds"]
        
        for location, data in weather_data.items():
            if data["temperature"] > thresholds["temperature_high"]:
                alerts.append(f"High temperature alert in {location}: {data['temperature']}°F")
            
            if data["temperature"] < thresholds["temperature_low"]:
                alerts.append(f"Low temperature alert in {location}: {data['temperature']}°F")
            
            if data["precipitation_chance"] > thresholds["precipitation_chance"]:
                alerts.append(f"High precipitation chance in {location}: {data['precipitation_chance']}%")
        
        return alerts
    
    def send_daily_report(self):
        """Send daily weather report to users"""
        logger.info("Preparing daily weather report")
        weather_data = self.get_weather_for_locations()
        
        if not weather_data:
            logger.warning("No weather data available for report")
            return
        
        # Format the report
        report = "Daily Weather Report\n\n"
        for location, data in weather_data.items():
            report += f"=== {location} ===\n"
            report += f"Temperature: {data['temperature']}°F\n"
            report += f"Condition: {data['condition']}\n"
            report += f"Humidity: {data['humidity']}%\n"
            report += f"Wind: {data['wind_speed']} mph\n"
            report += f"Precipitation Chance: {data['precipitation_chance']}%\n\n"
        
        # Check for alerts
        alerts = self.check_alerts(weather_data)
        if alerts:
            report += "ALERTS:\n"
            for alert in alerts:
                report += f"- {alert}\n"
        
        # Send the report
        self.notifier.send_notification("Weather Report", report)
        logger.info("Daily weather report sent")
    
    def run(self):
        """Run the WeatherBot"""
        logger.info("WeatherBot running")
        
        # Schedule daily reports
        self.scheduler.schedule_daily(self.send_daily_report)
        
        # Keep the bot running
        try:
            while True:
                self.scheduler.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("WeatherBot stopped by user")
        except Exception as e:
            logger.error(f"Error in WeatherBot: {e}")
            raise

if __name__ == "__main__":
    bot = WeatherBot()
    bot.run()
