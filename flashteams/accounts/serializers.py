from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    """
    serializer class for team
    """
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)

    class Meta:
        model = Team
        fields = ["name", "description"]

    def create(self, validated_data):
        return Team.objects.create(**validated_data)
