# Django REST Framework
from rest_framework import serializers
from django.core.validators import FileExtensionValidator

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
            'image',
        )

class PostSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    body = serializers.CharField(max_length=10000)
    image = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        required=False
    )

    def validate(self, data):
        image = None
        if 'image' in data:
            image = data['image']

        if image:
            if image.size > (1024 * 1024):
                raise serializers.ValidationError(
                    f"La imagen es demasiado grande, el peso máximo permitido es de 512KB y el tamaño enviado es de {round(image.size / 1024)}KB"
                )
        
        return data

    def create(self, data):

        post = Post.objects.create(**data)
        return post