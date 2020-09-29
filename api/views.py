from django.shortcuts import rendere
from rest_framework.response import Response 
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

# Create your views here.

class MovieSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = (MovieSerializer)
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            response = {'message': 'ishladi'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'error'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = (RatingSerializer)

    