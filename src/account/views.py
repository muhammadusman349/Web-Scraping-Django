from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializers import SigninSerializer, SignupSerializer


class SignupView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/signup.html')

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('signin-view')
        return render(request, 'auth/signup.html', {'errors': serializer.errors})


class SigninView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/signin.html')

    def post(self, request, *args, **kwargs):
        serializer = SigninSerializer(data=request.data)
        if serializer.is_valid():
            # Handle successful sign in (e.g., set session or token)
            return redirect('index')
        return render(request, 'auth/signin.html', {'errors': serializer.errors})


def index(request):
    return render(request, 'auth/index.html')
