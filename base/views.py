from .models import Filme
from . serializers import FilmeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def filmes(request):

    if request.method == "GET":
        filmes = Filme.objects.all()
        filme_serializer = FilmeSerializer(filmes, many=True)
        return Response(filme_serializer.data)
    
    if request.method == "POST":
        filme_serializer = FilmeSerializer(data=request.data)
        if filme_serializer.is_valid():
            filme_serializer.save()
            return Response(filme_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def filme_detail(request, id):

    try:
        filme = Filme.objects.get(id=id)
    except Filme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == "GET":
        filme_serializer = FilmeSerializer(filme)
        return Response(filme_serializer.data)

    elif request.method == "PUT":
        filme_serializer = FilmeSerializer(filme, data=request.data)
        if filme_serializer.is_valid():
            filme_serializer.save()
            return Response(filme_serializer.data, status=status.HTTP_200_OK)
        return Response(filme_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#get filmes
#serializa
#retorna json