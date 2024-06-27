from rest_framework import generics
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import make_aware
from django.db.models import Q
import logging
from datetime import datetime
from django.shortcuts import get_object_or_404


logger = logging.getLogger(__name__)

class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Task.objects.all()

        created_at__gte = self.request.query_params.get('created_at__gte', None)
        if created_at__gte:
            try:
                created_at__gte = make_aware(datetime.strptime(created_at__gte, '%Y-%m-%dT%H:%M:%S.%fZ'))
                queryset = queryset.filter(created_at__gte=created_at__gte)
            except ValueError:
                return Response({"detail": "Invalid date format. Use ISO format: YYYY-MM-DDTHH:MM:SS.sssZ"}, status=status.HTTP_400_BAD_REQUEST)

        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))

        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Error creating task"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            task = get_object_or_404(Task, pk=pk)
            serializer = TaskSerializer(instance=task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating task: {e}")
            return Response({"detail": "Error updating task"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LabelListCreateView(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]

class LabelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated]
