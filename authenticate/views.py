from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from authenticate.serializers import UserSerializer


class LoginView(APIView):
    """
    Class-Based View to request login username and password and authenticate users.
    """
    renderer_classes = [TemplateHTMLRenderer]

    """
    POST Method to authenticate user
    """
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(instance=user)
            return HttpResponseRedirect('/tasks')
        else:
            context = {'message': 'The credentials you inputted are invalid', 'status': 'LOGIN_FAILED'}
        return Response(data=context, status=status.HTTP_400_BAD_REQUEST, template_name='authenticate/login.html')

    """
    GET Method to return HTML Page
    """
    def get(self, request):
        return Response(template_name='authenticate/login.html')


class RegisterView(CreateAPIView):
    """
    Class-Based View to register user's details to database
    """
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = UserSerializer

    """
    POST Method to receive User details
    Redirects to Login Page if Successful
    """
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {'user': serializer.data}
            return HttpResponseRedirect('/login')
        context = {'errors': serializer.errors, 'status': 'REGISTER_FAILED'}
        return Response(data=context, status=status.HTTP_400_BAD_REQUEST, template_name='authenticate/register.html')

    """
    GET Method to return HTML Register Page
    """
    def get(self, request):
        return Response(template_name='authenticate/register.html')


class LogoutView(APIView):
    """
    Class Based View to log user out and invalidate their session
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')
