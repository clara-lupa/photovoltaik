from django.shortcuts import render
from rest_framework import viewsets
from yields.models import PvYield
from yields.serializers import PvYieldSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PvYieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PvYield.objects.all()
    serializer_class = PvYieldSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state']
