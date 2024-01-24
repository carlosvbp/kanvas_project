import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=100)
    my_courses = models.ManyToManyField(
        "courses.Course",
        through="students_courses.StudentCourse",
        related_name="students",
    )
