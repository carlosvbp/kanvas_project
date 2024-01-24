from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from utils.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class GenericView(APIView):
    queryset = None
    serializer_class = None


class CreateAPIView(GenericView, CreateModelMixin):
    def post(self, request: Request) -> Response:
        return self.create(request)


class ListAPIView(GenericView, ListModelMixin):
    def get(self, request: Request) -> Response:
        return self.list(request)


class ListCreateAPIView(ListAPIView, CreateAPIView):
    ...


class RetrieveAPIView(GenericView, RetrieveModelMixin):
    def get(self, request: Request, pk: str) -> Response:
        return self.retrieve(request)


class UpdateAPIView(GenericView, UpdateModelMixin):
    def patch(self, request: Request, pk: str) -> Response:
        return self.partial_update(request, pk)


class DestroyAPIView(GenericView, DestroyModelMixin):
    def delete(self, request: Request, pk: str) -> Response:
        return self.destroy(request, pk)


class RetrieveUpdateDestroyAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    ...
