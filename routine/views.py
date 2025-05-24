from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Routine, Todo
from django.core.exceptions import ObjectDoesNotExist
from . import serializers
# Create your views here.
class RoutineTitleApiView(APIView):
    def post(self, request):
        routine_details_serializer = serializers.RoutineSerializer(data = request.data, context = {'request': request})
        if routine_details_serializer.is_valid():
            routine_details_serializer.save()
            return Response(routine_details_serializer.data)
        return Response(routine_details_serializer.errors)

class CreateRoutineAPIView(APIView):
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