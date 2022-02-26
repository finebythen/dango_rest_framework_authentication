from tokenize import Token
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import AuthorSerializer, BookSerializer
from app_auth.models import Author, Book


@api_view(['GET'])
def api_routes(request):
    routes = {
        'authors all': 'api/authors/',
        'author detail': 'api/authors/<int:pk>/',
        'books all': 'api/books/',
    }
    return Response(routes)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_authors_all_view(request):
    try:
        qs = Author.objects.all()
        serializer = AuthorSerializer(qs, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except (ConnectionError, ConnectionAbortedError):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def api_authors_detail_view(request, pk):
    try:
        qs = Author.objects.get(id=pk)
        serializer = AuthorSerializer(qs, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except (ConnectionError, ConnectionAbortedError):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_books_all_view(request):
    try:
        qs = Book.objects.all()
        serializer = BookSerializer(qs, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except (ConnectionError, ConnectionAbortedError):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)