# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser

# Serializers
from posts.serializers import (PostModelSerializer, PostSerializer)

class PostViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = PostModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

        
    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        data = PostModelSerializer(post).data
        return Response(data, status=status.HTTP_201_CREATED)
        