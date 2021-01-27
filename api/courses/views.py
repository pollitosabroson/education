import logging

from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer

logger = logging.getLogger(__name__)


class CoursesListCreateViewSet(generics.ListCreateAPIView):
    """Endpoint to create cursor within the platform, to create a course,
        the ID of a teacher is always required."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        """You get the list of all the existing courses on the platform."""
        return super(
            CoursesListCreateViewSet, self
        ).get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Endpoint to create cursor within the platform, to create a course,
        the ID of a teacher is always required."""
        return super(
            CoursesListCreateViewSet, self
        ).create(request, *args, **kwargs)


class CourseViewSet(generics.RetrieveAPIView):
    """Endpoint to obtain a course within the platform."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'public_id'
