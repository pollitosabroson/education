import logging

from rest_framework import generics

from .models import Vote
from .serializers import VotingSerializer

logger = logging.getLogger(__name__)


class VoteCreateViewSet(generics.CreateAPIView):
    """Endpoint to obtain voting within the platform for a course or a teacher,
    in this endpoint an option from the following is required.
    ## choices
    {choices}
    """
    __doc__ = __doc__.format(
        choices="""
            """.join(
            "    * {choice}".format(
                choice=v
            ) for k, v in VotingSerializer.CHOICES)
    )

    queryset = Vote.objects.all()
    serializer_class = VotingSerializer
