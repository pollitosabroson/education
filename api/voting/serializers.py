import logging

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from courses.models import Course
from professors.models import Professor

from .models import Vote

logger = logging.getLogger(__name__)


class VotingSerializer(serializers.Serializer):
    """Voting Serializer."""

    PROFESSOR = 'professor'
    COURSE = 'course'

    CHOICES = (
        (PROFESSOR, _('Professor')),
        (COURSE, _('Course')),
    )

    CHOICE_MODELS = {
        PROFESSOR: Professor,
        COURSE: Course
    }

    value = serializers.IntegerField(
        max_value=settings.MAX_VALUE_VOTE,
        min_value=settings.MIN_VALUE_VOTE,
        help_text=_(
            f'Only values ​​between {settings.MIN_VALUE_VOTE} '
            'and {settings.MAX_VALUE_VOTE} are accepted'
        ),
        required=True,
    )
    id = serializers.CharField(
        required=True,
        max_length=settings.LONG_PUBLIC_ID,
        help_text=_(
            'Object ID that we are going to evaluate'
        )
    )
    choices = serializers.ChoiceField(
        choices=CHOICES,
        help_text=_(
            'Options that can be voted on'
        )
    )

    def to_representation(self, instance):
        """Create a public representation of the professor.
        Args:
            Instance(Instance): Instance of professor
        Return:
            Dict: Dicrt
        """
        return instance.content_object.vote_representation()

    def validate(self, data):
        """Validate all values.
        Args:
            data(Instance): all values of serializer
        """
        choice = data.get('choices')
        if choice not in self.CHOICE_MODELS.keys():
            raise serializers.ValidationError(
                _('The selected value does not exist')
            )
        model = self.CHOICE_MODELS.get(choice)
        value = model.objects.filter(
            public_id=data.get('id')
        )
        if not value.exists():
            raise serializers.ValidationError(
                {'id': _(f'The {choice} id does not exist')}
            )
        data['id'] = value.first()

        return data

    def create(self, validate_data):
        """Create new vote.
        Args:
            validate_data(instance): Instance with all the data of the
            serializers and values ​​of the view
        """
        vote = Vote.create(
            value=validate_data.get('value'),
            content_object=validate_data.get('id')
        )
        return vote
