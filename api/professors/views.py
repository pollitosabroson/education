import logging

from rest_framework import generics

from professors.models import Professor
from professors.serializers import ProfessorSerializer

logger = logging.getLogger(__name__)


class ProfessorsListCreateViewSet(generics.ListCreateAPIView):
    """Endpoint to create a teacher within the platform."""

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get(self, request, *args, **kwargs):
        """You get the list of all the existing professors on the platform."""
        return super(
            ProfessorsListCreateViewSet, self
        ).get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Endpoint to create a teacher within the platform."""
        return super(
            ProfessorsListCreateViewSet, self
        ).create(request, *args, **kwargs)


class ProfessorViewSet(generics.RetrieveAPIView):
    """Endpoint to get a professor's profile"""

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'public_id'
