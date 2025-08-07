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

class CreateRoutineAPIView(APIView):
    permission_classes =[permissions.AccessPermission]
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

class EditRoutineLinkAPIView(APIView):

    def post(self, request, routine_slug ):
        form_data = request.data
        edited_data ={}
        for key, value in form_data.items():
            # The If block filter out the incoming request if the value of the key are none or an empty string
            if value is not None and value!= '':
                # append the the key and value to the edited_data dictionary. NOTE: These are the fields the users tends to edit
                edited_data[key] = value

        try:
            routine = Todo.objects.get(details__slug=routine_slug)
        except ObjectDoesNotExist:
            return Response("Routine not found")
        else:
            # access_token and refresh_token this get the user token from session cokes
            access_token = request.session.get('access_tokens')
            refresh_token = request.session.get('refresh_tokens')
            header = {"AUTHORIZATION": f"Bearer {access_token}"}
            edit_title_endpoint = f"http://127.0.0.1:8000/api/edit/routine/{routine_slug}/"

            edit_activity_endpoint = f'http://127.0.0.1:8000/api/edit/tasks/{routine_slug}/'
            title_keys = ['title', 'description']
            tasks_keys= ['activity_name', 'start_time', 'end_time']

            title_section_data = {}
            tasks_section_data = {}
            # for this for block, we need to separate the data going to the  edit_title_endpoint and  edit_activity_endpoint, separating the data by their keys
            for key, value in edited_data.items():
                if key in title_keys:
                    title_section_data[key] = value
                elif key in tasks_keys:
                    tasks_section_data[key] = value
                else:
                    pass
            title_section_data_response = requests.patch(edit_title_endpoint, json=title_section_data, headers=header)
            tasks_section_data_response = requests.patch(edit_activity_endpoint, json=tasks_section_data, headers=header)
        return Response({'Title Section':title_section_data_response.json(), 'task Section': tasks_section_data_response.json()})

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
