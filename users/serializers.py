"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Models
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

class UserLoginSerializer(serializers.Serializer):

    # Required fields
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Data validation
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key