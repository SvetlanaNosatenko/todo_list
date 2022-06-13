from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = ["id", "username", "first_name", "last_name", "email"]


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = User
        read_only_fields = ("id",)
        fields = ["id", "username", "first_name", "last_name", "email", "password", "password_repeat"]

    def validate(self, attrs: dict):
        password: str = attrs.get("password")
        password_repeat: str = attrs.pop("password_repeat")
        if password != password_repeat:
            raise ValidationError('Password and password_repeat is not equal')
        return attrs

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs: dict):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError("Username or password is incorrect")
        return user


class UpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password], required=True)

    class Meta:
        model = User
        read_only_field = ["id"]
        fields = ["old_password", "new_password"]

    def validate(self, attrs: dict):
        old_password = attrs.get("old_password")
        user: User = self.context['request'].user
        if not user.check_password(old_password):
            raise ValidationError({"old_password": "is incorrect"})
        return attrs

    def save(self, **kwargs):
        user: User = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save(update_fields=["password"])
        return user
