from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from uuid_generator.models import RandomGenerator


class RandomGeneratorViewSet(viewsets.ViewSet, generics.GenericAPIView):
    model = RandomGenerator

    def list(self, request):
        pass
