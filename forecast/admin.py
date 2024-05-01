from django.contrib import admin
from .models import WeatherData


class WeatherDataAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the WeatherData model.
    This class defines how the WeatherData model is displayed
    and edited in the admin interface.
    """

    list_display = ("latitude", "longitude", "detailing_type", "last_updated")
    fields = ("latitude", "longitude", "detailing_type", "data")
    exclude = ("last_updated",)


admin.site.register(WeatherData, WeatherDataAdmin)
