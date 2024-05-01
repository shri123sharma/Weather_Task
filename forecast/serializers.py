from rest_framework import serializers


class WeatherDataSerializer(serializers.Serializer):
    # Define fields for latitude, longitude, and detailing_type
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    detailing_type = serializers.CharField(required=True)  # detailing_type is required

    # Custom validation to ensure detailing_type is present in the data
    def validate_detailing_type(self, data):
        if "detailing_type" not in data:
            raise serializers.ValidationError("detailing_type is required")
        return data

    # Convert latitude and longitude to internal values
    def to_internal_value(self, data):
        try:
            # Convert latitude and longitude to floats
            latitude = float(data.get("latitude"))
            longitude = float(data.get("longitude"))
            detailing_type = data["detailing_type"]  # Retrieve detailing_type
            return {
                "latitude": latitude,
                "longitude": longitude,
                "detailing_type": detailing_type,
            }
        except (ValueError, TypeError):
            # Raise validation error for invalid latitude or longitude
            raise serializers.ValidationError(
                {"error": "Invalid latitude or longitude"}
            )

    # Validate latitude to ensure it's within the range [-90, 90]
    def validate_latitude(self, value):
        if value < -90 or value > 90:
            raise serializers.ValidationError(
                "Latitude must be within the range -90 to 90"
            )
        return value

    # Validate longitude to ensure it's within the range [-180, 180]
    def validate_longitude(self, value):
        if value < -180 or value > 180:
            raise serializers.ValidationError(
                "Longitude must be within the range -180 to 180"
            )
        return value
