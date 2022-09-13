from rest_framework import serializers
from authentication.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    """
    serialize registration requests and create a new user
    """

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    role = serializers.ChoiceField(
        choices=[
            ("TL","TEAM LEAD"),
            ("TM", "TEAM MEMBER"),
        ]
    )

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        },
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "confirmed_password",
            "role",
        ]

    def validate(self, data):
        """
        Validate data before it gets saved
        """

        confirmed_password = data.get("confirmed_password")
        try:
            validate_password(data["password"])
        except ValidationError as identifier:
            raise serializers.ValidationError({"password": str(identifier).replace("[" ", " ").replace(" "]", "")})

        if not self.do_passwords_match(data["password"], confirmed_password):
            raise serializers.ValidationError({"passwords": ("Passwords do not match")})

        return data

    def create(self, validated_data):
        """
        create a user
        """
        del validated_data["confirmed_password"]
        return User.objects.create_user(**validated_data)

    def do_passwords_match(self, password1, password2):
        """
        Check if passwords match
        """
        return password1 == password2
