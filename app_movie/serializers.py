from rest_framework import serializers

from .models import Movie, Genre


class MovieSerializer(serializers.ModelSerializer):
    movie_detail_url = serializers.SerializerMethodField(read_only=True, source='get_movie_detail_url')

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'movie_year', 'movie_banner', 'movie_genre', 'movie_detail_url']
        depth = 1

    def get_movie_detail_url(self, obj):
        return f"http://localhost:8000/api/v1/movie/{obj.id}"


class MovieDetailSerializer(serializers.ModelSerializer):
    movie_genre_info = serializers.SerializerMethodField(read_only=True, source='get_movie_genre_info')

    class Meta:
        model = Movie
        fields = '__all__'
        # depth = 1

    def get_movie_genre_info(self, obj):
        info = {
            'genre_id': obj.movie_genre.id,
            'genre_name': obj.movie_genre.genre_name
        }
        return info