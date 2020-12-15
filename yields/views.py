from django.shortcuts import render
from rest_framework import viewsets
from yields.models import PvYield
from yields.serializers import PvYieldSerializer

class PvYieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PvYield.objects.all()
    serializer_class = PvYieldSerializer
