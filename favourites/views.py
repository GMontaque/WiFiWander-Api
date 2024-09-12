from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Favourites
from .serializers import FavouritesSerializer
from wifi_locations.models import WifiLocation
from django.http import Http404

class FavouritesList(APIView):
    """
    List all favourites for the current user or create a new one.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        favourites = Favourites.objects.filter(user=user)
        serializer = FavouritesSerializer(favourites, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        wifi_location_id = data.get('wifi_location_id')

        if not wifi_location_id:
            return Response({"detail": "WiFi location ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            wifi_location = WifiLocation.objects.get(id=wifi_location_id)
        except WifiLocation.DoesNotExist:
            return Response({"detail": "WiFi location not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FavouritesSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user, wifi_location=wifi_location)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FavouritesDetail(APIView):
    """
    Retrieve, update, or delete a favourite instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            favourite = Favourites.objects.get(pk=pk, user=self.request.user)
            return favourite
        except Favourites.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        favourite = self.get_object(pk)
        serializer = FavouritesSerializer(favourite)
        return Response(serializer.data)

    def delete(self, request, pk):
        favourite = self.get_object(pk)
        favourite.delete()
        return Response({"msg": "WiFi Location Removed"}, status=status.HTTP_204_NO_CONTENT)
