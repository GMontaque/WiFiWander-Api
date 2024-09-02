from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Favourites
from .serializers import FavouritesSerializer
from wifi_wander_api.permissions import IsOwnerOrReadOnly
from django.http import Http404

class FavouritesList(APIView):
    """
    List all favourites for the current user or create a new one.
    """

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        
        favourites = Favourites.objects.filter(user=user)
        serializer = FavouritesSerializer(favourites, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FavouritesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FavouritesDetail(APIView):
    """
    Retrieve, update or delete a favourite instance.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            favourite = Favourites.objects.get(pk=pk)
            self.check_object_permissions(self.request, favourite)
            return favourite
        except Favourites.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        favourite = self.get_object(pk)
        serializer = FavouritesSerializer(favourite)
        return Response(serializer.data)

    def put(self, request, pk):
        favourite = self.get_object(pk)
        serializer = FavouritesSerializer(
            favourite, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        favourite = self.get_object(pk)
        favourite.delete()
        return Response({"msg": "Wifi Location Removed"}, status=status.HTTP_204_NO_CONTENT)
