# location/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests

from .serializers import ZipCodeSerializer

class ZipCodeView(APIView):
    def get(self, request):
        serializer = ZipCodeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        zip_code = serializer.validated_data['zip_code']

        # Call a geocoding service, for example, OpenStreetMap Nominatim
        url = f'https://nominatim.openstreetmap.org/search?format=json&limit=1&postalcode={zip_code}'
        headers = {'User-Agent': 'YourAppName/1.0 (your@email.com)'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data:
                location = data[0]
                serializer.validated_data['latitude'] = float(location.get('lat'))
                serializer.validated_data['longitude'] = float(location.get('lon'))
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Location not found for the given zip code'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Failed to fetch location data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
