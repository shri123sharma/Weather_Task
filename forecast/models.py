from django.db import models


class WeatherData(models.Model):
    """
    Model to store weather data fetched from weather API.
    """

    latitude = models.FloatField(help_text="Latitude of the location")
    longitude = models.FloatField(help_text="Longitude of the location")
    detailing_type = models.CharField(max_length=20)
    data = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Weather data {self.latitude}-{self.longitude}-{self.detailing_type}"
