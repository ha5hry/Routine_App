from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Routine, Todo
from django.core.exceptions import ObjectDoesNotExist
from . import serializers
import requests
# Create your views here.
class RoutineTitleApiView(APIView):
    def post(self, request):
        routine_details_serializer = serializers.RoutineSerializer(data = request.data, context = {'request': request})
        if routine_details_serializer.is_valid():
            routine_details_serializer.save()
            return Response(routine_details_serializer.data)
        return Response(routine_details_serializer.errors)

class RoutineTaskAPIView(APIView):
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

# class MyRoutinesApiView(APIView):
#     def get(sef, request):
#         get_routines = Todo.objects.all(details_author = request.user)
#         serializer = serializers.TodoSerializer(get_routines)
#         return Response(serializers.data)

class CreateRoutineAPIView(APIView):
    def post(self, request):
        # This section handles the routine details models
        access_token = request.session.get('access_tokens')
        refresh_token = request.session.get('refresh_tokens')
        title = request.data.get('title')
        title_endpoint = 'http://127.0.0.1:8000/api/routine/title/'
        header = {'AUTHORIZATION': f'Bearer {access_token}'}
        data = {'title': request.data.get('title'), 'description': request.data.get('description')}
        title_response = requests.post(title_endpoint, json=data, headers=header)
        title_response_json = title_response.json()
        print(title_response_json)
        print(title_response.status_code)

        # This section is for The Todos models
        title_object = Routine.objects.get(title = title)
        title_slug = title_object.slug
        todo_endpoint = f'http://127.0.0.1:8000/api/create/routine/add/{title_slug}/'
        todo_response = requests.post(todo_endpoint, json={'activity_name': request.data.get('activity_name'), 'start_time': request.data.get('start_time'), 'end_time': request.data.get('end_time')})
        todo_endpoint_json = todo_response.json()
        print(title_slug)
        return Response(headers={"HX-Redirect": "/homepage/"})
