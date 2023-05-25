from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Filme
from .serializers import FilmeSerializer

class FilmesAPIView(APIView):
    def get(self, request):
        filmes = Filme.objects.all()
        filme_serializer = FilmeSerializer(filmes, many=True)
        return Response(filme_serializer.data)

    def post(self, request):
        filme_serializer = FilmeSerializer(data=request.data)
        if filme_serializer.is_valid():
            filme_serializer.save()
            return Response(filme_serializer.data, status=status.HTTP_201_CREATED)
        return Response(filme_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmeDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Filme.objects.get(id=id)
        except Filme.DoesNotExist:
            return None

    def get(self, request, id):
        filme = self.get_object(id)
        if filme is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        filme_serializer = FilmeSerializer(filme)
        return Response(filme_serializer.data)

    def put(self, request, id):
        filme = self.get_object(id)
        if filme is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        filme_serializer = FilmeSerializer(filme, data=request.data)
        if filme_serializer.is_valid():
            filme_serializer.save()
            return Response(filme_serializer.data, status=status.HTTP_200_OK)
        return Response(filme_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        filme = self.get_object(id)
        if filme is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        filme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#get filmes
#serializa
#retorna json