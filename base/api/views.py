from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from base.models import Task
from .serializer import TaskSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Overviews
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail View': '/task-details/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        'token': '/api/token',
        'refresh': '/api/token/refresh',

    }
    return Response(api_urls)

# Get all Tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskList(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# Get a single detailed Tasks
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskDetails(request, pk):
    # task = Task.objects.get(id=pk, user=request.user)
    task = get_object_or_404(Task, pk=pk, user=request.user)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)

# Create a Tasks


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    # print(request.data)
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        task = Task.objects.create(
            title=request.data['title'], user=request.user)
        task.save()

    return Response(serializer.data)


# Edit a Tasks
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Delete a Tasks


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    if task.user == request.user:
        task.delete()
        return Response('Successfully deleted')
    else:
        return Response('Access Denied')
