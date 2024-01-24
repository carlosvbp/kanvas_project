from django.urls import path
from contents.views import CreateContentView, RetrieveUpdateDestroyContentView


urlpatterns = [
    path("courses/<str:course_id>/contents/", CreateContentView.as_view()),
    path(
        "courses/<str:course_id>/contents/<str:content_id>/",
        RetrieveUpdateDestroyContentView.as_view(),
    ),
]
