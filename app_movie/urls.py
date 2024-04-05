from django.urls import path

from .views import MovieListAPIView, MovieDetailAPIView, MovieCreateAPIView


urlpatterns = [
    path('create/', MovieCreateAPIView.as_view()),
    path('<int:pk>/', MovieDetailAPIView.as_view()),
    path('', MovieListAPIView.as_view()),
]