from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from webapp import views
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from .serlizers import employeeSerializer


class emplyeeList(viewsets.ModelViewSet):
    def get(request,requrest):
        queryset = models.employee.objects.all()
        Serializer = employeeSerializer(queryset, many=True)
        return Response(Serializer.data)

    def post(self):
        pass
