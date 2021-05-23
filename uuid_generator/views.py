from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from uuid_generator.manager import RandomGeneratorDao
from uuid_generator.models import RandomGenerator
from uuid_generator.serializers import RandomGeneratorSerializer


class RandomGeneratorViewSet(viewsets.ViewSet, generics.GenericAPIView):
    model = RandomGenerator
    serializer_class = RandomGeneratorSerializer

    def get_queryset(self):
        RandomGeneratorDao.generate_uuid()
        return RandomGeneratorDao.fetch_all_uuids()

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)
