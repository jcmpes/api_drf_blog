# Django REST Framework
from rest_framework import serializers
# Model
from posts.models import Post

class PostModelSerializer(serializers.ModelSerializer):
    """Post Model Serializer"""

    class Meta:
        """Meta class."""

        model = Post
        fields = (
            'pk',
            'date',
            'title',
            'body',
        )

class PostSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    body = serializers.CharField(max_length=10000)

    def create(self, data):

        post = Post.objects.create(**data)
        return post