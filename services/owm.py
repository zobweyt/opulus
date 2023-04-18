"""Utility service for formatting the OpenWeatherMap API responses."""

from pyowm import OWM
from pyowm.utils import config
from pyowm.weatherapi25.observation import Observation
from pyowm.weatherapi25.location import Location
from pyowm.weatherapi25.weather import Weather

from opulus import settings

_config = config.get_default_config()
_config["language"] = "RU"

_owm = OWM(settings.OWM_API_KEY, _config)
weather_manager = _owm.weather_manager()

# Custom emojis for `Weather.weather_icon_name`.
# See details at https://openweathermap.org/weather-conditions.
EMOJIS = {
    "01d": "☀️", "01n": "🌑",  # clear sky
    "02d": "🌤️", "02n": "☁️",  # few clouds
    "03d": "☁️", "03n": "☁️",  # scattered clouds
    "04d": "⛅", "04n": "☁️",  # broken clouds
    "09d": "🌧️", "09n": "🌧️",  # shower rain
    "10d": "🌦️", "10n": "🌧️",  # rain
    "11d": "⛈️", "11n": "⛈️",  # thunderstorm
    "13d": "❄️", "13n": "❄️",  # snow
    "50d": "🌫️", "50n": "🌫️"   # mist
}


def format_observation(observation: Observation) -> str:
    weather: Weather = observation.weather
    location: Location = observation.location

    weather_emoji = EMOJIS.get(weather.weather_icon_name)
    weather_location = location.name or f"{location.lat}, {location.lon}"

    temperature = weather.temperature("celsius")
    average_temperature = round(temperature["temp"])
    temperature_feel = round(temperature["feels_like"])

    weather_status = weather.detailed_status.capitalize()
    wind = weather.wind()["speed"]

    message = f"{weather_emoji} *{weather_location} {average_temperature}°C*\n" \
              f"{weather_status}, ощущается как *{temperature_feel}°C*\n" \
              f"Ветер *{wind} м/c* · Влажность *{weather.humidity}*%"

    return message
