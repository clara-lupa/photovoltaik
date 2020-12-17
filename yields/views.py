from rest_framework import viewsets
from yields.models import PvYield
from django.http import JsonResponse
import geocoder


class PvYieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PvYield.objects.all()

    def list(self, request):

        if {'plz', 'capacity'} <= request.query_params.keys():
            return JsonResponse(self.__pv_system_yield(request.query_params['plz'], request.query_params['capacity']))

        elif 'state' in request.query_params.keys():
            return JsonResponse(self.__federal_state_yield(request.query_params['state']))


        err = {'error_message': 'Please enter a valid query.'}
        return JsonResponse(err)

    def __federal_state_yield(self, state):
        try:
            pv_yield = PvYield.objects.get(state=state)
        except:
            return {'error_message': 'The state code you entered does not exist.'}

        return {'yield': pv_yield.spec_yield, 'state': pv_yield.state}

    def __pv_system_yield(self, plz, capacity):
        geocoder_query = '{}, Germany'.format(plz)
        try:
            state_full = geocoder.osm(geocoder_query).osm['addr:state']
            pv_yield = PvYield.objects.get(state_full=state_full)
        except:
            return {'error_message': 'The postcode you entered does not exist.'}

        try:
            capacity_as_int = int(capacity)
        except:
            return {'error_message': 'The capacity value you entered is not a number.'}

        system_yield = capacity_as_int * pv_yield.spec_yield
        return {'yield': system_yield, 'state': pv_yield.state}
