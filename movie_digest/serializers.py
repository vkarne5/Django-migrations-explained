from rest_framework import serializers

# importing models
from .models import dim_movie


# Serializer for generating list of movies available in database
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        # model to be returned
        model = dim_movie
        # select all fields of the model
        fields = ('__all__')

