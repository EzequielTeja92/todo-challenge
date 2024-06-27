from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .helpers import validate_username, validate_email_address, validate_first_name, validate_last_name

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(validators=[validate_email_address])
    username = serializers.CharField(validators=[validate_username])
    first_name = serializers.CharField(validators=[validate_first_name])
    last_name = serializers.CharField(validators=[validate_last_name])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            return user
        except Exception as e:
            raise serializers.ValidationError({"detail": "Error creating user"})
