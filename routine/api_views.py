from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Routine, Todo
from django.core.exceptions import ObjectDoesNotExist
from . import serializers
import requests
from common import permissions
# Create your views here.
class RoutineTitleApiView(APIView):
    permission_classes =[permissions.AccessPermission]
    def post(self, request):
        routine_details_serializer = serializers.RoutineSerializer(data = request.data, context = {'request': request})
        if routine_details_serializer.is_valid():
            routine_details_serializer.save()
            return Response(routine_details_serializer.data)
        return Response(routine_details_serializer.errors)
    
    def patch(self, request, routine_slug):
        try:
            get_routine_details = Routine.objects.get(slug=routine_slug)
        except ObjectDoesNotExist:
            return Response({'message': "Routine can't be found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user != get_routine_details.author:
                return Response({'message':'This can only be edited by the owner'},  status=status.HTTP_403_FORBIDDEN )
            routine_details_serializer = serializers.RoutineSerializer( get_routine_details, data = request.data, context = {'request': request}, partial = True)
            if routine_details_serializer.is_valid():
                routine_details_serializer.save()
                return Response(routine_details_serializer.data)
            return Response(routine_details_serializer.errors)

class RoutineTaskAPIView(APIView):
    permission_classes =[permissions.AccessPermission]
    def post(self, request, routine_slug):
        get_routine = Routine.objects.get(slug = routine_slug)
        serializer = serializers.TodoSerializer(data = request.data, context={'request':request, 'routine_slug': routine_slug})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request, routine_slug):
        get_routine_details = Routine.objects.get(slug = routine_slug)
        get_routine = Todo.objects.get(details = get_routine_details)
        serializer = serializers.TodoSerializer(get_routine)

        return Response(serializer.data)

    def patch(self, request, routine_slug):
        try:
            get_routine = Todo.objects.get(details__slug=routine_slug)
        except ObjectDoesNotExist:
            return Response({'message': "Task can't be found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user != get_routine.details.author:
                return Response({'message':'This can only be edited by the owner'},  status=status.HTTP_403_FORBIDDEN )
            serializer = serializers.TodoSerializer( get_routine, data = request.data, context={'request':request, 'routine_slug': routine_slug}, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

class DeleteRoutineApiView(APIView):
    permission_classes = [permissions.AccessPermission]
    def delete(self,request, routine_slug):

        try:
            get_routine_details = Routine.objects.get(slug=routine_slug)
        except ObjectDoesNotExist:
            return Response({'message': "Routine can't be found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user != get_routine_details.author:
                return Response({'message':'This can only be edited by the owner'},  status=status.HTTP_403_FORBIDDEN )
            get_routine_details.delete()
            return Response("Routine deleted")




class RoutinesAPIView(APIView):
    permission_classes = [permissions.AccessPermission]
    def get(self, request):
        instance = Routine.objects.filter(author = request.user)
        task_instance = Todo.objects.filter (details__author = request.user)
        serializer =serializers.RoutineSerializer(instance, many = True)
        task_serializer = serializers.TodoSerializer(task_instance, many=True)
        return Response({"Title Data":serializer.data,  "task Data":task_serializer.data})

class TasksAPIView(APIView):
    permission_classes = [permissions.AccessPermission]
    def get(self, request, routine_slug):
        instance = Todo.objects.filter(details__slug = routine_slug)
        serializer =serializers.TodoSerializer(instance, many = True)
        return Response(serializer.data)
