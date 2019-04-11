# importing packages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

# importing models
from .models import dim_movie

# importing serializers
from .serializers import MovieListSerializer


# API for returning list of all movies available in database
class movieList(APIView):
    def get(self,request):
        # retuns objects for all records in the model
        query_result = dim_movie.objects.all()
        # Formatting query result to create a list of dictionaries
        serialized_data = MovieListSerializer(query_result,many=True).data

        # return response in API
        return JsonResponse(
            {"content" : serialized_data,
            "status" : status.HTTP_200_OK},
            safe=False)