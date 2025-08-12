"""
Weather API module for fetching weather data
"""

import requests
import logging

logger = logging.getLogger(__name__)

class WeatherAPI:
    """Class for interacting with weather API services"""
    
    def __init__(self, api_key):
        """Initialize with API key"""
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, location):
        """
        Get current weather for a location
        
        Args:
            location (str): City name or location
            
        Returns:
            dict: Weather data
        """
        try:
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'imperial'  # For Fahrenheit
            }
            
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant weather information
            weather_data = {
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'precipitation_chance': data.get('pop', 0) * 100 if 'pop' in data else 0,
                'timestamp': data['dt']
            }
            
            return weather_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API request error: {e}")
            raise
        except (KeyError, ValueError) as e:
            logger.error(f"Error parsing weather data: {e}")
            raise
