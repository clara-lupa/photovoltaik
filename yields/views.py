from django.shortcuts import render
from rest_framework import viewsets
from yields.models import PvYield
from yields.serializers import PvYieldSerializer
from django.http import HttpResponse, JsonResponse


class PvYieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PvYield.objects.all()

    def list(self, request):
        # has to be refactored
        print(request.query_params.keys())
        if "state" in request.query_params.keys():
            try:
                pv_yield = PvYield.objects.get(state=request.query_params['state'])
                response = {"yield": pv_yield.spec_yield, "state": pv_yield.state}
                return JsonResponse(response)
            except:
                err = {"error_message": "the state code you entered does not exist"}
                return JsonResponse(err)

        elif {"plz", "capacity"} <= request.query_params.keys():
            import geocoder
            geocoder_query = "{}, Germany".format(request.query_params['plz'])
            state_full = geocoder.osm(geocoder_query).osm['addr:state']
            try:
                pv_yield = PvYield.objects.get(state_full=state_full)
            except:
                err =  {"error_message": "the plz you entered does not exist",
                    "state_full": state_full}
                return JsonResponse(err)
            system_yield = int(request.query_params['capacity']) * int(pv_yield.spec_yield)
            response = {'yield': system_yield, 'state': pv_yield.state}
            return JsonResponse(response)

        err = {"error_message": "please enter a valid query"}
        return JsonResponse(err)
