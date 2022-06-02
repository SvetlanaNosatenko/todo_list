from django.contrib.auth import login, logout
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, UpdateAPIView, GenericAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.models import User
from core.serializers import LoginSerializer, UpdatePasswordSerializer, \
    CreateUserSerializer, \
    UserSerializer


class SignupView(CreateAPIView):
    model = User
    permission_classes = (AllowAny, )
    serializer_class = CreateUserSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request=request, user=user, backend='django.contrib.auth.backends.ModelBackend')
        return Response(serializer.data, status=200)


class ProfileView(RetrieveUpdateDestroyAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=204)


class UpdatePasswordView(UpdateAPIView):
    model = User
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user, backend='django.contrib.auth.backends.ModelBackend')
        return JsonResponse(data=serializer.data, status=200)
