from rest_framework.generics import GenericAPIView, CreateAPIView
from authentication.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status


class RegistrationAPIView(GenericAPIView):
    """Register new users."""

    serializer_class = RegistrationSerializer

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



