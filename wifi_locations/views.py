from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WifiLocation,Address
from .serializers import LocationsSerializer,AddressSerializer
from wifi_wander_api.permissions import IsOwnerOrReadOnly

class LocationList(APIView):

    def get(self, request):
        profiles = WifiLocation.objects.all()
        serializer = LocationsSerializer(
            profiles, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        data=request.data
        # data['added_by'] = request.user.id
        serializer = LocationsSerializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(added_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Location(APIView):
    def get_object(self, pk):
        try:
            profile = WifiLocation.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except WifiLocation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = LocationsSerializer(
            profile, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = LocationsSerializer(
            profile, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        profile = self.get_object(pk)
        
        try:
            profile.delete()
        except:
           return Response({"msg":"Wifi Location not found"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"msg":"Wifi Location Deleted"})
    

class AddressList(APIView):

    def get(self, request):
        profiles = Address.objects.all()
        serializer = AddressSerializer(
            profiles, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        data=request.data
        # data['added_by'] = request.user.id
        serializer = AddressSerializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)