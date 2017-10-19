from .models import Brewery
from .serializers import BrewerySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BreweryList(APIView):
    def get(self, request, format=None):
        breweries = Brewery.objects.all()
        serializer = BrewerySerializer(breweries, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = BrewerySerializer(data=request.data)
        if serializer.isValid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BreweryDetail(APIView):
    def get_object(self, pk):
        try:
            brewery = Brewery.objects.get(pk=pk)
        except Brewery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        brewery = self.get_object(pk)
        serializer = BrewerySerializer(brewery)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        brewery = self.get_object(pk)
        serializer = BrewerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brewery = self.get_object(pk)
        brewery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)