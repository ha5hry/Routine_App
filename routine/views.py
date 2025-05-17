from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Routine, Todo
import random, string
from . import serializers
# Create your views here.
class RoutineApiView(APIView):
    def post(self, request):
        serializer = serializers.RoutineSerializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)