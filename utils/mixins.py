from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class ListModelMixin:
    queryset = None
    serializer_class = None

    def list(self, request: Request) -> Response:
        queryset = self.queryset.all()
        return Response(self.serializer_class(queryset, many=True).data)


class CreateModelMixin:
    queryset = None
    serializer_class = None

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveModelMixin:
    queryset = None
    serializer_class = None

    def retrieve(self, request: Request, pk: str) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        return Response(self.serializer_class(instance).data)


class UpdateModelMixin:
    queryset = None
    serializer_class = None

    def partial_update(self, request: Request, pk: str) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DestroyModelMixin:
    queryset = None
    serializer_class = None

    def destroy(self, request: Request, pk: str) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
