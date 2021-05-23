from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from uuid_generator.manager import RandomGeneratorDao
from uuid_generator.models import RandomGenerator


class RandomGeneratorViewSet(viewsets.ViewSet, generics.GenericAPIView):
    model = RandomGenerator

    def get_queryset(self):
        return RandomGeneratorDao.fetch_all_uuids() + RandomGeneratorDoa.generate_uuid()

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
