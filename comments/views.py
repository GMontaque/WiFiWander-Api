from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comments
from .serializers import CommentSerializer
from wifi_wander_api.permissions import IsOwnerOrReadOnly

# View to handle listing all comments and creating new comments
class CommentList(APIView):

    # Handle GET request to list all comments
    def get(self, request):
        comments = Comments.objects.all()  # Retrieve all comments from the database
        serializer = CommentSerializer(
            comments, many=True, context={'request': request}
        )  # Serialize the comments into JSON format
        return Response(serializer.data)  # Return the serialized data in the response
    
    # Handle POST request to create a new comment
    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():  # Validate the data
            serializer.save(user=request.user)  # Save the comment, assigning the current user as the author
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created comment data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if the data is invalid
    

# View to handle retrieving, updating, or deleting a specific comment
class CommentDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]  # Restrict access to only allow owners to modify or delete their comments

    # Helper method to retrieve the comment by primary key (pk)
    def get_object(self, pk):
        try:
            comment = Comments.objects.get(pk=pk)  # Attempt to retrieve the comment by its ID
            self.check_object_permissions(self.request, comment)  # Check if the current user has permission to interact with the comment
            return comment
        except Comments.DoesNotExist:  # If the comment does not exist, raise a 404 error
            raise Http404

    # Handle GET request to retrieve a specific comment
    def get(self, request, pk):
        comment = self.get_object(pk)  # Get the comment using the helper method
        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data)  # Return the serialized comment data

    # Handle PUT request to update a specific comment
    def put(self, request, pk):
        comment = self.get_object(pk)  # Get the comment using the helper method
        serializer = CommentSerializer(
            comment, data=request.data, context={'request': request}
        )  # Serialize the updated data
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the updated comment
            return Response(serializer.data)  # Return the updated comment data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if the data is invalid
    
    # Handle DELETE request to delete a specific comment
    def delete(self, request, pk):
        comment = self.get_object(pk)  # Get the comment using the helper method
        comment.delete()  # Delete the comment from the database
        return Response({"msg": "Comment Deleted"}, status=status.HTTP_204_NO_CONTENT)  # Return a success message with no content
