from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Possibles
from .serializers import PossiblesSerializer
from wifi_wander_api.permissions import IsOwnerOrReadOnly

class PossiblesList(APIView):

    def get(self, request):
        possibles = Possibles.objects.all()
        serializer = PossiblesSerializer(
            possibles, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PossiblesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PossiblesDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            possibles = Possibles.objects.get(pk=pk)
            self.check_object_permissions(self.request, possibles)
            return possibles
        except Possibles.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        possibles = self.get_object(pk)
        serializer = PossiblesSerializer(possibles, context={'request': request})
        return Response(serializer.data)


    def put(self, request, pk):
        possibles = self.get_object(pk)
        serializer = PossiblesSerializer(
            possibles, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        possibles = self.get_object(pk)
        possibles.delete()
        return Response({"msg": "Wifi Location Removed"}, status=status.HTTP_204_NO_CONTENT)
