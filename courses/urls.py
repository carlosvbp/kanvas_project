from django.urls import path
from courses.views import (
    ListCreateCourseView,
    RetrieveUpdateDestroyCourseView,
    RetrieveUpdateStudentCourseView,
)


urlpatterns = [
    path("courses/", ListCreateCourseView.as_view()),
    path("courses/<str:course_id>/", RetrieveUpdateDestroyCourseView.as_view()),
    path(
        "courses/<str:course_id>/students/", RetrieveUpdateStudentCourseView.as_view()
    ),
]
