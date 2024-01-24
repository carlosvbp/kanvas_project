from contents.models import Content
from contents.serializers import ContentSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from courses.models import Course
from courses.permissions import IsAdminOrParticipantReadOnly, IsAdminUser


class CreateContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})
        serializer.save(course=course)


class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParticipantReadOnly]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_object(self):
        try:
            Course.objects.get(pk=self.kwargs["course_id"])
            content = Content.objects.get(pk=self.kwargs["content_id"])
            print(content)
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        self.check_object_permissions(self.request, content)
        return content
