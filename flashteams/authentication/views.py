from rest_framework.generics import GenericAPIView, CreateAPIView
from authentication.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User


class RegistrationAPIView(GenericAPIView):
    """Register new users."""

    serializer_class = RegistrationSerializer
    queryset = User

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        response = {
            "data": {
                "user": user_data,
                "message": "user created successfully"
            }
        }

        return Response(response, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    """ api view fo log in """

    serializer_class = LoginSerializer
    queryset = User

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data

        repsonse = {
            "data": {
                "user": dict(user),
                "message": "You have successfuly logged in"
            }
        }

        return Response(repsonse, status=status.HTTP_200_OK)

