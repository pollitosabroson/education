import logging

from rest_framework import generics

from professors.models import Professor
from professors.serializers import ProfessorSerializer

logger = logging.getLogger(__name__)


class ProfessorsListCreateViewSet(generics.ListCreateAPIView):
    """Create and list all users."""

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorViewSet(generics.RetrieveAPIView):
    """Single profile for professor."""

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'public_id'
