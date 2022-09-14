from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer


class TeamCreateListAPIView(ListCreateAPIView):
    """
    create a team
    """

    serializer_class = TeamSerializer
    queryset = Team

    def get_queryset(self):
        return Team.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data = serializer.data

        return Response(data)
