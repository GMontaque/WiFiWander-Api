from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WifiLocation
from .serializers import WifiLocationSerializer
from wifi_wander_api.permissions import IsOwnerOrReadOnly

class LocationList(APIView):
    """
    View to list all wifi locations and create a new wifi location.
    """

    def get(self, request):
        """
        Return a list of all wifi locations.
        """
        locations = WifiLocation.objects.all()
        serializer = WifiLocationSerializer(locations, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        """
        Create a new wifi location.
        """
        serializer = WifiLocationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(added_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Location(APIView):
    """
    View to retrieve, update, or delete a wifi location.
    """

    def get_object(self, pk):
        """
        Helper method to get the object with given pk.
        """
        try:
            location = WifiLocation.objects.get(pk=pk)
            self.check_object_permissions(self.request, location)
            return location
        except WifiLocation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a wifi location by id.
        """
        location = self.get_object(pk)
        serializer = WifiLocationSerializer(location, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a wifi location by id.
        """
        location = self.get_object(pk)
        serializer = WifiLocationSerializer(location, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Delete a wifi location by id.
        """
        location = self.get_object(pk)
        location.delete()
        return Response({"msg": "Wifi Location Deleted"}, status=status.HTTP_204_NO_CONTENT)
