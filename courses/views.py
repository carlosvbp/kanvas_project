from accounts.models import Account
from courses.models import Course
from courses.permissions import IsAdminUser, IsSuperUserOrParticipant
from courses.serializers import (
    CourseDetailSerializer,
    CourseSerializer,
    RetrieveUpdateStudentCourseSerilizer,
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserOrParticipant]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return self.queryset.all()


class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserOrParticipant]
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_url_kwarg = "course_id"


class RetrieveUpdateStudentCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = RetrieveUpdateStudentCourseSerilizer
    lookup_url_kwarg = "course_id"
