from django.urls import path
from .views import WeatherForecastAPIView

# Define URL patterns for the weather forecast API
urlpatterns = [
    # Endpoint for accessing weather forecast data
    path(
        "weather-forecast-api/",
        WeatherForecastAPIView.as_view(),
        name="weather_forecast",
    ),
]
