from django.urls import path
from . import views


urlpatterns = [
    path('filmes/', views.filmes, name='filmes'),
    path('filme/<int:id>', views.filme_detail, name='filmes'),
]

