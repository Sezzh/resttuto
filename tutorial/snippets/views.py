from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import (
    SnippetModelSerializer as SnippetSerializer, UserSerializer
)
from snippets.permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_queryset(self):
        snippet_pk = self.kwargs['snippet_pk']
        try:
            return Snippet.objects.get(pk=snippet_pk)
        except DoesNotExist:
            raise Http404

    # muchas dudas aqui
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset
        self.check_object_permissions(self.request, obj)
        return obj


class UserSnippetList(generics.ListAPIView):

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Snippet.objects.filter(owner_id=pk)

    def list(self, request, pk):
        queryset = self.get_queryset()
        serializer = SnippetSerializer(queryset, many=True)
        return Response(serializer.data)
