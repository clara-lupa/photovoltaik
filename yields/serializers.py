from rest_framework import serializers
from yields.models import PvYield

class PvYieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = PvYield
        fields = ['state', 'spec_yield']
