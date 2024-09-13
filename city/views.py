import json
from rest_framework.response import Response
from rest_framework import views
from .serializers import CitySerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class CityPostalView(views.APIView):
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['codigo_municipio', 'nombre_municipio', 'codigo_postal']
    search_fields = ['codigo_municipio', 'nombre_municipio', 'codigo_postal']

    def get_data(self):
        with open('city/cities.json', 'r') as json_file:
            data = json.load(json_file)
        return data

    def filter_data(self, data, params):
        for field in self.filterset_fields:
            if params.get(field):
                data = [item for item in data if item.get(field) == params[field]]
        return data

    def search_data(self, data, search_term):
        if not search_term:
            return data
        search_term = search_term.lower()
        return [
            item for item in data
            if any(search_term in str(value).lower() for value in item.values())
        ]

    def get(self, request, *args, **kwargs):
        data = self.get_data()
        data = self.filter_data(data, request.query_params)
        search_term = request.query_params.get('search')
        data = self.search_data(data, search_term)
        serializer = CitySerializer(data, many=True)
        return Response(serializer.data)
