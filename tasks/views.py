from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskCreateView(LoginRequiredMixin, CreateAPIView):
    """
    Class-Based View to Create :Task objects
    """
    serializer_class = TaskSerializer
    renderer_classes = [TemplateHTMLRenderer]

    """
    POST Method to create a :Task Object and save to SQLite Database
    """
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data)
            serializer.save()
            return Response(data={}, status=status.HTTP_201_CREATED, template_name='tasks/create-task.html')
        print(serializer.errors)
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    """
    GET Method to return HTML Page
    """
    def get(self, request):
        context = {'user': request.user}
        return Response(data=context, status=status.HTTP_201_CREATED, template_name='tasks/create-task.html')


class TaskListView(LoginRequiredMixin, ListAPIView):
    """
    Class-Based View to List :Task objects
    """
    serializer_class = TaskSerializer
    renderer_classes = [TemplateHTMLRenderer]
    """
    GET Method to retrieve all :Task objects in the SQLite Database
    """
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(instance=tasks, many=True)
        context = {'tasks': serializer.data, 'user': request.user}
        return Response(data=context, status=status.HTTP_201_CREATED, template_name='tasks/tasks.html')


class TaskDetailView(LoginRequiredMixin, APIView):
    """
    Class-Based View to Update a :Task and to delete a :Task
    """
    """
    HTTP PUT Method to update a :Task object in the SQLite Database
    """
    def put(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    HTTP DELETE Method to delete a :Task object in the SQLite Database
    """
    def delete(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        task.delete()
        context = {'message': "Task was successfully deleted"}
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)
