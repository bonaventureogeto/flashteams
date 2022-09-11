from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    "user serializer"
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
