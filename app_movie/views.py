from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieDetailSerializer


# Create your views here.
class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class MovieCreateAPIView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer