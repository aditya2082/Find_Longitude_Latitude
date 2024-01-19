# location/serializers.py
from rest_framework import serializers

class ZipCodeSerializer(serializers.Serializer):
    zip_code = serializers.CharField(max_length=10)
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)
