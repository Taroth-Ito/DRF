from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView


class HelloAPIView(APIView):
    def get(self, reqeust):
        data = {"message": "Hello from drf"}
        return Response(data)
