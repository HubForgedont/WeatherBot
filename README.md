```markdown
# WeatherBot 🌦️

WeatherBot is an automated weather reporting and reminder system that provides real-time weather updates, daily forecasts, and severe weather alerts through customizable notifications.

## 🌟 Features

- **Real-time Weather Data**: Fetches current weather conditions from OpenWeatherMap API
- **Daily Reports**: Automated daily weather summaries delivered at your preferred time
- **Weather Alerts**: Instant notifications for extreme weather conditions
- **Multi-location Support**: Monitor weather for multiple cities simultaneously
- **Customizable Notifications**: Choose between email, push notifications, or both
- **Configurable Thresholds**: Set your own temperature and precipitation alert thresholds

## 📋 Requirements

- Python 3.7+
- OpenWeatherMap API key (free tier available)
- Email account for notifications (optional)

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/HubForgedont/weatherbot.git

# Navigate to the project directory
cd weatherbot

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env file with your API keys and settings
```

### Configuration

Edit the `config.json` file to customize your settings:

```json
{
  "locations": ["New York", "London", "Tokyo"],
  "update_frequency": "daily",
  "notification_methods": ["email", "push"],
  "alert_thresholds": {
    "temperature_high": 95,
    "temperature_low": 32,
    "precipitation_chance": 70
  }
}
```

### Usage

```bash
# Run the bot
python weatherbot.py
```

For continuous operation, consider setting up as a service or using a process manager like PM2.

## 📊 Sample Output

### Daily Weather Report

```
Daily Weather Report

=== New York ===
Temperature: 72°F
Condition: Partly cloudy
Humidity: 65%
Wind: 8 mph
Precipitation Chance: 15%

=== London ===
Temperature: 61°F
Condition: Light rain
Humidity: 78%
Wind: 12 mph
Precipitation Chance: 75%

ALERTS:
- High precipitation chance in London: 75%
```

## 🛠️ Project Structure

```
weatherbot/
├── weatherbot.py         # Main application file
├── config.json           # Configuration settings
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── modules/
    ├── __init__.py
    ├── weather_api.py    # Weather API integration
    ├── notifier.py       # Notification system
    └── scheduler.py      # Scheduling system
```

## ⚙️ Advanced Configuration

### Environment Variables

Create a `.env` file with the following variables:

```
# Weather API credentials
WEATHER_API_KEY=your_openweathermap_api_key_here

# Email notification settings
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
FROM_EMAIL=your_email@gmail.com
TO_EMAIL=recipient@example.com
```

### Running as a Service

To run WeatherBot as a systemd service on Linux:

1. Create a service file:

```bash
sudo nano /etc/systemd/system/weatherbot.service
```

2. Add the following content:

```
[Unit]
Description=WeatherBot Service
After=network.target

[Service]
User=HubForgedont
WorkingDirectory=/path/to/weatherbot
ExecStart=/usr/bin/python3 /path/to/weatherbot/weatherbot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

3. Enable and start the service:

```bash
sudo systemctl enable weatherbot
sudo systemctl start weatherbot
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact

Project Link: [https://github.com/HubForgedont/weatherbot](https://github.com/HubForgedont/weatherbot)

## 🙏 Acknowledgements

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Python Requests Library](https://docs.python-requests.org/)
- [Schedule Library](https://schedule.readthedocs.io/)

---

created by https://x.com/HubForgeAI
