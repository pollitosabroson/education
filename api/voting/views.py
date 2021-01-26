import logging

from rest_framework import generics

from .models import Vote
from .serializers import VotingSerializer

logger = logging.getLogger(__name__)


class VoteCreateViewSet(generics.CreateAPIView):
    """Create and list all users."""

    queryset = Vote.objects.all()
    serializer_class = VotingSerializer
