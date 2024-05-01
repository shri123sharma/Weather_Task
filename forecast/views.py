from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.conf import settings
from .models import WeatherData
from .utils.api import fetch_weather_data
from .serializers import WeatherDataSerializer


class WeatherForecastAPIView(APIView):
    def post(self, request):
        # Deserialize the incoming data using WeatherDataSerializer
        serializer = WeatherDataSerializer(data=request.data)

        # Check if the deserialized data is valid
        if serializer.is_valid():
            # Extract latitude, longitude, and detailing_type from validated data
            latitude = serializer.validated_data.get("latitude")
            longitude = serializer.validated_data.get("longitude")
            detailing_type = serializer.validated_data.get("detailing_type")

            try:
                # Attempt to retrieve the latest weather data from the database
                weather_data = WeatherData.objects.filter(
                    latitude=latitude,
                    longitude=longitude,
                    detailing_type=detailing_type,
                ).latest("last_updated")

                # Check if the retrieved data is still valid based on expiry settings
                if (
                    timezone.now() - weather_data.last_updated
                ).total_seconds() / 60 <= settings.DATA_EXPIRY_MINUTES:
                    # Return the valid weather data
                    return Response(weather_data.data)
            except WeatherData.DoesNotExist:
                # If weather data is not found in the database, proceed to fetch from API
                pass

            # Fetch weather data from the external API
            fetched_data = fetch_weather_data(latitude, longitude, detailing_type)

            if fetched_data:
                # If data is successfully fetched, store it in the database
                WeatherData.objects.create(
                    latitude=latitude,
                    longitude=longitude,
                    detailing_type=detailing_type,
                    data=fetched_data,
                )
                return Response(fetched_data)
            # If fetching data from the API fails, return an error response
            return Response(
                "Failed to fetch weather data from OpenWeatherMap API",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        # If the incoming data is invalid, return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
