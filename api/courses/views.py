import logging

from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer

logger = logging.getLogger(__name__)


class CoursesListCreateViewSet(generics.ListCreateAPIView):
    """Create and list all users."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseViewSet(generics.RetrieveAPIView):
    """Single profile for Course."""

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'public_id'
