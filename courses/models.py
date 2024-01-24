import uuid
from django.db import models
from django.db import models


class COURSE_STATUS(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)
    status = models.TextField(
        choices=COURSE_STATUS.choices, default=COURSE_STATUS.NOT_STARTED, max_length=11
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.PROTECT,
        related_name="courses",
        default=None,
        null=True,
    )
