import requests
import logging
from django.conf import settings
from .weather_constants import BASE_URL

# Configure logging
logging.basicConfig(level=logging.ERROR)


def fetch_weather_data(latitude, longitude, detailing_type):
    '''
    
    '''
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = f"{BASE_URL}?lat={latitude}&lon={longitude}&appid={api_key}"

    _detailing_type = detailing_type.lower()
    if _detailing_type == "current":
        url = f"{base_url}&exclude=minutely,hourly,daily"
    elif _detailing_type == "minute forecast":
        url = f"{base_url}&exclude=current,hourly,daily"
    elif _detailing_type == "hourly forecast":
        url = f"{base_url}&exclude=current,minutely,daily"
    elif _detailing_type == "daily forecast":
        url = f"{base_url}&exclude=current,minutely,hourly"
    else:
        url = base_url

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as err:
        logging.error("Error fetching weather data: %s", err)
