from django.shortcuts import render
from rest_framework import viewsets
from yields.models import PvYield
from yields.serializers import PvYieldSerializer
from django.http import HttpResponse, JsonResponse


class PvYieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PvYield.objects.all()

    def list(self, request):
        print(request.query_params.keys())
        err = {}
        if "state" in request.query_params.keys():
            try:
                pv_yield = PvYield.objects.get(state=request.query_params['state'])
                serializer = PvYieldSerializer(pv_yield)
                return JsonResponse(serializer.data, safe=False)
            except:
                err = {"error_message": "the state code you entered does not exist"}
                return JsonResponse(err)

        elif {"plz", "capacity"} <= request.query_params.keys():
            try:
                import geocoder
                geocoder_query = "{}, Germany".format(request.query_params['plz'])
                state = geocoder.osm(geocoder_query).osm['addr:state']
                return JsonResponse(state, safe=False)
            except:
                err =  {"error_message": "invalid query format"}

        return JsonResponse(err)
