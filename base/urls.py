from django.urls import path
from . import views


urlpatterns = [
    path('filmes/', views.FilmesAPIView.as_view(), name='filmes'),
    path('filme/<int:id>', views.FilmeDetailAPIView.as_view(), name='filme'),
]

