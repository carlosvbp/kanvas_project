import uuid
from django.db import models
from django.db import models


class Content(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="contents"
    )
